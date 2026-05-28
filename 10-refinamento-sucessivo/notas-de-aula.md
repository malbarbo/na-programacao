---
# vim: set spell spelllang=pt_br:
title: Refinamento sucessivo
---

# Introdução

Programas maiores não saem prontos de uma vez. \pause

Precisamos de uma técnica para sair de um **problema** e chegar a um **conjunto de funções** que o resolvem.


# Refinamento sucessivo

A ideia do **refinamento sucessivo** (ou decomposição *top-down*) é: \pause

- escrever o `main` em **alto nível**, descrevendo os passos da solução; \pause
- **refinar** cada passo em uma função, aplicando a receita de projeto de funções; \pause
- repetir até chegar a funções simples e fáceis de testar.


# Exemplo

<!-- TODO: exemplo trabalhado completo, um problema não-trivial decomposto passo a passo -->


# Boas práticas

- funções pequenas, com uma responsabilidade clara;
- nomes que revelam a intenção;
- testar cada função isoladamente (doctests) antes de juntar tudo.


# Revisão

<!-- TODO: perguntas e respostas -->
