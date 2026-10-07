---
name: email-oficio
description: Escreve um e-mail com cara de ofício do SEI da UFAM (cabeçalho, número, local e data, endereçamento, assunto, texto, fecho e assinatura), grava como rascunho no Gmail pelo conector e só envia depois que a pessoa conferir e disser "pode enviar". Na Oficina de IA, o destino é inpactas@ufam.edu.br, para registrar a tarefa. Use quando pedirem "ofício por e-mail", "e-mail no modelo de ofício", "registrar a tarefa na INPACTAS" ou o exercício do dia 3.
---

# E-mail com cara de ofício (rascunho, conferência, envio)

Exercício da Oficina de IA da PROTEC/UFAM. O e-mail parece o ofício que o SEI imprime, mas é um
exercício: não tem número oficial nem assinatura eletrônica.

## 1. Junte (pergunte nas caixas de pergunta, de uma vez)
- Nome completo, cargo e a unidade (com a sigla: PROTEC, CDTECH, PROGESP...).
- A tarefa que a pessoa quer registrar: uma rotina do trabalho dela que a IA pode automatizar
  (se houver `LEIA-ME.md` ou `CLAUDE.md` nesta pasta com as rotinas, ofereça as que estão lá).
- O que ela já fez na oficina para essa tarefa (uma ou duas frases) e o que pede à INPACTAS
  (acompanhar, ajudar a testar, registrar como ideia).
O que faltar vira `[CONFERIR: ...]` em amarelo. Nunca invente nome, cargo, número ou data.

## 2. Monte o ofício em HTML (corpo do e-mail)
- Destinatário: `inpactas@ufam.edu.br`. Assunto do e-mail:
  `[Oficina IA] Ofício - <SIGLA DA UNIDADE> - <tarefa em até 6 palavras>`.
- HTML simples, só com estilo em linha (o Gmail apaga `<style>`), fonte Calibri 12 pt, largura
  máxima 680 px, nesta ordem:
  1. Cabeçalho centralizado, em negrito: `UNIVERSIDADE FEDERAL DO AMAZONAS` e, abaixo, o nome da
     unidade por extenso e a sigla.
  2. À esquerda: `OFÍCIO Nº [CONFERIR: o SEI dá o número]/2026/<SIGLA>/UFAM`.
  3. À direita: `Manaus, <dia> de <mês> de 2026.` (dia sem zero à esquerda, mês em minúscula).
  4. Endereçamento: `À Coordenação da INPACTAS` / `Universidade Federal do Amazonas` /
     `inpactas@ufam.edu.br`.
  5. `Assunto: Registro de tarefa automatizada com IA.` em negrito.
  6. Vocativo `Senhor Coordenador,` e o texto em parágrafos justificados, com recuo na primeira linha:
     a tarefa, por que ela toma tempo, o que a IA faz nela e o que se pede à INPACTAS. Até 3
     parágrafos, sem jargão.
  7. Fecho `Atenciosamente,` e a assinatura centralizada: NOME EM MAIÚSCULAS e, abaixo, o cargo.
  8. Uma linha cinza, pequena, no fim: `Exercício da Oficina de IA · PROTEC/UFAM · documento sem
     valor oficial · gerado com apoio de IA (Claude)`.
- `[CONFERIR: ...]` com fundo amarelo (`background:#fff3a0`).
- Mande também a versão em texto puro (campo `body`), com as mesmas partes.
- INPACTAS sempre em caixa-alta.

## 3. Grave o rascunho
- Use a ferramenta `create_draft` do conector Gmail (aparece como `claude.ai Gmail` no `/mcp`), com
  `to`, `subject`, `htmlBody` e `body`. Guarde o `id` do rascunho.
- Sem o conector do Gmail: pare e explique que é preciso ligar o Gmail em claude.ai › Personalização
  › Conectores e abrir uma conversa nova. Não tente outro caminho para mandar e-mail.

## 4. Mostre e espere
- Mostre o texto do ofício, o assunto, o destinatário e o link do rascunho (`viewUrl`).
- Pergunte: "Confira o rascunho no Gmail. Posso enviar para inpactas@ufam.edu.br?"
- Se pedirem mudança: apague o rascunho antigo (`delete_draft`), grave um novo e mostre de novo.

## 5. Envie só depois do ok
- Só com "pode enviar" (ou "envia", "sim, pode") escrito pela pessoa nesta conversa: use
  `send_message` com o `draftId` do rascunho. Não envie para mais ninguém e não ponha cópia.
- Se o conector não tiver `send_message`: diga para a pessoa abrir o rascunho e clicar em Enviar.
- Confirme em uma linha: enviado, para quem, com que assunto. Sugira marcar o passo na trilha.

## Nunca
- Enviar sem o "pode enviar" da pessoa nesta conversa, nem para outro endereço.
- Ler, arquivar ou apagar outros e-mails da caixa da pessoa.
- Pôr CPF, telefone pessoal ou dado de terceiro no ofício.
