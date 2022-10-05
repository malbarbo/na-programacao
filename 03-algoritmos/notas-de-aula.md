---
# vim: set spell spelllang=pt_br:
title: Algoritmos
---

# Introdução

Fundamentos de Algoritmos \pause

- Resolver problemas projetando programas que sejam bem escritos e funcionem corretamente. \pause

O que são algoritmos e qual a relação deles com resolução de problemas e programas de computadores? \pause

O que é um algoritmo?


# Definições de algoritmo

Dicionário Silveira Bueno \pause

> Conjunto predeterminado e definido de regras e processos destinados à solução de um problema, com um número finito de etapas.


\pause

Dicionário Merriam-Webster \pause

> Um procedimento passo a passo para resolver um problema ou atingir um objetivo.

\pause

Forbellone e Eberspächer \pause

> Uma sequência de passos que visam atingir um objetivo bem definido.

\pause

Knuth

> Um conjunto finito de regras que fornece uma sequência de operações para resolver um tipo específico de problema.

O que estas definições tem em comum?


# Algoritmo

O que estas definições tem em comum?

- sequência de etapas/passos/operações \pause

- resolução de um problema \pause

Então, qual a relação de algoritmo e resolução de problemas? \pause

Processos de resolução de problemas podem ser descritos com algoritmos. \pause

Embora algoritmos possam ser usados em diversos contextos, estamos interessados nos algoritmos que podem ser executados por computadores.


# Algoritmos

Podemos descrever/representar um algoritmo de algumas maneiras, entre elas \pause

- Descrição textual

- Fluxograma

- Pseudocódigo

\pause

Vamos ver alguns exemplos!


# Descrição textual

Temos uma tabela com nomes de jogadores e os seus pontos em um determinado campeonato e queremos determinar a classificação dos jogadores. \pause Podemos criar um algoritmo que descreve uma forma de fazer isso? \pause Sim! \pause

Vamos fazer um algoritmo usando descrição textual. \pause

Nessa forma de representação de algoritmo, todas as instruções são dadas através de texto em linguagem natural.


# Descrição textual

<div class="columns">
<div class="column" width="50%">
Obtenha a tabela com os pontos.

Marque a linha 1 da tabela como linha de referência.

Olhando para a linha de referência e para as linhas que estão após ela, procure pela linha com o jogador com mais pontos e troque de lugar o conteúdo dessa linha com o conteúdo da linha de referência.

Se existe uma linha após a linha de referência, considere essa próxima linha como referência e repita o processo, senão pare.

No final, a tabela foi reorganizada de acordo com a classificação dos jogadores. \pause

</div>
<div class="column" width="25%">
**Entrada**

Jogador | Pontos
--------|-------
Paula   | 8
Jorge   | 10
Maria   | 7
José    | 6
Ana     | 9
Mário   | 8

\pause

</div>
<div class="column" width="25%">
**Saída**

Jogador | Pontos
--------|-------
Jorge   | 10
Ana     | 9
Paula   | 8
Mário   | 8
Maria   | 7
José    | 6

</div>
</div>


# Fluxograma

Temos um número positivo e um chute inicial para a raiz quadrado desse número, queremos, a partir do chute inicial, encontrar um valor aproximado para a raiz quadrado do número. \pause Podemos criar um algoritmo que descreve uma forma de fazer isso? \pause Sim! \pause

Vamos fazer um algoritmo usando fluxograma. \pause

Em um fluxograma, utilizamos símbolos para representar graficamente a sequência de ações do algoritmo.


# Fluxograma

<div class="columns">
<div class="column" width="50%">
**Método de Newton**

![](imagens/fluxograma.pdf)

\pause

</div>
<div class="column" width="25%">
**Entrada**

$N = 4$

$C = 1$

\pause

</div>
<div class="column" width="25%">
**Saída**

$2$
</div>
</div>


# Pseudocódigo

Temos dois números inteiros positivos e queremos encontrar o máximo divisor comum entre eles. \pause Podemos criar um algoritmo que descreve uma forma de fazer isso? \pause Sim! \pause

Vamos fazer um algoritmo em pseudocódigo. \pause

Pseudocódigo usa linguagem natural e geralmente é estruturado para parecer mais com código em uma linguagem de programação.


# Pseudocódigo

<div class="columns">
<div class="column" width="60%">
**Algoritmo de Euclides**

Passo 1:

- Obtenha os números inteiros positivos $A$ e $B$
- Se $A < B$, troque o valor de $A$ por $B$ e vice-versa

Passo 2:

- Se $B = 0$, então pare e a resposta é o valor de $A$
- Senão
    - $C \leftarrow A - B$
    - $A \leftarrow B$ // Copie o valor de $B$ para $A$
    - $B \leftarrow C$ // Copie o valor de $C$ para $B$
    - Se $A < B$, troque o valor de $A$ por $B$ e vice-versa
    - Repita o passo 2

\pause

</div>
<div class="column" width="20%">
**Entrada**

$A = 52$

$B = 36$

\pause

</div>
<div class="column" width="20%">
**Saída**

$4$
</div>
</div>


# Algoritmos

<div class="columns">
<div class="column" width="50%">

O que todos esses algoritmos têm em comum? \pause

- Entrada e saída \pause

- Ações (processamento) \pause

    - Cálculo de valores \pause

    - Escolha entre ações \pause

    - Repetição de ações \pause

- Uso de memória (leitura e armazenamento de valores) \pause
</div>
<div class="column" width="50%">
![](imagens/arq.pdf)
</div>
</div>


# Limite dos algoritmos

Todos os problemas podem ser resolvidos com algoritmos? \pause

O que é um problema? \pause

Vamos considerar apenas problemas bem definidos, que especificam com precisão quais são as possíveis entradas e como as saídas estão relacionados com as entradas. \pause

Todos os problemas bem especificados podem ser resolvidos com algoritmos? \pause

O que significa dizer que um algoritmo resolve um problema? \pause Que para todas as entradas possíveis, o algoritmo produz a saída correta. \pause

E então, todos os problemas bem especificados podem ser resolvidos com algoritmos? \pause Não... \pause

Os problemas que podem ser resolvidos com algoritmos são chamados de problemas computáveis.


# Avaliação de algoritmos

Pode existir mais que um algoritmo que resolve o mesmo problema? \pause Sim. \pause

O que considerar na escolha ou no projeto de algoritmos? \pause

- Simplicidade \pause

- Uso de recursos (tempo de processamento, memória, energia, etc) \pause

- Corretude


# Algoritmos e computadores

Qual representação utilizar para escrever algoritmos que possam ser executados por um computador? \pause

Vamos discutir esta questão em seguida!


# Atividades

@. Aja como um computador humano e execute o algoritmo (fluxograma) para calcular a raiz quadrado de 8 com chute inicial 1.

@. Aja como um computador humano e execute o algoritmo (pseudocódigo) para calcular o mdc de 48 e 15.
