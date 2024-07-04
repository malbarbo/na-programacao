---
# vim: set spell spelllang=pt_br sw=4:
title: |
       | Fundamentos de Algoritmos
       | Tipos de dados
urlcolor: Blue
# TODO: adicionar exemplos que a saída é uma estrutura
---

# Começando

@) O que é um tipo de dado?

@) Qual é o propósito da etapa de definição de tipos de dados no processo de projeto de funções?

@) Quais são os princípios que podemos utilizar para determinar se um tipo de dado é adequado para
representar uma informação?

@) Quando devemos utilizar enumerações para representar informações?

@) De que forma enumerações como entrada para funções guiam a criação dos exemplos e a implementação da função?
<!--TODO: colocar no material essa informação! -->

@) Quando devemos utilizar estruturas para representar informações?


# Praticando

@) Projete uma enumeração para representar as direções norte, leste, sul e oeste. Em seguida,

    a) Projete uma função que indique a direção oposta de uma direção.

    a) Projete uma função que indique qual é direção que está a 90 graus no sentido horário de outra direção.

    a) Projete uma função que indique qual é direção que está a 90 graus no sentido anti-horário de outra direção. Use a função do item b para fazer a implementação (não use seleção nem operações aritméticas nessa implementação).

@) Projete uma enumeração para representar o estado de um elevador que pode estar parado, subindo ou descendo. Em seguida,

    a) Sabendo que um elevador está parado e irá atender imediatamente uma solicitação, projete uma função que determine, a partir do andar atual e do andar solicitado, qual será a condição do elevador ao atender a solicitação.

    b) Sabendo que um elevador só pode começar a se movimentar se estiver parado, projete uma função que verifique se o elevador pode passar de um estado para outro. Faça uma tabela que mostre as nove possibilidades de entrada da função e a saída de cada possibilidade. Faça os exemplos a partir da tabela. Faça a implementação simplificada a partir da tabela.

@) Projete um estrutura para representar uma data com dia, ano e mês. Em seguida

    a) Projete uma função que verifique se uma data é o último dia do ano.

    a) Projete uma função que receba duas datas e produza verdadeiro se a primeira vem antes que a segunda.

    a) (Desafio) Projete uma função que verifique se uma data é válida. Considere que em anos bissextos fevereiro tem 29 dias e que um ano é bissexto se é múltiplo de 400 ou é múltiplo de 4 mas não é múltiplo de 100.

@) Projete uma estrutura para representar resoluções (altura e largura em pixels) de telas e imagens. Em seguida

    a) Projete uma função que determine quantos mega pixels uma imagem tem dada a sua resolução. O número de megapixel pode ser caculado multiplicando-se a altura e largura e dividindo-se por 1 milhão.

    a) Projete uma função que receba duas resoluções, uma de uma imagem e outra de uma tela, e verifique se a imagem pode ser exibida completamente na tela sem a necessidade de rotação ou redução de tamanho.

    a) Projete uma função que indique se uma resolução tem aspecto (razão entre largura e altura) de 4:3, 16:9 ou outro (projete um tipo enumerado para representar o aspecto). Por exemplo, a resolução $1080 \times 1920$ tem aspecto 16:9, pois $1080 \times 16 = 1920 \times 9$.

    <!-- TODO: adicionar um item sobre fator de escala -->


# Avançando

@) Dizemos que o nome de uma pessoal é curto se tem no máximo quatro letras e longo se tem mais que 8 letras. Um nome que não é nem curto e nem longo é mediano. Projete uma função que classifique um nome de acordo com seu número de letras.

@) O Brasil institui há algum tempo um sistema de bandeira tarifária para sinalizar ao consumidores os custos reais de geração de energia. Nesse sistema, a bandeira verde indica condições favoráveis de geração de energia e a tarifa não sofre acréscimo. Já a bandeira amarela indica condições menor favoráveis e por isso a tarifa sofre um acréscimo de R$ 0,01874 para cada quilowatt-hora. A bandeira vermelha - patamar 1 indica condições mais custosas de geração e o acréscimo na tarifa é de R$ 0,03971 para cada quilowatt-hora consumido. Por fim, a bandeira vermelha - patamar 2 indica condições ainda mais custosas e o acréscimo na tarifa é de R$ 0,09492 para cada quilowatt-hora consumido. Projete uma função que determine o valor final que o consumidor tem que pagar dado o seu consumo em quilowatt-hora, a tarifa básica do quilowatt-hora e a bandeira tarifária.

