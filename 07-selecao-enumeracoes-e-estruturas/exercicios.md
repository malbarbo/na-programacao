---
# vim: set spell spelllang=pt_br sw=4:
# TODO: adiconar mais exercícios
title: Seleção, enumerações e estruturas - Exercícios
---

#. Cada cidadão de um país, cuja moeda chama dinheiro, tem que pagar imposto sobre a sua renda. Cidadãos que recebem até 1000 dinheiros pagam 5% de imposto. Cidadãos que recebem entre 1000 e 5000 dinheiros pagam 5% de imposto sobre 1000 dinheiros e 10% sobre o que passar de 1000. Cidadãos que recebem mais do 5000 dinheiros pagam 5% de imposto sobre 1000 dinheiros, 10% de imposto sobre 4000 dinheiros e 20% sobre o que passar de 5000. Projete uma função que calcule o imposto que um cidadão deve pagar dado a sua renda.

#. Em um determinado jogo os jogadores são classificados em níveis de 0 a 25 e este nível é atualizado semanalmente baseado na quantidade de horas que o jogador jogou o jogo. Os jogadores que jogaram entre 4 e 5 horas permanecem no mesmo nível. Os jogadores que jogaram menos que 4 horas diminuem um nível a cada 1 hora que faltou para alcançar as 4 horas. Os jogadores que jogaram mais de 5 horas aumentam um nível a cada hora jogada além das 5 horas respeitando o limite máximo de 7 níveis. Projete uma função que recebe o nível atual do jogador e a quantidade de horas jogadas em uma semana e calcule o novo nível do jogador.

#. Muitos letreiros exibem mensagens que tem mais caracteres do que eles podem exibir, para isso, eles exibem apenas uma porção da mensagem que é alterada com o passar do tempo. Por exemplo, em um letreiro de 20 caracteres, a mensagem `'Promocao de sorvetes, pague 2 leve 3!'` é exibida como `Promocao de sorvetes` no momento 0, como `'romocao de sorvetes,'` no momento 1, `'omocao de sorvetes, '`, no momento 3, e assim por diante até que no momento 17 é exibido `'tes, pague 2 leve 3!'`. O momento sempre aumenta, e após chegar no final da mensagem ela começa a ser exibida novamente, nesse caso, no momento 18 é exibido `'es, pague 2 leve 3! '` e no momento 19 é exibido `'s, pague 2 leve 3! P'`, onde o `P` é o início da mensagem. Projete uma função que determine os caracteres de uma mensagem que devem ser exibidos em um determinado momento em um letreiro que pode exibir um determinado número de caracteres. Você pode assumir que o número de caracteres da mensagem é maior do que o do letreiro.

#. A nota final em um disciplina é calculada pela média simples de 4 avaliações que valem de 0 a 10. A partir da nota final os alunos ficam em um de três situações: Aprovado, alunos com nota final maior ou igual a 7. Reprovado, alunos com nota menor que 4. Exame, alunos com nota maior igual a 4 e menores que 7. Projete uma função que indique a situação de um aluno dado as 4 notas das suas avaliações.

#. Beatriz gosta muito de jogar cartas com as amigas. Para treinar memória e raciocínio lógico, ela inventou um pequeno passatempo com cartas enumeradas de 1 a 13. Ela retira as três primeiras cartas do topo de um baralho bem embaralhado, e as coloca em sequência, da esquerda para a direita, na mesa, com as faces voltadas para cima. Então ela olha, por um breve instante, cada uma das cartas da sequência e logo as recoloca na mesa, com a face para baixo. Usando apenas a sua memória, Beatriz deve agora dizer se a sequência de cartas está ordenada crescentemente, decrescentemente, ou não está ordenada. De tanto jogar, ela está ficando cansada e não confia em seu próprio julgamento para saber se acertou ou errou. Por isso, ela pediu para você fazer um programa que, dada uma sequência de três cartas, determine se a sequência dada está ordenada crescentemente, decrescentemente, ou não está ordenada.

#. Jokenpô é um jogo recreativo bastante conhecido no Brasil. Nele dois participantes esticam a mão simultaneamente e formam um símbolo, que pode ser pedra, papel ou tesoura. A decisão de quem ganha é feita da seguinte forma: a pedra ganha da tesoura, a tesoura ganha do papel, e o papel ganha da pedra. Projete uma função que determine a partir do nome e símbolo feito por dois jogadores, quem ganhou no jogo.

#. O desempenho de um time de futebol em um determinado campeonato é dado pelo número de pontos, número   de vitórias e saldo de gols (diferenças entre todos os gols marcados e sofridos), nessa ordem. Caso dois times empatem nesse critérios, a ordem alfabética dos nomes é usado para desempate.

    a) Projete uma função que determine qual de dois times tem o melhor desempenho.

    b) Considerando que cada jogo ganho pelo time dá 3 pontos e empate 1 ponto, projete uma função que atualize o desempenho de um time dado o resultado de um jogo.
