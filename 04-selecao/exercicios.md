---
# vim: set spell spelllang=pt_br sw=4:
title: |
       | Fundamentos de Algoritmos
       | Seleção
urlcolor: Blue
---

**\color{red}Lembre-se** de usar o `mypy` e o `doctest` na etapa de verificação.


# Começando

@) Qual é a forma geral da instrução `if`{.python} (incluindo `elif`{.python} e `else`{.python}) e como ela é executada pelo Python?

@) Quando "descobrimos" que precisamos utilizar seleção na implementação de uma função? Quais são as duas estratégias que podemos utilizar para implementar uma função usando seleção?


# Praticando

@) Projete uma função que transforme uma string para que ela tenha uma quantidade $n$ caracteres. Se a string tem mais caracteres que $n$, os caracteres excedentes do final devem ser removidos. Se a string tem menos caracteres que $n$, espaços em branco devem ser adicionados no final.

@) Projete uma função que determine o sinal de um número, produzindo `-1`{.python} para valores negativos, `1`{.python} para valores positivos e `0`{.python} para o `0`{.python}.

@) Projete uma função que restrinja um valor a um determinado intervalo, isto é, devolve o valor se ele está no intervalo, senão "força" o valor para dentro do intervalo devolvendo o extremo do intervalo mais próximo do valor. A sua implementação usa seleção? Você consegue fazer uma implementação usando as funções pré-definidas `min`{.python} e `max`{.python} do Python?

@) Escolha um exemplo de cada exercício anterior e mostre a ordem que as linhas são executadas. Use o Python Tutor para verificar se as respostas estão corretas.


# Avançando

@) Um banco emprega diferentes taxas de correção anual para um investimento dependendo do valor aplicado no início de cada ano. Para valores até R$ 2000 a taxa de correção é de 10%, para valores entre R$ 2000 e R$ 5000 a taxa de correção é de 12%, para valores maiores que R$ 5000 a taxa de correção é de 13%.

    a) Projete uma função que calcule quanto um investimento realizado no início do ano irá render após um ano aplicado no banco.

    b) Projete uma função que calcule quanto um investimento realizado no início do ano irá render após dois anos aplicado no banco. Dica: use a função do item a para fazer a implementação.


@) Uma palavra duplicada é formada pela ocorrência de duas partes iguais, separadas ou não por hífen. Por exemplo, as palavras xixi, mimi, lero-lero e mata-mata são palavras duplicadas. Projete uma função que verifique se uma palavra é duplicada.

@) Em um determinado jogo os jogadores são classificados em níveis de 0 a 25 e este nível é atualizado semanalmente baseado na quantidade de horas que o jogador jogou o jogo. Os jogadores que jogaram entre 4 e 5 horas permanecem no mesmo nível. Os jogadores que jogaram menos que 4 horas diminuem um nível a cada 1 hora que faltou para alcançar as 4 horas. Os jogadores que jogaram mais de 5 horas aumentam um nível a cada hora jogada além das 5 horas respeitando o limite máximo de 7 níveis. Projete uma função que recebe o nível atual do jogador e a quantidade de horas jogadas em uma semana e calcule o novo nível do jogador.

@) Muitos letreiros exibem mensagens que tem mais caracteres do que eles podem exibir, para isso, eles exibem apenas uma porção da mensagem que é alterada com o passar do tempo. Por exemplo, em um letreiro de 20 caracteres, a mensagem `'Promocao de sorvetes, pague 2 leve 3!'` é exibida como `Promocao de sorvetes` no momento 0, como `'romocao de sorvetes,'` no momento 1, `'omocao de sorvetes, '`, no momento 3, e assim por diante até que no momento 17 é exibido `'tes, pague 2 leve 3!'`. O momento sempre aumenta, e após chegar no final da mensagem ela começa a ser exibida novamente, nesse caso, no momento 18 é exibido `'es, pague 2 leve 3! '` e no momento 19 é exibido `'s, pague 2 leve 3! P'`, onde o `P` é o início da mensagem. Projete uma função que determine os caracteres de uma mensagem que devem ser exibidos em um determinado momento em um letreiro que pode exibir um determinado número de caracteres. Você pode assumir que o número de caracteres da mensagem é maior do que o do letreiro. A sua implementação usa seleção? Você consegue fazer uma implementação que não utiliza seleção?
