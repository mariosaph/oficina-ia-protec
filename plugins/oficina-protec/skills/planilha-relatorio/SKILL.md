---
name: planilha-relatorio
description: Transforma uma planilha (CSV ou XLSX) num relatório curto, com números calculados por programa e conferidos, tabela-resumo e texto explicativo. Use quando o usuário pedir relatório, resumo, balanço, totais ou "o que essa planilha mostra" a partir de uma planilha de gastos, bolsas, atendimentos, inscrições, patrimônio ou similar. Nunca faz conta de cabeça e nunca inventa número.
---

# Planilha em relatório curto

## Quando usar
- O usuário aponta uma planilha `.csv` ou `.xlsx` e quer totais, contagens, comparação entre
  grupos (setor, mês, modalidade) ou um texto para prestar contas.

## Passos
1. Pergunte, se não estiver claro: para quem é o relatório, qual período, qual coluna agrupa
   (ex.: setor) e qual coluna soma (ex.: valor).
2. Olhe a estrutura antes de calcular. Se existir o `planilha_resumo.py` do kit (pasta
   `robos`), use-o; ele faz as contas e a conferência:
   - Mac: `python3 planilha_resumo.py <arquivo> --agrupar <coluna> --somar <coluna>`
   - Windows: `py planilha_resumo.py <arquivo> --agrupar <coluna> --somar <coluna>`
   Sem ele, escreva um script Python curto para as contas e mostre o código. Conta de cabeça, não.
3. Leia a seção "Conferência" e as "Observações": linhas fora da soma, valores não numéricos,
   valores ambíguos (1.234). Se algo não conferir, pare e mostre ao usuário antes de escrever.
4. Escreva o relatório usando só os números do script. Cada número do texto tem de aparecer
   na tabela ou na saída do script.
5. Releia o texto contra a tabela: total, maiores grupos, percentuais e datas do período.

## Dados pessoais
Planilha com nome, CPF ou contato de pessoas: agrupe por categoria, nunca por pessoa, a não ser
que o relatório precise. Antes de o relatório sair da unidade, use a skill conferir-lgpd.

## Nunca
- Inventar, arredondar sem avisar ou "estimar" número que não está na planilha.
- Esconder linhas ignoradas: elas vão em Observações.
- Tirar conclusão de causa ("gastou mais porque...") sem que a planilha mostre. Pode sugerir
  hipótese, escrita como hipótese.
- Alterar a planilha original. Se for preciso limpar dados, trabalhe numa cópia.

## Formato da saída

```text
RELATÓRIO - [assunto] - [período]
Fonte: [arquivo], [n] linhas. Números calculados por [planilha_resumo.py / script], conferidos.

Resumo em três frases: [total, maior grupo, o que chama atenção]

| [Grupo] | Linhas | Total | % |
|---|---:|---:|---:|
| ... |
| Total | ... | ... | 100% |

Destaques
- [até 4 pontos, cada um com o número que o sustenta]

Observações sobre os dados
- [linhas fora da soma, valores a conferir, limitações]
```

Números no padrão brasileiro (1.234,56). Valores em reais com "R$" só se a coluna for de reais.
Depois do relatório, diga em uma linha o que o usuário deve conferir antes de enviar.
