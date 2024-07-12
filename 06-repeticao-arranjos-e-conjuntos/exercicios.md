---
# vim: set spell spelllang=pt_br sw=4:
title: |
       | Fundamentos de Algoritmos
       | Repetição, arranjos e conjuntos
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

@) Quais são as três perguntas que precisamos responder quando estamos implementando uma função utilizando a abordagem incremental?


# Praticando

<!-- Básico -->

@) Projete uma função que concatene todos os elementos de uma lista de strings.

@) Projete uma função que crie uma lista de números a partir de uma lista de strings convertendo cada string para um número. Assuma que todas as strings representam números válidos.

@) Projete uma função que crie uma nova lista somando um valor $x$ especificado a cada elemento de uma lista de inteiros.

@) Projete uma função que calcule o produto de todos os elementos de uma lista de inteiros.


<!-- Seleção -->

@) Projete uma função que verifique se a quantidade de elementos de uma lista de floats é menor que 4.

@) Projete uma função que verifique se todos os elementos de uma lista de inteiros são menores que 10.

@) Projete uma função que verifique se todos os elementos de uma lista de booleanos são falsos.

@) Projete uma função que verifique se algum dos elementos de uma lista de booleanos é verdadeiro.

@) Projete uma função que crie uma nova lista removendo todas os valores nulos de uma lista de inteiros.


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

@) Projete uma função que receba como entrada uma lista `lst` de números e crie uma nova lista colocando os valores negativos de `lst` antes dos positivos.


<!-- Indíce e range -->

@) Projete uma função que encontre as posições de todas as ocorrências de um nome em uma lista de nomes.

@) Projete uma função que receba como entrada uma lista de números e uma posição e devolva uma nova lista sem o elemento da posição especificada.

    a) Esboce uma solução em duas etapas e depois implemente a função (não use operações de sublista).

    a) Faça uma implementação alternativa que use apenas uma repetição (não use operações de sublista).

    a) Faça uma implementação que use operações de sublista e não use repetição.

    a) Avalia e classifique as implementações em ordem de simplicidade.

@) Projete uma função que receba como entrada uma lista de números, uma posição $i$ e um número $n$ e devolva uma nova lista com $n$ adicionado na posição $i$ da lista de entrada.

    a) Esboce uma solução em três etapas e depois implemente a função (não use operações de sublista).

    a) Faça uma implementação alternativa que use apenas uma repetição (não use operações de sublista).

    a) Faça uma implementação que use operações de sublista e não use repetição.

    a) Avalia e classifique as implementações em ordem de simples.


<!-- Enquanto e generalização a partir de repetição física de código -->

@) Revise as funções dos exercícios anteriores e verifique quais podem ser implementadas utilizando o "enquanto" para deixar o código mais eficiente ou simples. Faça a implementação dessas funções usando o "enquanto".

@) Projete uma função que verifique se uma lista de número é dobrada, isto é, pode ser obtida pela concatenação de duas listas iguais (não use operações de sublista).

@) Projete uma função que determine qual é a menor quantidade de elementos de uma lista que precisam ser somados (a partir do início da lista) para que a soma seja maior que um dado valor. Se não for possível atingir a soma desejada, a função deve devolver -1.


<!-- Repetição sem listas -->

@) A sequência de Fibonacci começa com 1, 1, e cada número seguinte é obtido pela soma dos dois anteiros, dessa forma a sequência é 1, 1, 2, 3, 5, 8, 13, 21, ... Projete uma função que receba como parâmetro um número natural $n > 0$ e determine o $n$-ésimo número da sequência de Fibonacci.

@) Defina uma função que receba como parâmetro um valor $n$ e calcule o valor aproximado de $\pi$ usando os primeiros $n$ termos da série

   $$\pi = 4 \sum_{k=0}^{\infty} \frac{(-1)^k}{2 k + 1}
       = 4 \left ( \frac{1}{1} - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \cdots  \right)$$


<!-- Outros -->

