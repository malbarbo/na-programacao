---
# vim: set spell spelllang=pt_br:
title: Projeto de programas
---

# Introdução

Até agora, projetamos **funções isoladas**: cada exemplo e exercício era uma (ou poucas) função, testada com doctests. \pause

Mas para resolver um problema de verdade, precisamos de um **programa**: algo que possamos executar, que leia uma entrada, faça o processamento e produza uma saída. \pause

Neste capítulo vamos ver o que é um programa e quais são as principais famílias de programas.


# O que é um programa

Um programa é composto de:

- **funções colaboradoras** (que já sabemos projetar) e
- um **ponto de entrada**, a função `main`, que organiza a execução. \pause

A estrutura típica é **Entrada → Processamento → Saída**:

- a entrada e a saída são a "casca" que conecta o programa ao mundo;
- o processamento é o "miolo", feito pelas funções puras que já sabemos projetar e testar.


# Três famílias de programas

Os programas podem ser classificados pela forma como recebem a entrada e interagem com o mundo:

- **em lote** (não-interativo),
- **interativo**,
- **reativo** (orientado a eventos).


# Programas em lote

Um programa **em lote** (ou não-interativo) recebe **toda a entrada de uma vez**, em geral pela linha de comando, processa e imprime o resultado, e então termina. \pause

<!-- TODO: exemplo trabalhado em lote (sys.argv, main, Entrada/Processamento/Saída) -->


# Programas interativos

Um programa **interativo** dialoga com o usuário **durante a execução**, lendo dados com `input()` e respondendo com `print()`, em um laço, até o usuário encerrar. \pause

<!-- TODO: mesmo problema do exemplo em lote, reescrito como interativo, para contrastar -->


# Programas reativos

Um programa **reativo** (orientado a eventos) fica **em execução**, reagindo a um fluxo de eventos, e não termina sozinho. \pause

Exemplos: jogos, animações e interfaces gráficas (o modelo `World` visto no material de imagens e animações) e também **serviços/servidores**. \pause

Um serviço é **reativo**, não em lote: ele não recebe tudo de uma vez, espera e responde requisições ao longo do tempo.

<!-- TODO: referenciar o material A0 (World) como a versão gráfica/prática -->


# Comparação

<!-- TODO: tabela comparando as três famílias: quando recebe a entrada, se/quando termina, exemplos -->


# Revisão

<!-- TODO: perguntas e respostas -->
