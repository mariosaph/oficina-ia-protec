---
name: agendar-robo
description: Agenda um robô que já funciona para rodar sozinho todo dia (Agendador de Tarefas no Windows, launchd ou cron no Mac). Use quando o usuário pedir para agendar, automatizar o horário, rodar todo dia ou rodar sozinho. Só agenda robô que já rodou bem à mão; robô agendado nunca manda nada para fora.
---

# Agendar um robô

## Antes de agendar, confira com o usuário
1. O robô já rodou à mão várias vezes, em simulação e com `--executar`, e ele conferiu o resultado?
   Se não, pare e proponha rodar à mão primeiro.
2. O robô agendado só prepara (relatório, rascunho, aviso num arquivo). Se ele envia algo para fora
   (e-mail, WhatsApp, formulário), não agende: quem envia é uma pessoa.
3. Horário com folga: uma ou duas vezes por dia basta. A cada hora já é demais.
4. Os segredos estão no `.env` da pasta do robô, e não no comando agendado.

## Windows: Agendador de Tarefas
1. Na pasta do robô, crie `rodar_<robo>.cmd`:
   ```bat
   @echo off
   cd /d "%~dp0"
   if not exist logs mkdir logs
   py <robo>.py --executar >> logs\agendador.log 2>&1
   ```
2. Peça ao usuário para dar dois cliques no `.cmd` uma vez e confira se `logs\agendador.log` foi escrito.
3. Crie a tarefa com `schtasks` (mostre o comando e espere o ok):
   `schtasks /Create /TN "Oficina - <robo>" /TR "\"<caminho>\rodar_<robo>.cmd\"" /SC DAILY /ST 08:00`
4. Para testar agora: `schtasks /Run /TN "Oficina - <robo>"`. Para parar: `schtasks /Delete /TN "Oficina - <robo>"`.

## Mac: launchd (preferido; roda ao acordar se o Mac estava dormindo)
1. Crie `~/Library/LaunchAgents/br.ufam.oficina.<robo>.plist` com Label, ProgramArguments
   (`/usr/bin/python3` ou o resultado de `which python3`, o caminho do `.py` e `--executar`),
   WorkingDirectory (a pasta do robô), StartCalendarInterval (Hour 8, Minute 0) e
   StandardOutPath/StandardErrorPath em `logs/agendador.log`. Use caminhos absolutos.
2. Confira e ligue: `plutil -lint <plist>` e `launchctl bootstrap gui/$(id -u) <plist>`.
3. Teste agora: `launchctl kickstart gui/$(id -u)/br.ufam.oficina.<robo>`; leia `logs/agendador.log`.
4. Desligar: `launchctl bootout gui/$(id -u) <plist>`.
5. O macOS bloqueia sem aviso robô agendado que mexe em Mesa, Documentos ou Downloads. Prefira
   robôs que trabalham dentro da pasta de trabalho.

## Mac: cron (alternativa simples, não roda o que perdeu dormindo)
`0 8 * * * cd "<pasta do robô>" && /usr/bin/python3 <robo>.py --executar >> logs/agendador.log 2>&1`

## Casos especiais
- `organizar_pasta.py` pergunta SIM antes de mover. Agendado, use `--confirmado` (só depois de várias
  rodadas à mão); cada execução deixa em `logs/` um `movimentos-*.csv` que permite desfazer.

## Nunca
- Agendar robô que envia mensagem, e-mail ou formulário sem uma pessoa conferir antes.
- Pôr senha ou token no comando agendado.
- Agendar sem mostrar o comando ao usuário e esperar o ok.

## No fim, diga ao usuário
O nome da tarefa, o horário, onde fica o log e o comando para desligar.
