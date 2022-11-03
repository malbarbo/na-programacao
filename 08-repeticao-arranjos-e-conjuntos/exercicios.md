---
# vim: set spell spelllang=pt_br sw=4:
# TODO: adiconar mais exercícios
title: Repetição, arranjos e conjuntos
---


**Exercícios**

#. Projete uma função que some todos os valores de um arranjo de 7 números.

#. Projete uma função que encontre o valor máximo de um arranjo com 5 números.

#. Projete uma função que junte todas as string de um arranjo de 5 strings.

#. Projete uma função que verifique se um arranjo com 5 números inteiros tem mais números positivos ou negativos.

#. A Láurea Acadêmica é uma homenagem prestada a alunos que tiveram elevado nível de aproveitamento no curso de graduação. Na UEM, todos os alunos que tiveram mais do que 2/3 das notas finais das disciplinas maiores do que 9,0 recebem esta homenagem. Projete um programa que receba as notas finais de um aluno e determine se ele receberá a Láurea Acadêmica.

#. Uma eleição é realizada com apenas dois candidatos. Cada eleitor pode votar ou no primeiro candidato, ou no segundo candidato, ou ainda, votar em branco. O candidato que tiver mais votos ganha a eleição. Se os votos em branco forem mais do que 50% do total de votos, novas eleições devem ser convocadas. Projete uma função que receba como entrada uma lista não vazia de votos e determine qual foi o resultado da eleição. Dica: deseje uma função auxilar que conte votos de um tipo especificado por parâmetro.

#. O problema do menor retângulo delimitador consiste em determinar o retângulo de menor altura e menor largura que pode cobrir um conjunto de pontos no plano cartesiano. Projete uma função que resolva o problema do menor retângulo delimitador. Considere que o retângulo deve ter os lados paralelos aos eixos $x$ e $y$. Dica: faça alguns exemplos no papel!

#. O Miguel é doutorando em física e precisa coletar dados de um experimento, mas ele só tem a sua disposição um equipamento precário que produz algumas leituras incorretas. O equipamento não deveria produzir valores negativos, mas em um teste preliminar o Miguel percebeu que o equipamento está produzindo números negativos. A boa notícia é que todos os números não negativos produzidos pelo equipamento estão corretos. Projete uma função que elimine os valores incorretos de uma sequência de valores produzidas pelo equipamento.

#. Projete uma função que encontre o índice (posição) da primeira ocorrência do valor máximo de um arranjo dinâmico não vazio.

#. Projete uma função que encontre os índices de todas as ocorrências de um determinado nome em um arranjo dinâmico de nomes.

#. Projete uma função que receba como entrada um arranjo dinâmico de números em ordem não decrescente e um valor $n$ e devolva um novo arranjo dinâmico com os elementos do arranjo de entrada junto com $n$ em ordem não decrescente. Dica: faça dois "para cada", um após o outro, um para selecionar os menores que $n$ e outro para selecionar os maiores.

#. Ordenação por inserção é uma algoritmo para ordenar um arranjo de valores. A ideia do algoritmo é analisar cada elemento do arranjo de entrada e colocá-lo em ordem no arranjo de saída. Usando a função do exercício anterior, projete uma função que receba como entrada um arranjo dinâmico e devolva um novo arranjo dinâmico com os valores da entrada ordenados.

#. Projete uma função que receba como entrada um arranjo dinâmico de números e uma posição e devolva um novo arranjo sem o elemento da posição especificada.

#. Projete uma função que verifique se um arranjo de valores está em ordem não decrescente.

#. Projete uma função que receba como entrada um arranjo dinâmico de números, uma posição $i$ e um número $n$ e devolva um novo arranjo com $n$ adicionado na posição $i$ do arranjo de entrada.

#. Projete uma função que verifique se um arranjo de valores é palíndromo.

#. A escola do seu irmão mais novo está fazendo um coletânea de ditos populares. Cada aluno da escola escolheu um dito popular e a escola agregou todos eles em um arquivo texto (um dito por linha). Agora a escola precisa eliminar os ditos repetidos e classificá-los em ordem, mas ela não sabe como fazer isso. Você pode ajudar?

#. Projete uma função que separe as "partes" de uma string usando um espaço como delimitador.

#. Dizemos que um arranjo é dobrado se ele pode ser dividido ao meio e a primeira metade é igual a segunda metade. Projete uma função que verifique se um arranjo de número é dobrado.

#. Projete uma função `subarranjo` que funcione da mesma forma que a função `substr`, mas que receba como entrada um arranjo de número ao invés de uma string.

#. Em um jogo de sobrevivência um personagem se move por um mundo aberto tridimensional formado por cubos do mesmo tamanho. Cada posição (cubo) do mapa tem uma coordenada $(X, Y, Z)$ e cada componente da coordenada pode assumir qualquer valor inteiro (o mapa é infinito!). O personagem pode se deslocar um cubo por vez, seja para o norte, sul, leste ou oeste ou para cima ou para baixo. Projete uma função que receba a posição do personagem e uma sequência de deslocamentos e calcule a nova posição do personagem.

#. Rotacionar um arranjo $n$ posições a esquerda significa mover os primeiros $n$ elementos do arranjo para as últimas $n$ posições do arranjo. Por exemplo, rotacionar o arranjo `{5, 3, 4, 1, 7}`{.cpp} duas posições a esquerda produz o arranjo `{4, 1, 7, 5, 3}`{.cpp}. Projete uma função que rotacione um arranjo $n$ posições a esquerda.

#. Um número inteiro positivo $n$ é primo se ele tem exatamente dois divisores distintos, $1$ e $n$. Projete uma função que verifique se um número inteiro positivo é primo. Dica: Faça exemplos de código (sem repetição lógica) para verificar se alguns números específicos ($5$, $8$, $11$) são primos e tente generalizar o código com repetição lógica usando o "enquanto". Leia com cuidado a definição e faça o código mais simples e direto possível!

#. Um número inteiro positivo $n$ é perfeito se a soma dos seus divisores, exceto ele mesmo, é igual a $n$. Por exemplo, $6$ é perfeito pois os divisores de $6$ (exceto ele mesmo) são $1, 2$ e $3$ e a soma $1 + 2 + 3$ é igual a $6$. O número $28$ também é perfeito, verifique você mesmo! Projete uma função que verifique se um número inteiro positivo é perfeito. Use as mesmas dicas do exercício anterior.

<!--
#. Você acaba de ser contratado por um empresa que está desenvolvendo um sistema de gerenciamento de campeonatos amadores de futebol. A sua primeira tarefa é projetar uma função que calcule o saldo de gols de um time a partir dos resultados das partitas que ele jogou. O saldo de gols é a diferente entre os gols que o time fez e os gols que o time sofreu. Por exemplo, se os resultados para um determinado time foram $3 \times 1$, $0 \times 1$ e $5 \times 2$, onde o primeiro número são os gols feitos e o segundo os gols sofridos, então o saldo de gols é $4$.

#. O Pedro está com dificuldades em gerenciar os seus gastos e por isso fez uma acordo consigo mesmo: toda vez que a conta ficar negativa, ele fará uma doação de 10 reais para um entidade social. Ele tem anotado o saldo inicial da sua conta, e todos os gastos e recebimentos que teve em um período, os gastos com valores negativos e os recebimentos com valores positivos, agora ele precisa da sua ajuda para calcular quanto deve doar. Projete uma função para resolver o problema do Pedro.
-->
