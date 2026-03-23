---
# vim: set spell spelllang=pt_br:
title: |
       | Fundamentos de Algoritmos
       | Algoritmos e linguagens
urlcolor: Blue
---

# Começando

@) O que é um algoritmo?

@) Qual é a relação entre algoritmos e programas de computadores?

@) Podemos utilizar o português para programar? Explique.

@) O que é uma linguagem de programação?


# Praticando

@) Aja como um computador humano e execute o algoritmo (fluxograma) para calcular a raiz quadrada de 9.

@) Aja como um computador humano e execute o algoritmo (pseudocódigo) para calcular o MDC de 18 e 60.

@) Aja como um computador humano e execute o algoritmo (função matemática) para calcular a soma dos valores da lista $[6, 1, 4, 2]$.


# Avançando

@) Tente relacionar as construções do fluxograma do algoritmo que calcula a raiz quadrada com as construções do código em C++.

@) Tente relacionar as construções do pseudocódigo que calcula o MDC com as construções do código em Python.

@) Dois algoritmos podem resolver o mesmo problema de formas diferentes. Um critério para escolher entre eles é a simplicidade. Considere os dois algoritmos a seguir para verificar se um número natural é par.

    **Algoritmo A**: Divida o número por 2. Se o resto é 0, o número é par. Senão, o número é ímpar.

    **Algoritmo B**: Subtraia 2 do número repetidamente. Se chegar em 0, o número é par. Se chegar em 1, o número é ímpar.

    Qual dos dois algoritmos é mais simples? Por quê?


# Explorando

Os computadores utilizam internamente o sistema binário (base 2) para representar números. No sistema decimal usamos 10 dígitos (0 a 9) e cada posição representa uma potência de 10. Por exemplo, o número 352 representa $3 \times 10^2 + 5 \times 10^1 + 2 \times 10^0 = 300 + 50 + 2 = 352$. No sistema binário usamos apenas 2 dígitos (0 e 1) e cada posição representa uma potência de 2. Por exemplo, o número 1101 em binário representa $1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 = 8 + 4 + 0 + 1 = 13$.

O algoritmo a seguir converte um número natural positivo $N$ para a sua representação em binário:

Passo 1: Divida $N$ por 2 e anote o resto.

Passo 2: $N \leftarrow$ resultado da divisão inteira de $N$ por 2.

Passo 3: Se $N > 0$, repita o passo 1.

Passo 4: Leia os restos de baixo para cima.

Exemplo de execução para $N = 13$:

  Passo    $N$    $N \div 2$    Resto
  ------   ----   ----------    ------
  1        13     6             1
  2        6      3             0
  3        3      1             1
  4        1      0             1

Restos de baixo para cima: 1101. Portanto, 13 em decimal é 1101 em binário.

@) Aja como um computador humano e execute o algoritmo acima para converter o número 25 para binário.


# Desafio

@) Uma linguagem pode surgir a partir de processos naturais? O DNA é a linguagem mais complexa que conhecemos, qual é a sua origem?
