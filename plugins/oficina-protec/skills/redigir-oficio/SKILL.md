---
name: redigir-oficio
description: Redige ofícios e outras comunicações oficiais no padrão ofício do Manual de Redação da Presidência da República (3ª edição, 2018), com identificação, data, endereçamento, assunto, texto, fecho e signatário. Use quando o usuário pedir ofício, memorando, comunicação oficial, resposta a ofício, convite institucional ou encaminhamento de documento. Nunca inventa número de ofício ou de processo SEI, nome, cargo, data ou valor; marca [CONFERIR].
---

# Redigir ofício (padrão ofício)

Base: Manual de Redação da Presidência da República, 3ª edição (2018), e Decreto nº 9.758/2019.
Desde a 3ª edição, memorando e aviso também seguem o padrão ofício e se chamam ofício.

## Antes de escrever, junte
1. Quem assina (nome e cargo) e o setor que expede, com as siglas.
2. Destinatário: cargo, setor, órgão e endereço. É da administração pública federal ou não?
3. O objetivo em uma frase: informar, solicitar, convidar, responder ou encaminhar.
4. Referências: o ofício ou processo a que responde e os documentos anexos.
Se faltar algo, pergunte uma vez, em lista curta. O que continuar faltando vira `[CONFERIR: ...]`.

## Estrutura, nesta ordem
1. Cabeçalho: órgão e setores, centralizado. No SEI, o modelo já traz.
2. Identificação, à esquerda: `OFÍCIO Nº [CONFERIR: número]/2026/[SIGLA DO SETOR]/[SIGLA DO ÓRGÃO]`
   (siglas da menor para a maior hierarquia). No SEI, o número é gerado pelo sistema.
3. Local e data, à direita: `Manaus, 5 de outubro de 2026.` Sem sigla do estado, dia sem zero
   à esquerda (o dia 1 em ordinal: 1º), mês em minúscula, ponto final.
4. Endereçamento, à esquerda, com o endereço em duas linhas (logradouro; CEP e cidade/UF).
   Veja a regra de tratamento abaixo.
5. Assunto, em negrito, sem verbo, de quatro a cinco palavras, com ponto final:
   `Assunto: Convite para reunião técnica.`
6. Vocativo: `Senhor Diretor,` ou `Senhora Coordenadora,`.
7. Texto:
   - Comunicação: introdução direta ("Solicito", "Informo", "Convido"; evite "Tenho a honra de" e
     "Cumpre-me informar"), desenvolvimento com uma ideia por parágrafo, conclusão com o pedido.
   - Encaminhamento: comece pela referência ("Em resposta ao Ofício nº ..., encaminho ...") ou
     pelo motivo, com os dados do documento encaminhado (tipo, data, origem, assunto).
   - Numere os parágrafos só se houver três ou mais; vocativo e fecho não se numeram.
8. Fecho: `Respeitosamente,` para hierarquia superior; `Atenciosamente,` para a mesma
   hierarquia, inferior e demais casos.
9. Signatário, centralizado: NOME EM MAIÚSCULAS (sem negrito e sem linha acima) e, abaixo, o
   cargo só com iniciais maiúsculas.

## Tratamento
- Destinatário da administração pública federal (outra universidade federal, ministério,
  instituto federal): pelo Decreto nº 9.758/2019, o único tratamento é "senhor" ou "senhora".
  Ficam vedados "Vossa Excelência", "Excelentíssimo", "Vossa Senhoria", "Vossa Magnificência",
  "doutor", "ilustre", "digníssimo" e "respeitável". O endereçamento leva só cargo, setor e
  endereço (ex.: `Ao Pró-Reitor de Pesquisa`), sem pronome e sem nome; o nome entra só se o
  cargo não bastar ou se o ofício for para aquela pessoa (`Ao Senhor Fulano de Tal`).
- Destinatário fora da administração federal (prefeitura, governo do estado, Judiciário,
  Legislativo, empresa) ou autoridade estrangeira: siga a tabela do Manual. Autoridade de Vossa
  Excelência: `A Sua Excelência o Senhor`; demais: `Ao Senhor` ou `À Senhora` (nunca "A Sua
  Senhoria o Senhor").
- Se o setor tiver orientação própria, ela vale. Na dúvida, marque `[CONFERIR: tratamento]`.

## Formatação, quando gerar arquivo (no SEI, o editor cuida disso)
Use o modelo do SEI da UFAM, abaixo: ele já sai com a cara do ofício que o SEI imprime. Sem o modelo:
Calibri ou Carlito 12 (citações 11, notas 10). Margens: esquerda 3 cm, direita 1,5 cm, superior e
inferior 2 cm. Texto justificado, entrelinha simples, 6 pt depois de cada parágrafo, recuo de
2,5 cm. Número de página a partir da segunda. Destaque só com negrito, sem abuso.

## Arquivo .docx no modelo da UFAM para o SEI
Quando pedirem o ofício em .docx ou "com o modelo da UFAM para o SEI" (no Mac, troque `py` por `python3`):
1. Escreva `saida/oficio.json` com os campos; `py "${CLAUDE_SKILL_DIR}/preencher_oficio.py" --exemplo` mostra todos
   (o texto vai em `paragrafos`; `itens` só com três pontos ou mais). O que você não sabe fica fora do
   .json (segue em amarelo no arquivo) ou vira `[CONFERIR: ...]`. Número do ofício e do processo: o SEI dá.
2. Rode `py "${CLAUDE_SKILL_DIR}/preencher_oficio.py" saida/oficio.json` (sem a biblioteca: `py -m pip install python-docx`)
   e diga onde o arquivo ficou, com a lista "Para conferir" que o script mostrou.
Assinatura eletrônica, QR, código verificador e CRC o SEI gera ao assinar; no SEI a pessoa cola o texto no
editor do Ofício, e o .docx serve para revisar antes. Modelo: `modelo-oficio-sei-ufam.docx`, nesta pasta.

## Nunca
- Inventar número de ofício ou de processo SEI, nome, cargo, data, prazo, valor, lei ou artigo.
- Copiar dado pessoal que o ofício não precisa (CPF, endereço residencial, telefone pessoal).
- Usar fecho antigo ("Sem mais para o momento", "Cordialmente") ou sublinhado e itálico como destaque.

## Saída
1. O ofício completo em texto simples, pronto para colar no SEI.
2. Abaixo, `Para conferir:` com cada `[CONFERIR]` e a dúvida de tratamento, se houver.
3. Uma linha dizendo o tipo (comunicação ou encaminhamento) e por que escolheu aquele fecho.
4. Se a pessoa pediu .docx: o caminho do arquivo gerado no modelo da UFAM para o SEI.
