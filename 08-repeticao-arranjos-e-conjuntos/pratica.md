---
# vim: set spell spelllang=pt_br sw=4:
title: Repetição, arranjos e conjuntos - Prática
---

<!-- Básico -->

@. Projete uma função que concatene todos os elementos de uma lista de strings.

@. Projete uma função que crie uma lista de números a partir de uma lista de strings convertendo cada string para um número. Assuma que todas as strings representam números válidos.

@. Projete uma função que crie uma nova lista somando um valor $x$ especificado a cada elemento de uma lista de inteiros.

@. Projete uma função que calcule o produto de todos os elementos de uma lista de inteiros.


<!-- Seleção -->

@. Projete uma função que verifique se a quantidade de elementos de uma lista de floats é menor que 4.

@. Projete uma função que verifique se todos os elementos de uma lista de inteiros são menores que 10.

@. Projete uma função que verifique se todos os elementos de uma lista de booleanos são falsos.

@. Projete uma função que verifique se algum dos elementos de uma lista de booleanos é verdadeiro.

@. Projete uma função que crie uma nova lista removendo todas os valores nulos de uma lista de inteiros.


<!-- Esboço e calculo de mais de um valor-->

@. Projete uma função que conte quantas vezes o valor mínimo de uma lista de inteiros não vazia aparece na lista.

    a) Esboce uma solução em duas etapas e depois implemente a função.

    a) Faça uma implementação alternativa que use apenas uma repetição.

    a) Avalie qual das implementações é mais simples.

@. Projete uma função que calcule a amplitude dos valores de uma lista não vazia de números, isto é, a diferença entre o maior e menor valor da lista.

    a) Esboce uma solução em três etapas e depois implemente a função.

    a) Faça uma implementação alternativa que use apenas uma repetição.

    a) Avalie qual das implementações é mais simples.

@. Projete uma função que indique se uma lista de inteiros tem mais valores positivos ou negativos.

@. Projete uma função que receba como entrada uma lista `lst` de números e crie uma nova lista colocando os valores negativos de `lst` antes dos positivos.


<!-- Indíce e range -->

@. Projete uma função que encontre as posições de todas as ocorrências de um nome em uma lista de nomes.

@. Projete uma função que receba como entrada uma lista de números e uma posição e devolva uma nova lista sem o elemento da posição especificada.

    a) Esboce uma solução em duas etapas e depois implemente a função (não use operações de sublista).

    a) Faça uma implementação alternativa que use apenas uma repetição (não use operações de sublista).

    a) Faça uma implementação que use operações de sublista e não use repetição.

    a) Avalia e classifique as implementações em ordem de simplicidade.

@. Projete uma função que receba como entrada uma lista de números, uma posição $i$ e um número $n$ e devolva uma nova lista com $n$ adicionado na posição $i$ da lista de entrada.

    a) Esboce uma solução em três etapas e depois implemente a função (não use operações de sublista).

    a) Faça uma implementação alternativa que use apenas uma repetição (não use operações de sublista).

    a) Faça uma implementação que use operações de sublista e não use repetição.

    a) Avalia e classifique as implementações em ordem de simples.


<!-- Enquanto e generalização a partir de repetição física de código -->

@. Revise as funções dos exercícios anteriores e verifique quais podem ser implementadas utilizando o "enquanto" para deixar o código mais eficiente ou simples. Faça a implementação dessas funções usando o "enquanto".

@. Projete uma função que verifique se uma lista de número é dobrada, isto é, pode ser obtida pela concatenação de duas listas iguais (não use operações de sublista).

@. Projete uma função que determine qual é a menor quantidade de elementos de uma lista que precisam ser somados (a partir do início da lista) para que a soma seja maior que um dado valor. Se não for possível atingir a soma desejada, a função deve devolver -1.


<!-- Repetição sem listas -->

@. Um número inteiro positivo $n$ é primo se ele tem exatamente dois divisores distintos, $1$ e $n$. Projete uma função que verifique se um número inteiro positivo é primo. Dica: Faça exemplos de código (sem repetição lógica) para verificar se alguns números específicos ($5$, $8$, $11$) são primos e tente generalizar o código com repetição lógica usando o "enquanto".

@. Defina uma função que receba como parâmetro um valor $n$ e calcule o valor aproximado de $\pi$ usando os primeiros $n$ termos da série

   $$\pi = 4 \sum_{k=0}^{\infty} \frac{(-1)^k}{2 k + 1}
       = 4 \left ( \frac{1}{1} - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \cdots  \right)$$


<!-- Outros -->

@. Projete uma função que junte todos os elementos de uma lista de strings (não vazias) separando-os com `','`{.python} ou/e `'e'`{.python}, de acordo com a gramática do Português.
