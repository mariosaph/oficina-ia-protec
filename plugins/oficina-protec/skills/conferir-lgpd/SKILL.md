---
name: conferir-lgpd
description: Varre um texto, arquivo ou pasta atrás de dados pessoais (CPF, RG, telefone, e-mail, endereço, data de nascimento, dados bancários, matrícula) e de dados sensíveis (saúde, religião, raça ou etnia, política, sindicato, vida sexual, biometria, crianças) antes de algo sair da unidade, e propõe uma versão anonimizada. Use antes de enviar documento, publicar, mandar e-mail ou colar conteúdo em outro sistema, ou quando o usuário perguntar se pode compartilhar algo.
---

# Conferir LGPD antes de mandar para fora

LGPD é a Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018). Dado pessoal é o que
identifica uma pessoa ou permite identificá-la. Dado sensível (art. 5º, II) é o que fala de
origem racial ou étnica, religião, opinião política, filiação a sindicato ou a organização
religiosa, filosófica ou política, saúde, vida sexual, genética ou biometria. Dado de criança e
de adolescente tem regra própria (art. 14).

## Passos
1. Arquivo ou pasta: rode primeiro o varredor que acompanha esta skill. Ele lê o arquivo no
   computador e mostra só trechos mascarados, então o conteúdo não precisa passar por você:
   - Mac: `python3 "${CLAUDE_SKILL_DIR}/varrer.py" <arquivo ou pasta>`
   - Windows: `py "${CLAUDE_SKILL_DIR}/varrer.py" <arquivo ou pasta>`
   Ele lê .txt, .md, .csv, .docx e .eml; .pdf e .xlsx se pypdf e openpyxl estiverem instalados.
2. Texto colado na conversa: procure você mesmo os mesmos tipos (lista acima) e também nomes de
   pessoas, que o varredor não detecta.
3. Para cada achado, diga se o destino precisa daquele dado. Princípio da necessidade (art. 6º,
   III): só vai o mínimo para a finalidade.
4. Proponha a versão anonimizada, trocando por marcadores (`[CPF]`, `[E-MAIL]`) ou por papéis
   (`Servidor A`, `Empresa 1`, `Estudante 2`). Para arquivo, o varredor grava uma cópia:
   `varrer.py <arquivo> --anonimizar <arquivo-anonimizado.txt>`. O original nunca é alterado.
5. Diga o que só uma pessoa pode decidir: se há base legal para enviar, se o documento tem
   restrição de acesso no SEI, se o titular precisa ser avisado.

## Nunca
- Repetir na resposta um dado pessoal completo. Mostre mascarado: `***.***.***-35`, `f***@example.com`.
- Dizer que o documento "está livre de dados pessoais". O certo é "não encontrei" e o que não
  foi verificado (nomes, imagens, PDF digitalizado, planilhas sem leitor instalado).
- Enviar, publicar ou colar o conteúdo em outro sistema. Esta skill só confere.
- Dar parecer jurídico. Em caso de dúvida, indique o encarregado de dados da instituição.

## Formato da saída

```text
CONFERÊNCIA LGPD - [nome do arquivo ou "texto colado"] - destino: [para onde vai]

| Linha | Tipo | Trecho mascarado | Precisa ir? |
|---|---|---|---|

Dados sensíveis: [nenhum encontrado / lista com tema e linha]
Não verificado: [nomes, imagens, PDF digitalizado...]

Recomendação: [enviar como está / enviar a versão anonimizada / não enviar e por quê]
Decisão do usuário: [o que só ele pode decidir]
```

Se gerar a versão anonimizada, diga onde ficou e peça ao usuário para conferir antes de usar.
