---
# vim: set spell spelllang=pt_br sw=4:
title: |
       | Fundamentos de Algoritmos
       | Repetição e arranjos
urlcolor: Blue
# TODO: fazer exercícios mais interessantes (reais).
# TODO: adicionar exercícios de avaliação de expressões e execução passo a passo?
---

**\color{red}Lembre-se** de seguir o processo de projeto de funções e de usar o `mypy` e o `doctest` na etapa de verificação.

# Começando

@) Quando devemos utilizar arranjos para representar informações?

@) O que são valores mutáveis e valores imutáveis?

@) O que são efeitos colaterais?

@) Como distinguir quando devemos utilizar estruturas e quando devemos utilizar arranjos para representar informações?

@) Qual é a forma geral da instrução "para cada" e como ela é executada?

@) Podemos armazenar valores de tipos diferentes em um mesmo arranjo? Explique.

@) Quando devemos utilizar a abordagem incremental?

@) Quais são as três perguntas que precisamos responder para implementar uma função utilizando a abordagem incremental com o "para cada"?


# Praticando

<!-- Básico -->

@) Projete uma função que concatene todos os elementos de uma lista de strings.

@) Projete uma função que crie uma lista de números a partir de uma lista de strings convertendo cada string para um número. Assuma que todas as strings representam números válidos.

@) Projete uma função que calcule o produto de todos os elementos de uma lista de inteiros.


<!-- Seleção -->

@) Projete uma função que verifique se todos os elementos de uma lista de inteiros são pares.

@) Projete uma função que verifique se todos os elementos de uma lista de booleanos são falsos.

@) Projete uma função que crie uma nova lista removendo todas os valores zeros de uma lista de inteiros.


<!-- Esboço e calculo de mais de um valor-->

@) Projete uma função que conte quantas vezes o valor mínimo de uma lista de inteiros não vazia aparece na lista.

    a) Esboce uma solução em duas etapas e depois implemente a função.

    a) Faça uma implementação alternativa que use apenas uma repetição.

    a) Avalie qual das implementações é mais simples.

@) Projete uma função que calcule a amplitude dos valores de uma lista não vazia de números, isto é, a diferença entre o maior e menor valor da lista.

    a) Esboce uma solução em três etapas e depois implemente a função.

    a) Faça uma implementação alternativa que use apenas uma repetição.

    a) Avalie qual das implementações é mais simples.

@) Projete uma função que indique se uma lista de inteiros tem mais valores positivos ou negativos.

@) Projete uma função que receba como entrada uma lista de números e crie uma nova lista colocando os valores negativos da lista de entrada antes dos positivos.


# Resolvendo problemas

<!-- Para cada -->

@) O Miguel é doutorando em física e precisa coletar dados de um experimento, mas ele só tem a sua disposição um equipamento precário que produz algumas leituras incorretas. O equipamento não deveria produzir valores negativos, mas em um teste preliminar o Miguel percebeu que o equipamento está produzindo números negativos. A boa notícia é que todos os números não negativos produzidos pelo equipamento estão corretos. Projete uma função que elimine os valores incorretos de uma sequência de valores produzidas pelo equipamento.

@) Em um jogo de sobrevivência um personagem se move por um mundo aberto tridimensional formado por cubos do mesmo tamanho. Cada posição (cubo) do mapa tem uma coordenada $(X, Y, Z)$ e cada componente da coordenada pode assumir qualquer valor inteiro (o mapa é infinito!). O personagem pode se deslocar um cubo por vez, seja para o norte, sul, leste ou oeste ou para cima ou para baixo. Projete uma função que receba a posição do personagem e uma sequência de deslocamentos e calcule a nova posição do personagem.

@) O Pedro está com dificuldades em gerenciar os seus gastos e por isso fez uma acordo consigo mesmo: toda vez que a conta ficar negativa, ele fará uma doação de 10 reais para um entidade social. Ele tem anotado o saldo inicial da sua conta, e todos os gastos e recebimentos que teve em um período, os gastos com valores negativos e os recebimentos com valores positivos, agora ele precisa da sua ajuda para calcular quanto deve doar. Projete uma função para resolver o problema do Pedro.

@) Você acaba de ser contratado por um empresa que está desenvolvendo um sistema de gerenciamento de campeonatos amadores de futebol. A sua primeira tarefa é projetar uma função que calcule o desempenho de um time, que consiste no número de pontos, número de vitórias e saldo de gols (diferenças entre os gols feitos e sofridos) de um time a partir dos resultados das partidas que ele jogou. Cada vitória gera três pontos e cada empate um ponto. Por exemplo, se os resultados para um determinado time foram $5 \times 1$, $0 \times 2$ e $1 \times 1$, onde o primeiro número são os gols feitos e o segundo os gols sofridos, então o time fez 4 pontos, obteve 1 vitória e saldo de gols de 2.


<!-- Emboço de solução -->

@) A Láurea Acadêmica é uma homenagem prestada a alunos que tiveram elevado nível de aproveitamento no curso de graduação. Na UEM, todos os alunos que tiveram mais do que 2/3 das notas finais das disciplinas maiores do que 9,0 recebem esta homenagem. Projete um programa que receba as notas finais de um aluno e determine se ele receberá a Láurea Acadêmica.

@) Uma eleição é realizada com apenas dois candidatos. Cada eleitor pode votar ou no primeiro candidato, ou no segundo candidato, ou ainda, votar em branco. O candidato que tiver mais votos ganha a eleição. Se os votos em branco forem mais do que 50% do total de votos, novas eleições devem ser convocadas. Projete uma função que receba como entrada uma lista não vazia de votos e determine qual foi o resultado da eleição. Dica: projete uma função auxilar que conte votos de um tipo especificado por parâmetro.

@) O problema do menor retângulo delimitador consiste em determinar o retângulo de menor altura e menor largura que pode cobrir um conjunto de pontos no plano cartesiano. Projete uma função que resolva o problema do menor retângulo delimitador. Considere que o retângulo deve ter os lados paralelos aos eixos $x$ e $y$. Dica: faça alguns exemplos no papel!