@) Projete uma função que junte todos os elementos de uma lista de strings (não vazias) separando-os com `','`{.python} ou/e `'e'`{.python}, de acordo com a gramática do Português.

@) Projete uma função que receba um número inteiro positivo $n$, e crie a matriz identidade $I_n$, com $n$ linhas e $n$ colunas, com todos os elementos da diagonal principal (elementos com o mesmo índice) iguais a 1 e os demais elementos iguais a 0.

@) Projete uma função que encontre os índices de todas as linhas de uma matriz cuja a soma dos elementos é zero.

@) Projete uma função que encontre os índices de todas as colunas de uma matriz cuja a soma dos elementos é zero.

@) Projete uma função que verifique se uma matriz $A$ é simétrica, isto é, para cada elemento $a_{ij}$ da matriz, $a_{ij} = a_{ji}$.


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


<!-- Enquanto e generalização -->

@) Um número inteiro positivo $n$ é perfeito se a soma dos seus divisores, exceto ele mesmo, é igual a $n$. Por exemplo, $6$ é perfeito pois os divisores de $6$ (exceto ele mesmo) são $1, 2$ e $3$ e a soma $1 + 2 + 3$ é igual a $6$. O número $28$ também é perfeito, verifique você mesmo! Projete uma função que verifique se um número inteiro positivo é perfeito.

@) A empresa que você trabalha sofreu um falta de energia e agora é preciso recuperar os dados do backup. O primeiro passo é determinar o código dos clientes afetados. Em um primeiro momento foi obtido um arquivo (string) com o código de todos os clientes separados por vírgula. O seu trabalho agora é projetar uma função que gere uma lista dos códigos a partir dessa string. Por exemplo, para a string `"512,12,145"`{.python} a sua função deve gerar como resposta a lista `[512, 12, 145]`{.python}. Dica: você pode usar a expressão `c in s`{.python} para verificar se a string `c` está em `s` e o método `s.index(c)`{.python} para encontrar o índice da primeira ocorrência da string `c` em `s`.

@) Em um determinado jogo de construção de itens, cada item tem uma classe que varia de 1 a 10. Os item de classe 1 surgem conforme o jogador explorar os baús. Um item de classe 2 ou superior precisa ser construídos unindo dois itens da classe anterior. Por exemplo, para construir um item de classe 2 é necessário unir dois item de classe 1. Para construir um item de classe 10 é necessário unir dois item de classe 9. Projete uma função que receba como entrada um número $n$ (de 1 a 10), e determine quantos itens de classe 1 são necessário para construir um item de classe $n$. Suponha que a únicas operações aritméticas disponíveis seja a soma e a multiplicação.



<!-- Para cada no intervalo -->

<!--
@) Projete uma função que receba como entrada uma lista de números em ordem não decrescente e um valor $n$ e devolva uma nova lista com os elementos da lista de entrada junto com $n$ em ordem não decrescente.

@) Ordenação por inserção é uma algoritmo para ordenar uma lista de valores. A ideia do algoritmo é analisar cada elemento da lista de entrada e colocá-lo em ordem na lista de saída. Usando a função do exercício anterior, projete uma função que receba como entrada uma lista e devolva uma nova lista com os valores da entrada em ordem não decrescente.

@) A escola do seu irmão mais novo está fazendo um coletânea de ditos populares. Cada aluno da escola escolheu um dito popular e a escola agregou todos eles em um arquivo texto (um dito por linha). Agora a escola precisa eliminar os ditos repetidos e classificá-los em ordem, mas ela não sabe como fazer isso. Você pode ajudar?

@) Rotacionar um arranjo $n$ posições a esquerda significa mover os primeiros $n$ elementos do arranjo para as últimas $n$ posições do arranjo. Por exemplo, rotacionar o arranjo `{5, 3, 4, 1, 7}`{.cpp} duas posições a esquerda produz o arranjo `{4, 1, 7, 5, 3}`{.cpp}. Projete uma função que rotacione um arranjo $n$ posições a esquerda.

@) Projete uma função que separe as "partes" de uma string usando um espaço como delimitador.

-->