@) A nota final em um disciplina é calculada pela média simples de 4 avaliações que valem de 0 a 10. A partir da nota final os alunos ficam em um de três situações: Aprovado, alunos com nota final maior ou igual a 7. Reprovado, alunos com nota menor que 4. Exame, alunos com nota maior igual a 4 e menores que 7. Projete uma função que indique a situação de um aluno dado as 4 notas das suas avaliações.

@) Beatriz gosta muito de jogar cartas com as amigas. Para treinar memória e raciocínio lógico, ela inventou um pequeno passatempo com cartas enumeradas de 1 a 13. Ela retira as três primeiras cartas do topo de um baralho bem embaralhado, e as coloca em sequência, da esquerda para a direita, na mesa, com as faces voltadas para cima. Então ela olha, por um breve instante, cada uma das cartas da sequência e logo as recoloca na mesa, com a face para baixo. Usando apenas a sua memória, Beatriz deve agora dizer se a sequência de cartas está ordenada crescentemente, decrescentemente, ou não está ordenada. De tanto jogar, ela está ficando cansada e não confia em seu próprio julgamento para saber se acertou ou errou. Por isso, ela pediu para você fazer um programa que, dada uma sequência de três cartas, determine se a sequência dada está ordenada crescentemente, decrescentemente, ou não está ordenada.

@) Jokenpô é um jogo recreativo bastante conhecido no Brasil. Nele dois participantes esticam a mão simultaneamente e formam um símbolo, que pode ser pedra, papel ou tesoura. A decisão de quem ganha é feita da seguinte forma: a pedra ganha da tesoura, a tesoura ganha do papel, e o papel ganha da pedra. Projete uma função que determine a partir do nome e símbolo feito por dois jogadores, quem ganhou no jogo.

@) Em um concurso público a classificação dos candidatos é feita pelos pontos (0 a 100) obtidos em um prova, no caso de empate, o candidato com o menor número de inscrição é classificado primeiro. Dado as informações de dois candidatos do concurso, projete uma função que determine o candidato melhor classificado.

@) Considere um jogo onde o personagem está em um tabuleiro (semelhante a um tabuleiro de jogo de xadrez). As linhas e colunas do tabuleiro são enumeradas de 1 a 10, dessa forma, é possível representar a posição (casa) do personagem pelo número da linha e da coluna que ele se encontra. O personagem fica virado para uma das direções: norte, sul, leste ou oeste. O jogador pode avançar o seu personagem qualquer número de casas na direção que ele está virado, mas é claro, não pode sair do tabuleiro. Projete uma função que indique a partir das informações do personagem, qual é o número máximo de casas que ele pode avançar na direção que ele está virado.

@) Uma determinada sala de reunião pode ser usada das 8:00h às 18:00h. Cada interessado em utilizar a sala faz uma reserva indicando o intervalo de tempo que gostaria de utilizar a sala. Como parte de um sistema de reservas, você deve projetar uma função que verifique se duas reservas podem ser atendidas, ou seja, não têm conflito de horário.

@) O desempenho de um time de futebol em um determinado campeonato é dado pelo número de pontos, número   de vitórias e saldo de gols (diferenças entre todos os gols marcados e sofridos), nessa ordem. Caso dois times empatem nesse critérios, a ordem alfabética dos nomes é usado para desempate.

    a) Projete uma função que determine qual de dois times tem o melhor desempenho.

    b) Considerando que cada jogo ganho pelo time dá 3 pontos e empate 1 ponto, projete uma função que atualize o desempenho de um time dado o resultado de um jogo.

@) Segundo a Wikipédia, um pixel é o menor elemento de um dispositivo de exibição, como por exemplo, um monitor, ao qual é possível atribuir uma cor. Nos monitores atuais, os pixels são organizados em linhas e colunas, de maneira a formar a imagem exibida. Cada pixel pode ser referenciado por uma coordenada, que é o número da linha e coluna que ele aparece. Por exemplo, em um monitor de 1920 colunas por 1080 linhas, o pixel no canto superior esquerdo está na posição (0, 0), enquanto o pixel no canto inferior direito está na posição (1919, 1079).

    Em um ambiente gráfico com janelas, quando o usuário faz um clique com o mouse é necessário identificar em qual janela ocorreu o clique.

    a) Projete uma função que receba como parâmetros as informações sobre uma janela e um clique do mouse e determine se o clique aconteceu sobre a janela.

    b) (Desafio) Projete uma função que verifique se os espaços de duas janelas se sobrepõem.
