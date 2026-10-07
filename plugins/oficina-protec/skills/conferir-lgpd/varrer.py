#!/usr/bin/env python3
"""
varrer.py - procura dados pessoais em arquivos ANTES de eles saírem (para o Claude, um e-mail,
um site) e mostra só trechos MASCARADOS. Assim o conteúdo não precisa passar pelo Claude.

Procura: CPF (confere o dígito), CNPJ, RG, e-mail, telefone, CEP, endereço, data de
nascimento, matrícula/SIAPE, dados bancários e PIX, placa de veículo, número de processo,
e palavras que indicam dado sensível (saúde, religião, raça/etnia, política/sindicato,
vida sexual, biometria/genética) e dado de criança ou adolescente.

Não procura: nomes de pessoas (é preciso olhar à mão). Achar nada não prova que não há dado
pessoal; é uma ajuda, não uma garantia.

Lê: .txt .md .csv .tsv .json .html .eml .docx (sem biblioteca), .pdf (com pypdf) e .xlsx (com openpyxl).

COMO RODAR (no Windows troque python3 por py)
  python3 varrer.py documento.txt
  python3 varrer.py pasta_com_arquivos
  python3 varrer.py ata.txt --anonimizar ata-anonimizada.txt    grava uma CÓPIA trocando
                                                                CPF, e-mail, telefone etc.
O arquivo original nunca é alterado.
"""

import argparse
import re
import sys
import zipfile
from pathlib import Path

TEXTO = {".txt", ".md", ".csv", ".tsv", ".json", ".html", ".htm", ".eml", ".xml"}

