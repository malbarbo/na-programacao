---
# vim: set spell spelllang=pt_br:
title: Linguagens de programação
---

# Introdução

Como descrever o que um computador deve fazer? \pause

Usando uma linguagem. \pause

Mas o que é uma linguagem e qual a sua função? \pause

Um sistema estruturado para comunicação.


# Introdução

Podemos utilizar o português para programar um computador? \pause Não, porque o computador não entende o português! \pause Ainda que o computador entendesse o português, ele não seria uma linguagem adequada para programação porque não é preciso o bastante. \pause

E que linguagem o computador entende? \pause Cada tipo de computador entende um linguagem específica, a sua linguagem de máquina. \pause

Então, precisamos programar o computador usando a linguagem de máquina? \pause Hoje em dia não, mas os primeiros computadores eram programados usando linguagem de máquina!

# {.plain}

![](imagens/eniac.jpeg)


# Linguagem de programação

Se não queremos utilizar linguagem de máquina, como podemos programar os computadores? \pause Como duas entidades que falam linguagens diferentes podem se comunicar? \pause Usando um tradutor.\pause

Se a linguagem fonte e a linguagem alvo forem bem definidas, podemos escrever um programa que faça a tradução de forma automática. \pause A linguagem de máquina (alvo) é bem definida, precisamos de uma linguagem fonte que também seja bem definida.


# Sintaxe e semântica

Uma linguagem de programação é uma linguagem formal (bem definida) adequada para programar computadores. \pause

Uma linguagem de programação é caracterizada por diversos aspectos, entre eles

- A sintaxe e a semântica
- Nível de abstração
- Modo de execução


# Sintaxe e semântica

A **sintaxe** de uma linguagem é o conjunto de regras que define como os símbolos podem ser agrupados para criar as sentenças na linguagem. \pause

Operação de soma com dois número: \pause

- Na maioria das linguagens: `20 + 17` \pause
- No Lisp: `(+ 20 17)`


# Sintaxe e semântica

A **semântica** de uma linguagem define o significado das construções da linguagem. \pause

A expressão `12 + "3"` é valida sintaticamente em muitas linguagens, mas o significado é diferente entre elas \pause

- Lua: significa que o texto "3" deve ser convertido para um número e depois somado com 12. \pause
- Javascrip: significa que o número 12 deve ser transformado para um texto e depois juntado com "3". \pause
- Na maioria linguagens: é um erro semântico.


# Nível de abstração

Uma linguagem de programação pode requerer (ou permitir) que o programador controle com mais detalhes ou menos detalhes o computador. Quanto mais detalhes são necessários, mais baixo nível é a linguagem, quanto menos detalhes, mais alto nível. \pause


_A programming language is low level when its programs require attention to the irrelevant_. (Alan Perlis) \pause

Ser relevante ou não depende do contexto, por exemplo, para sistemas embarcados, controlar com detalhes o uso da memória pode ser bastante relevante, já para um _script_ que será executado em um computador de trabalho, nem tanto.


# Modo de execução

Uma linguagem de programação pode ser compilada ou interpretada. \pause

Em uma linguagem compilada o código do programa é primeiro traduzido (compilado) para código de máquina e posteriormente executado. \pause

Em uma linguagem interpretada o código do programa é lido e executado diretamente pelo interpretador.


# Compilação vs interpretação

Características de programas compilados \pause

- Execução eficiente

- Ciclo de desenvolvimento lento (tem que esperar o compilador) \pause


Características de programas interpretados \pause

- Execução menos eficiente

- Ciclo de desenvolvimento mais rápido (não precisa esperar o compilador)


# Exemplo C++

<div class="columns">
<div class="column" width="50%">

Exemplo em C++ - Raiz quadrada

Parte do arquivo `raiz.cpp`

\small

```cpp
// Entrada
double n = stof(argv[1]);
double c = stof(argv[2]);

// Processamento
while (abs(c * c - n) >= 0.1) {
    double c_ = (c + n / c) / 2;
    c = c_;
}

// Saída
cout << c << endl;
```

\pause
</div>
<div class="column" width="50%">
\small

**Windows**

Compilação

```
g++ -o raiz.exe raiz.cpp
```

\pause


Execução

```
> raiz.exe 4 1
2.00061
```


**Linux**

Compilação

```
g++ -o raiz raiz.cpp
```

\pause


Execução

```
> ./raiz 4 1
2.00061
```
</div>
</div>


# Exemplo Python

<div class="columns">
<div class="column" width="50%">

Exemplo em Python - MDC

Parte do arquivo `mdc.py`

\footnotesize

```python
# Entrada
a = int(sys.argv[1])
b = int(sys.argv[2])
# Processamento
if a < b:
    a, b = b, a
while b != 0:
    c = a - b
    a = b
    b = c
    if a < b:
        a, b = b, a
# Saída
print(a)
```

\pause
</div>
<div class="column" width="50%">
Interpretação

```
> python3 mdc.py 52 36
4
```

</div>
</div>


# Linguagens

Existem centenas de linguagens de programação, cada uma com sua próprias características e usos, então, qual delas aprender? \pause

Nenhuma em particular. \pause O mais importante não são as linguagens em si, mas os princípios que são utilizados para criar os programas nas linguagens. \pause

Dominando os fundamentos de algoritmos e paradigmas de programação, aprender uma nova linguagem não é uma tarefa difícil!


# Linguagens

Mas precisamos de uma linguagem para começar. \pause Nessa disciplina vamos utilizar a linguagem C++! \pause

C++ é uma das linguagens mais poderosas que existem, \pause mas também uma das mais complicas! \pause Mas não se preocupe, vamos utilizar apenas construções básicas! \pause

Vamos começar?


# Atividades

@. Tente relacionar construções do fluxograma do algoritmo que calcula a raiz quadrada com construções do código em C++.

@. Tente relacionar construções do pseudo código que calcula o MDC com construções do código em Python.
