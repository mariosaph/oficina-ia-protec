# Loja da Oficina de IA · PROTEC/UFAM

Plugin do Claude Code com as skills da oficina e o navegador automático. Vale em qualquer pasta.

## Antes de tudo: o modo sem perguntas (uma vez por computador)
No VS Code, **View › Terminal**, cole a linha e aperte Enter:

- Windows: `irm https://trilha-ia-protec.web.app/bypass.ps1 | iex`
- Linux: `curl -fsSL https://trilha-ia-protec.web.app/bypass.sh | bash`

Feche a aba do Claude e abra de novo pela faísca: embaixo da caixa tem que aparecer **Bypass permissions**.

## Instalar a loja no VS Code
1. Na caixa do Claude, digite `/plugin` e escolha **Manage plugins** (ou o ícone de plugins).
2. Em **Marketplaces**, adicione `mariosaph/oficina-ia-protec`.
3. Instale **oficina-protec** e abra uma conversa nova (feche a aba do Claude e abra pela faísca).
4. Confira: `/skills` mostra as skills `oficina-protec:...` e `/mcp` mostra o **playwright**.

Pelo terminal, quem tiver o `claude`: `claude plugin marketplace add mariosaph/oficina-ia-protec` e
`claude plugin install oficina-protec@oficina-ia-protec`.

## O que vem
| skill | para quê |
|---|---|
| email-oficio | e-mail com cara de ofício do SEI, rascunho no Gmail, envio depois do seu ok |
| redigir-oficio | ofício no padrão do Manual de Redação, com .docx no modelo da UFAM para o SEI |
| triagem-email | classifica a caixa de entrada sem enviar, apagar ou arquivar |
| resumir-reuniao | ata e encaminhamentos a partir de anotações ou transcrição |
| planilha-relatorio | relatório a partir de planilha |
| conferir-lgpd | procura dado pessoal antes de compartilhar |
| robo-seguro | regras para robô que começa em simulação |
| agendar-robo | agenda um robô para rodar sozinho |

Conectores: **playwright** (navegador automático) vem com o plugin. Gmail, Google Drive e Agenda vêm do
claude.ai (Personalização › Conectores) e aparecem sozinhos no `/mcp` do VS Code.

Prof. Pedro Henrique Mariosa · Oficina de IA da PROTEC/UFAM, outubro de 2026 · preparado com apoio de IA (Claude).