PADROES = [  # (tipo, expressão, troca na versão anonimizada)
    ("processo (NUP/SEI)", r"\b\d{5}\.\d{6}/\d{4}-\d{2}\b", "[PROCESSO]"),
    ("chave PIX", r"(?i)\bchave pix\b[\s:]*[^\s,;]+", "[CHAVE PIX]"),
    ("CPF", r"(?<![\d.])\d{3}\.?\d{3}\.?\d{3}-?\d{2}(?![\d-])", "[CPF]"),
    ("CNPJ", r"(?<![\d.])\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}(?!\d)", "[CNPJ]"),
    ("e-mail", r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b", "[E-MAIL]"),
    ("telefone", r"(?<!\d)(?:\+?55[\s.-]?)?\(?\d{2}\)?[\s.-]?9?\d{4}[\s.-]\d{4}(?!\d)", "[TELEFONE]"),
    ("CEP", r"(?<![\d.])\d{5}-\d{3}(?!\d)", "[CEP]"),
    ("RG", r"(?i)\bRG\b[\s:nº.°o]*\d[\d.\-]{3,}[\dxX]", "RG [RG]"),
    ("matrícula/SIAPE", r"(?i)\b(?:SIAPE|matr[íi]cula)\b[\s:nº.°o]*\d{4,}", "[MATRÍCULA]"),
    ("placa de veículo", r"\b[A-Z]{3}-?\d[A-Z0-9]\d{2}\b", "[PLACA]"),
    ("endereço", r"\b(?:Rua|R\.|Avenida|Av\.|Travessa|Tv\.|Alameda|Estrada|Rodovia|Beco|Praça|Conjunto)"
                 r"\s+(?:d[aeo]s?\s+)?[A-ZÀ-Ú0-9][^,\n;]{2,60}(?:,\s*(?:n[º°o.]\s*)?\d+)?", "[ENDEREÇO]"),
    ("data de nascimento", r"(?i)(?:nascid[oa] em|data de nascimento|nasc\.)[\s:]*\d{1,2}/\d{1,2}/\d{2,4}",
     "[NASCIMENTO]"),
    ("dados bancários", r"(?i)\b(?:ag[êe]ncia|conta corrente|conta poupan[çc]a|c/c)\b[\s:nº.]*\d[\d.\-xX]*",
     "[DADO BANCÁRIO]"),
]

SENSIVEIS = {  # LGPD, art. 5º, II, e art. 14 (crianças e adolescentes)
    "saúde": r"\b(?:CID[\s-]?\d|laudo|diagn[óo]stic\w*|doen[çc]a|atestado m[ée]dico|defici[êe]ncia|"
             r"gestante|gr[áa]vida|HIV|psiqui[áa]tric\w*|tratamento m[ée]dico|internad[oa])\b",
    "religião": r"\b(?:religi[ãa]o|religios[oa]|igreja|evang[ée]lic[oa]|cat[óo]lic[oa]|esp[íi]rita|"
                r"umbanda|candombl[ée]|terreiro)\b",
    "raça ou etnia": r"\b(?:ra[çc]a|etnia|[ée]tnic[oa]|ind[íi]gena|quilombola|cor da pele|autodeclarad[oa])\b",
    "opinião política ou sindicato": r"\b(?:filiad[oa] ao|partido pol[íi]tico|sindicato|sindicalizad[oa]|"
                                     r"filia[çc][ãa]o partid[áa]ria)\b",
    "vida sexual": r"\b(?:orienta[çc][ãa]o sexual|vida sexual|homossexual|bissexual|transexual)\b",
    "biometria ou genética": r"\b(?:biometria|biom[ée]tric[oa]|impress[ãa]o digital|DNA|gen[ée]tic[oa])\b",
    "criança ou adolescente": r"\b(?:menor de idade|crian[çc]a|adolescente|respons[áa]vel legal)\b",
}


def cpf_valido(numero):
    d = [int(c) for c in re.sub(r"\D", "", numero)]
    if len(d) != 11 or len(set(d)) == 1:
        return False
    for tamanho in (9, 10):
        soma = sum(d[i] * (tamanho + 1 - i) for i in range(tamanho))
        if (soma * 10 % 11) % 10 != d[tamanho]:
            return False
    return True


def mascarar(tipo, trecho):
    """Mostra só o bastante para achar o lugar: o fim do número ou o domínio do e-mail."""
    if tipo == "e-mail":
        usuario, dominio = trecho.split("@", 1)
        return usuario[:1] + "***@" + dominio
    if tipo in ("endereço", "dados bancários", "data de nascimento", "chave PIX"):
        palavras = trecho.split()
        return " ".join(palavras[:1]) + " ***"
    digitos = re.sub(r"\W", "", trecho)
    return "*" * max(len(digitos) - 2, 3) + digitos[-2:]


def ler(caminho):
    ext = caminho.suffix.lower()
    if ext in TEXTO:
        bruto = caminho.read_bytes()
        for cod in ("utf-8-sig", "cp1252", "latin-1"):
            try:
                return bruto.decode(cod)
            except UnicodeDecodeError:
                continue
    if ext == ".docx":
        with zipfile.ZipFile(caminho) as z:
            xml = z.read("word/document.xml").decode("utf-8", "replace")
        xml = re.sub(r"</w:p>", "\n", xml)
        return re.sub(r"<[^>]+>", "", xml)
    if ext == ".pdf":
        try:
            import pypdf
        except ImportError:
            raise RuntimeError("para ler PDF, instale o pypdf: py -m pip install pypdf")
        return "\n".join((p.extract_text() or "") for p in pypdf.PdfReader(str(caminho)).pages)
    if ext == ".xlsx":
        try:
            import openpyxl
        except ImportError:
            raise RuntimeError("para ler XLSX, instale o openpyxl: py -m pip install openpyxl")
        livro = openpyxl.load_workbook(str(caminho), read_only=True, data_only=True)
        linhas = []
        for folha in livro.worksheets:
            for linha in folha.iter_rows(values_only=True):
                linhas.append(" ; ".join("" if v is None else str(v) for v in linha))
        return "\n".join(linhas)
    return None


def varrer(texto):
    achados = []
    for n, linha in enumerate(texto.splitlines(), start=1):
        ocupado = []
        for tipo, padrao, _ in PADROES:
            for m in re.finditer(padrao, linha):
                if any(m.start() < f and m.end() > i for i, f in ocupado):
                    continue                      # o mesmo trecho já foi contado
                rotulo = tipo
                if tipo == "CPF" and not cpf_valido(m.group()):
                    rotulo = "número no formato de CPF (dígito não confere)"
                ocupado.append((m.start(), m.end()))
                achados.append((n, rotulo, mascarar(tipo, m.group())))
        for tema, padrao in SENSIVEIS.items():
            m = re.search(padrao, linha, re.I)
            if m:
                achados.append((n, f"possível dado sensível: {tema}", f'palavra "{m.group()}"'))
    return achados


def anonimizar(texto):
    for _, padrao, troca in PADROES:
        texto = re.sub(padrao, troca, texto)
    return texto


def principal():
    p = argparse.ArgumentParser(description="Procura dados pessoais e mostra só trechos mascarados.")
    p.add_argument("caminhos", nargs="+", help="arquivos ou pastas")
    p.add_argument("--anonimizar", metavar="SAIDA", help="grava uma cópia anonimizada (só com 1 arquivo)")
    args = p.parse_args()

    arquivos = []
    for c in map(Path, args.caminhos):
        if c.is_dir():
            arquivos += sorted(f for f in c.rglob("*") if f.is_file() and not f.name.startswith("."))
        elif c.is_file():
            arquivos.append(c)
        else:
            print(f"Não encontrado: {c}")
    total, lidos = 0, 0
    for arq in arquivos:
        try:
            texto = ler(arq)
        except Exception as erro:
            print(f"\n{arq.name}: não consegui ler ({erro})")
            continue
        if texto is None:
            continue
        achados = varrer(texto)
        total += len(achados)
        lidos += 1
        print(f"\n{arq.name}: {len(achados)} achado(s)")
        if achados:
            print(f"  {'linha':>5}  {'tipo':<46} trecho mascarado")
            for n, tipo, trecho in achados[:200]:
                print(f"  {n:>5}  {tipo:<46} {trecho}")
            if len(achados) > 200:
                print(f"  ... e mais {len(achados) - 200}.")
    print(f"\nTotal: {total} achado(s) em {lidos} arquivo(s) lido(s). Nomes de pessoas não são "
          "detectados: confira à mão.")

    if args.anonimizar:
        if len(arquivos) != 1:
            print("--anonimizar funciona com um arquivo de texto por vez.")
            return 1
        texto = ler(arquivos[0])
        destino = Path(args.anonimizar)
        if destino.resolve() == arquivos[0].resolve():
            print("A cópia anonimizada precisa de outro nome; o original não é alterado.")
            return 1
        destino.write_text(anonimizar(texto), encoding="utf-8")
        print(f"Cópia anonimizada gravada em {destino}. Confira antes de usar: nomes continuam lá.")
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(errors="replace")
    except AttributeError:
        pass
    sys.exit(principal())
