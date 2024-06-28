---
# vim: set spell spelllang=pt_br sw=4:
title: |
       | Fundamentos de Algoritmos
       | Seleção, enumerações e estruturas
urlcolor: Blue
# TODO: adicionar exemplos que a saída é uma estrutura
---

# Começando

@) Projete uma função que determine o sinal de um número, produzindo `-1`{.python} para valores negativos, `1`{.python} para valores positivos e `0`{.python} para o `0`{.python}.

@) Projete uma função que transforme uma string para que ela tenha uma quantidade $n$ caracteres. Se a string tem mais caracteres que $n$, os caracteres excedentes do final devem ser removidos. Se a string tem menos caracteres que $n$, espaços em branco devem ser adicionados no final.

@) Projete uma função que restrinja um valor a um determinado intervalo, isto é, devolve o valor se ele está no intervalo, senão "força" o valor para dentro do intervalo devolvendo o extremo do intervalo mais próximo do valor.

@) Escolha um exemplo de cada exercício anterior e mostre a ordem que as linhas são executadas. Confiram com o Python Tutor se a sua resposta está certa.


# Avançando

@) Cada cidadão de um país, cuja moeda chama dinheiro, tem que pagar imposto sobre a sua renda. Cidadãos que recebem até 1000 dinheiros pagam 5% de imposto. Cidadãos que recebem entre 1000 e 5000 dinheiros pagam 5% de imposto sobre 1000 dinheiros e 10% sobre o que passar de 1000. Cidadãos que recebem mais do 5000 dinheiros pagam 5% de imposto sobre 1000 dinheiros, 10% de imposto sobre 4000 dinheiros e 20% sobre o que passar de 5000. Projete uma função que calcule o imposto que um cidadão deve pagar dado a sua renda.

@) Um banco emprega diferentes taxas de correção anual para um investimento dependendo do valor aplicado no início de cada ano. Para valores até R$ 2000 a taxa de correção é de 10%, para valores entre R$ 2000 e R$ 5000 a taxa de correção é de 12%, para valores maiores que R$ 5000 a taxa de correção é de 13%.

    a) Projete uma função que calcule quanto um investimento realizado no início do ano irá render após um ano aplicado no banco.

    b) Projete uma função que calcule quanto um investimento realizado no início do ano irá render após dois anos aplicado no banco. Dica: use a função do item a para fazer a implementação.

@) Em um determinado jogo os jogadores são classificados em níveis de 0 a 25 e este nível é atualizado semanalmente baseado na quantidade de horas que o jogador jogou o jogo. Os jogadores que jogaram entre 4 e 5 horas permanecem no mesmo nível. Os jogadores que jogaram menos que 4 horas diminuem um nível a cada 1 hora que faltou para alcançar as 4 horas. Os jogadores que jogaram mais de 5 horas aumentam um nível a cada hora jogada além das 5 horas respeitando o limite máximo de 7 níveis. Projete uma função que recebe o nível atual do jogador e a quantidade de horas jogadas em uma semana e calcule o novo nível do jogador.

@) Muitos letreiros exibem mensagens que tem mais caracteres do que eles podem exibir, para isso, eles exibem apenas uma porção da mensagem que é alterada com o passar do tempo. Por exemplo, em um letreiro de 20 caracteres, a mensagem `'Promocao de sorvetes, pague 2 leve 3!'` é exibida como `Promocao de sorvetes` no momento 0, como `'romocao de sorvetes,'` no momento 1, `'omocao de sorvetes, '`, no momento 3, e assim por diante até que no momento 17 é exibido `'tes, pague 2 leve 3!'`. O momento sempre aumenta, e após chegar no final da mensagem ela começa a ser exibida novamente, nesse caso, no momento 18 é exibido `'es, pague 2 leve 3! '` e no momento 19 é exibido `'s, pague 2 leve 3! P'`, onde o `P` é o início da mensagem. Projete uma função que determine os caracteres de uma mensagem que devem ser exibidos em um determinado momento em um letreiro que pode exibir um determinado número de caracteres. Você pode assumir que o número de caracteres da mensagem é maior do que o do letreiro. A sua implementação usa seleção? Você consegue fazer uma implementação que não utiliza seleção?
