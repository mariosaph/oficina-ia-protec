---
name: resumir-reuniao
description: Transforma anotações, transcrição ou gravação transcrita de uma reunião numa ata curta, com participantes, decisões, encaminhamentos (o quê, quem, até quando) e pendências. Use quando o usuário pedir ata, resumo de reunião, encaminhamentos, "o que ficou decidido" ou colar uma transcrição. Nunca inventa responsável, prazo ou decisão que não esteja no material.
---

# Resumir reunião em ata curta

## Quando usar
- O usuário cola anotações, a transcrição de uma chamada (Meet, Teams, Zoom, gravador) ou aponta
  um arquivo `.txt`, `.docx` ou `.md` com o registro da reunião.
- Pede ata, resumo, lista de encaminhamentos ou "o que cada um ficou de fazer".

## Passos
1. Leia o material inteiro antes de escrever. Se for longo, separe por assunto (pauta).
2. Identifique, para cada assunto:
   - o que foi decidido (decisão é o que o grupo aceitou, não o que alguém sugeriu);
   - quem ficou responsável e até quando, só se isso foi dito;
   - o que ficou em aberto (dúvida, informação que falta, assunto adiado).
3. Participantes: liste só quem aparece no material. Use o nome como foi dito; não complete
   sobrenome nem cargo.
4. Datas: converta "sexta que vem" em data só se a data da reunião estiver no material;
   senão, escreva como foi dito e marque `[CONFERIR: data]`.
5. Se a ata for sair da unidade (e-mail, grupo, processo), rode antes a skill conferir-lgpd e
   tire o que não precisa ir: saúde, vida pessoal, conflito entre pessoas, CPF, telefone.
6. Confira: cada encaminhamento aparece no material? Cada decisão tem de onde veio?

## Nunca
- Inventar responsável, prazo, valor ou decisão. Sem responsável definido: `[sem responsável]`.
  Sem prazo: `[sem prazo]`.
- Transformar opinião de alguém em decisão do grupo.
- Registrar fala ofensiva, desabafo ou detalhe pessoal que não muda nada para o trabalho.
- Mandar a ata para alguém: o Claude só prepara; quem envia é o usuário.

## Formato da saída

```text
ATA DE REUNIÃO
Assunto: [tema geral]
Data: [data, se constar no material] | Local ou meio: [presencial / online, se constar]
Participantes: [nomes, como aparecem]

1. [Assunto da pauta]
   Decisão: [o que ficou decidido]
   Observação: [só se for necessário para entender a decisão]

2. [Assunto da pauta]
   ...

ENCAMINHAMENTOS
| O quê | Responsável | Prazo |
|---|---|---|
| [tarefa com verbo no infinitivo] | [nome ou sem responsável] | [data ou sem prazo] |

PENDÊNCIAS E DÚVIDAS
- [o que ficou em aberto]

Próxima reunião: [se foi marcada]
```

Depois da ata, em uma linha: quantas decisões, quantos encaminhamentos sem responsável ou sem
prazo e o que o usuário precisa conferir. Ata curta: até uma página, salvo pedido diferente.
