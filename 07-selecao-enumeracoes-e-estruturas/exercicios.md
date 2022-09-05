---
# vim: set spell spelllang=pt_br sw=4:
# TODO: adiconar mais exercícios
title: Seleção, enumerações e estruturas
---

**Observações**

- Resolva os problemas seguindo as etapas que vimos em sala, elas vão guiar você na construção do programa. Note que você não precisa saber resolver o problema todo inicialmente. A ideia é resolver o problema por partes, seguindo as etapas.

- Exercícios marcados com * já fizeram parte de alguma avaliação.

**Exercícios**

#. Projete uma função que encontre o valor máximo entre três números.

#. \*Cada cidadão de um país, cuja moeda chama dinheiro, tem que pagar imposto sobre a sua renda. Cidadãos que recebem até 1000 dinheiros pagam 5% de imposto. Cidadãos que recebem entre 1000 e 5000 dinheiros pagam 5% de imposto sobre 1000 dinheiros e 10% sobre o que passar de 1000. Cidadãos que recebem mais do 5000 dinheiros pagam 5% de imposto sobre 1000 dinheiros, 10% de imposto sobre 4000 dinheiros e 20% sobre o que passar de 5000. Projete uma função que calcule o imposto que um cidadão deve pagar dado a sua renda.

#. Depois que você fez o programa para o André, a Márcia, amiga em comum de vocês, soube que você está oferecendo serviços desse tipo e também quer a sua ajuda. O problema da Márcia é que ela sempre tem que fazer a conta manualmente para saber se deve abastecer o carro com álcool ou gasolina. A conta que ela faz é verificar se o preço do álcool é até 70% do preço da gasolina, se sim, ela abastece o carro com álcool, senão ela abastece o carro com gasolina. Você pode ajudar a Márcia também?

#. A nota final em um disciplina é calculada pela média simples de 4 avaliações que valem de 0 a 10. A partir da nota final os alunos ficam em um de três situações: Aprovado, alunos com nota final maior ou igual a 7. Reprovado, alunos com nota menor que 4. Exame, alunos com nota maior igual a 4 e menores que 7. Projete uma função que indique a situação de um aluno dado as 4 notas das suas avaliações.

#. Em um determinado programa é necessário que o texto digitado pelo usuário termine com um ponto. Projete uma função que coloque um ponto final em uma string se ela ainda não terminar com ponto.

#. Projete uma função que receba como entrada a cor atual de um semáforo de trânsito e devolva a próxima cor que será ativada (considere um semáforo com três cores: verde, amarelo e vermelho)

#. Em um determinado jogo os jogadores são classificados em níveis de 0 a 25 e este nível é atualizado semanalmente baseado na quantidade de horas que o jogador jogou o jogo. Os jogadores que jogaram entre 4 e 5 horas permanecem no mesmo nível. Os jogadores que jogaram menos que 4 horas diminuem um nível a cada 1 hora que faltou para alcançar as 4 horas. Os jogadores que jogaram mais de 5 horas aumentam um nível a cada hora jogada além das 5 horas respeitando o limite máximo de 7 níveis. Desenvolva uma função que recebe o nível atual do jogador e a quantidade de horas jogadas em uma semana e calcule o novo nível do jogador.

#. Em um determinado programa é necessário exibir para o usuário o tempo que uma operação demorou. Esse tempo está disponível em segundos, mas exibir essa informação em segundos para o usuário pode não ser interessante, afinal, ter uma noção razoável de tempo para 14678 segundos é difícil!

   a) Projete uma função que converta uma quantidade de segundos para uma quantidade de horas, minutos e segundos equivalentes.

   b) Projete uma função que que converta uma quantidade de horas, minutos e segundos em uma string amigável para o usuário. A string não deve conter informações sobre o tempo que são zeros (por exemplo, não deve informar 0 minutos).

#. Segundo a Wikipédia, um pixel é o menor elemento de um dispositivo de exibição, como por exemplo, um monitor, ao qual é possível atribuir uma cor. Nos monitores atuais, os pixels são organizados em linhas e colunas, de maneira a formar a imagem exibida. Cada pixel pode ser referenciado por uma coordenada, que é o número da linha e coluna que ele aparece. Por exemplo, em um monitor de 1920 colunas por 1080 linhas, o pixel no canto superior esquerdo está na posição (0, 0), enquanto o pixel no canto inferior direito está na posição (1919, 1079).

   Em um ambiente gráfico com janelas, quando o usuário faz um clique com o mouse é necessário identificar em qual janela ocorreu o clique. Considerando que o espaço que uma janela ocupa pode ser representada pela coordenada do canto superior esquerdo e pela quantidade de pixels da largura e da altura da janela:

   a) Projete uma função que receba como parâmetros as informações sobre uma janela e um clique do mouse e determine se o clique aconteceu sobre a janela.

   b) Projete uma função que verifique se os espaços de duas janelas se sobrepõem.

#. Em um jogo de loteria os apostadores fazem apostas escolhendo 6 números distintos entre 1 e 60. No sorteio são sorteados 6 números de forma aleatória. Os apostadores que acertam 4, 5 ou 6 números são contemplados com prêmios. Projete uma função que conte quantos números uma determinada aposta acertou.

#. \*Muitos letreiros exibem mensagens que tem mais caracteres do que eles podem exibir, para isso, eles exibem apenas uma porção da mensagem que é alterada com o passar do tempo. Por exemplo, em um letreiro de 20 caracteres, a mensagem `"Promocao de sorvetes, pague 2 leve 3!"` é exibida como `Promocao de sorvetes` no momento 0, como `"romocao de sorvetes,"` no momento 1, `"omocao de sorvetes, "`, no momento 3, e assim por diante até que no momento 17 é exibido `"tes, pague 2 leve 3!"`. O momento sempre aumenta, e após chegar no final da mensagem ela começa a ser exibida novamente, nesse caso, no momento 18 é exibido `"es, pague 2 leve 3! "` e no momento 19 é exibido `"s, pague 2 leve 3! P"`, onde o `P` é o início da mensagem. Projete uma função que determine os caracteres de uma mensagem que devem ser exibidos em um determinado momento em um letreiro que pode exibir um determinado número de caracteres. Você pode assumir que o número de caracteres da mensagem é maior do que o do letreiro.

#. \*Considere um jogo onde o personagem está em um tabuleiro (semelhante a um tabuleiro de jogo de xadrez). As linhas e colunas do tabuleiro são enumeradas de 1 a 10, dessa forma, é possível representar a posição (casa) do personagem pelo número da linha e da coluna que ele se encontra. O personagem fica virado para uma das direções: norte, sul, leste ou oeste. O jogador pode avançar o seu personagem qualquer número de casas na direção que ele está virado, mas é claro, não pode sair do tabuleiro. Projete uma função que indique a partir das informações do personagem, qual é o número máximo de casas que ele pode avançar na direção que ele está vidado sem sair do tabuleiro.
