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

## Dicionário Silveira Bueno

> Conjunto predeterminado e definido de regras e processos destinados à solução de um problema, com um número finito de etapas.

\pause

## Dicionário Merriam-Webster

> Um procedimento passo a passo para resolver um problema ou atingir um objetivo.

\pause

## Forbellone e Eberspächer

> Uma sequência de passos que visam atingir um objetivo bem definido.

\pause

## Knuth

> Um conjunto finito de regras que fornece uma sequência de operações para resolver um tipo específico de problema.

\pause

O que estas definições tem em comum?


# Definição de Algoritmo

O que estas definições tem em comum? \pause

- Sequência de etapas/passos/operações \pause

- Resolução de um problema \pause

Então, qual a relação de algoritmo e resolução de problemas e programas de computadores? \pause

- Processos de resolução de problemas podem ser descritos com algoritmos. \pause

E a relação com programas de computadores? \pause

- Algoritmos podem ser implementados como programas de computadores (embora algoritmos possam ser usados em diversos contextos, estamos interessados apenas naqueles que podem ser executados por computadores)


# Algoritmos

Como expressar um algoritmo? \pause

- Descrição textual

- Fluxograma

- Pseudocódigo

- Funções matemáticas

- Etc

\pause

Vamos fazer uma dinâmica!


# Dinâmica

Quatro equipes, cada equipe recebe um algoritmo e deve fazer \pause

- Leitura do algoritmo \pause

- Tentativa de execução do algoritmo \pause

- Descoberta do propósito do algoritmo \pause

- Apresentação para a turma


# Algoritmo 1 - Descrição textual

Considere a tabela ao lado.

<div class="columns">
<div class="column" width="50%">
Marque a linha 1 da tabela como linha de referência.

Olhando para a linha de referência e para as linhas que estão após ela, procure pela linha com a coluna **B** com maior valor e troque de lugar o conteúdo dessa linha com o conteúdo da linha de referência.

Se existe uma linha após a linha de referência, considere essa próxima linha como referência e repita o processo, senão pare.
</div>

<div class="column" width="50%">
_     |A       | B
------|--------|-------
**1** |Paula   | 8
**2** |Jorge   | 10
**3** |Maria   | 7
**4** |José    | 6
**5** |Ana     | 9
**6** |Mário   | 8

</div>
</div>


# Algoritmo 2 - Fluxograma

Usando $N = 4$ e $C = 1$, faça

![](imagens/fluxograma.pdf){width=7cm}


# Algoritmo 3 - Pseudocódigo

Passo 0:

- Começa com $A = 52$ e $B = 36$

Passo 1:

- Se $A < B$, troque o valor de $A$ por $B$ e vice-versa

Passo 2:

- Se $B = 0$, então pare e a saída é o valor de $A$
- Senão
    - $C \leftarrow A - B$
    - $A \leftarrow B$
    - $B \leftarrow C$
    - Repita o passo 1


# Algoritmo 4 - Função matemática

Calcule o valor de $f([2, 1, 4, 1, 2])$

$$f(x) = \begin{cases}
primeiro(x) & \text{se } num\_itens(x) = 1 \\
primeiro(x) + f(sem\_primeiro(x)) & \text{caso contrário}
\end{cases}$$


# Algoritmos

O que foi necessário para entender/executar esses algoritmos? \pause

- Entender a notação \pause

- Entender a semântica \pause

- Entender o modelo de execução


# Algoritmos

<div class="columns">
<div class="column" width="50%">
O que esses algoritmos têm em comum? \pause

- Entrada e saída \pause

- Ações (processamento) \pause

    - Cálculo de valores \pause

    - Escolha entre ações \pause

    - Repetição de ações \pause

- Uso de memória \pause
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

- Corretude e/ou precisão


# Algoritmos e computadores

Qual representação utilizar para escrever algoritmos que possam ser executados por um computador? \pause

Vamos discutir esta questão em seguida!



# Atividades

@. Aja como um computador humano e execute o algoritmo (fluxograma) para calcular a raiz quadrado de 8 com chute inicial 1.

@. Aja como um computador humano e execute o algoritmo (pseudocódigo) para calcular o mdc de 48 e 15.
