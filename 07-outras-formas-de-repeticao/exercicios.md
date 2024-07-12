---
# vim: set spell spelllang=pt_br sw=4:
title: |
       | Fundamentos de Algoritmos
       | Outras formas de repetição
urlcolor: Blue
# TODO: fazer exercícios mais interessantes (reais).
# TODO: adicionar exercícios de avaliação de expressões e execução passo a passo?
---

**\color{red}Lembre-se** de seguir o processo de projeto de funções e de usar o `mypy` e o `doctest` na etapa de verificação.

# Começando


# Praticando

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
