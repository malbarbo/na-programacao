---
# vim: set spell spelllang=pt_br:
title: Conceitos básicos
---

# Introdução

Até o momento nós estudamos alguns aspectos de

- Sistemas computacionais
- Algoritmos
- Linguagens de programação

\pause

Agora vamos ver as construções básicas da linguagem Python, para em seguida começarmos a estudar o processo de projeto de programas.


# Instalação

O Python é um software livre e pode ser baixado e instalado de <https://python.org>. \pause

Além do interpretador, a instalação padrão do Python vem com um ambiente de desenvolvimento e aprendizagem chamado IDLE. \pause

Ao iniciar o IDLE a janela a seguir é exibida \pause

![](imagens/idle.png){width=10cm}


# Janela de interações (REPL)

Utilizamos essa janela, chamada de janela de **interações** (ou REPL), para testar pequenos trechos de código. \pause

O símbolo `>>>` é chamado de _prompt_ e indica que o interpretador está pronto.


# Janela de interações (REPL)

As interações acontecem da seguinte forma

- Digitamos um trecho de código (_Read_)
- O código é avaliado (_Eval_)
- O resultado é mostrado na tela (_Print_)
- O processo se repete (_Loop_)

\pause

Exemplo de interação

```python
>>> 3 * 4
12
```


# Janela de interações (REPL)

O modo de interações também pode ser iniciado executado `python` no terminal de comandos. \pause

![](imagens/python-terminal.png){width=10cm}


# Observação

Note que na janela de interações não criamos programas para seres utilizados por usuários, mas experimentamos aspectos do Python e testamos os nossos programas. \pause

Veremos posteriormente como criar programas completos. \pause

Agora vamos explorar o Python!


# Tipos de dados e operações pré-definidas

A primeira coisa que aprendemos de uma linguagem de programação são os tipos de valores (tipos de dados) e operações já disponíveis na linguagem. \pause

Os primeiros computadores foram criados para fazerem cálculos matemáticos, então vamos começar com isso.


# Números

Python tem diversos tipos de números, os dois principais que vamos utilizar são \pause

<div class="columns">
<div class="column" width="50%">

Inteiros (`int`{.python}) \pause

```python
>>> 102
102
>>> -18
-18
```

\pause

</div>
<div class="column" width="50%">

Ponto flutuante (`float`{.python}), representação aproximada de números reais \pause

```python
>>> 1.3
1.3
>>> 0.345
0.345
>>> # Notação científica
>>> # 1.23 * 10^2
>>> 1.23e2
123.0
```

</div>
</div>


# Operações básicas

Podemos usar as quatro operações aritméticas básicas com esses tipos numéricos e algumas outras operações, conforme veremos a seguir.


# Operações básicas

<div class="columns">
<div class="column" width="50%">

```python
>>> # Soma e subtração
>>> 4 + 2
6
>>> 4 + 2.0 - 5
1.0
```

\pause

```python
>>> # Multiplicação e divisão
>>> 3 * 5.0
15.0
>>> 7 / 2
3.5
```

\pause

```python
>>> # Divisão sempre produz float
>>> 8 / 4
2.0
```
</div>
<div class="column" width="50%">
\pause

```python
>>> # Piso da divisão
>>> 7 // 2
3
>>> 5 // 1.3
3.0
```

\pause

```python
>>> # Resto da divisão
>>> 14 % 3
2
>>> # float é uma aproximação
>>> # de números reais
>>> 5 % 1.3
1.0999999999999999
```

</div>
</div>


# Comentários

O símbolo `#`{.python} (cerquilha), é utilizado para indicar um comentário. O comentário incia em `#`{.python} e vai até o final da linha. Os comentários são ignorados pelo interpretador do Python, mas são utilizados para adicionar informações relevantes para os leitores do código.


# Exponenciação

```python
>>> # Exponenciação e radiciação
>>> 3 ** 4
81
>>> 2 ** 80
1208925819614629174706176
>>> 16 ** 0.5
4.0
```

\pause

```python
>>> # A exponenciação tem prioridade sobre a divisão
>>> 27 ** 1/3
9.0
>>> # Usamos parênteses para mudar a prioridade
>>> 27 ** (1/3)
3.0
```


# Prioridades

O Python utiliza a mesma precedência que estamos acostumados na matemática. Podemos usar o acrônimo PEMDAS para lembrar das prioridades

- **P**arênteses
- **E**xponenciação
- **M**ultiplicação e **D**ivisão
- **A**dição e **S**ubtração

Operadores com a mesma precedência são avaliados da esquerda para a direita, exceto a exponenciação, que é da direita para a esquerda.


# Exercício

Qual é o resultado de cada expressão a seguir?

\small

```python
>>> 15 // 7

>>> 15 % 7

>>> 12 // 27

>>> 12 % 27

>>> 3 * 4 - 5 / (8 // 3)

>>> 5 * 8 // 3 / 4 % 3

>>> 2 ** 2 ** 3 // 4 * 3

```


# Exercício

Qual é o resultado de cada expressão a seguir?

\small

```python
>>> 15 // 7
2
>>> 15 % 7
1
>>> 12 // 27
0
>>> 12 % 27
12
>>> 3 * 4 - 5 / (8 // 3)
9.5
>>> 5 * 8 // 3 / 4 % 3
0.25
>>> 2 ** 2 ** 3 // 4 * 3
192
```


# Conversão

<div class="columns">
<div class="column" width="50%">

```python
>>> # Arredondamento
>>> round(3.4)
3
>>> round(3.5)
4
>>> round(3.5134, 2)
3.51
```

\pause

</div>
<div class="column" width="50%">

```python
>>> # Conversão entre int e float
>>> int(7.6)
7
>>> int(-2.3)
-2
>>> float(4)
4.0
```

</div>
</div>


# Módulos

As operações que vimos até agora estão disponíveis automaticamente, outras operações estão disponíveis em módulos, que devem ser importados antes de poderem ser utilizados. \pause

O Python tem uma [extensa](https://xkcd.com/353/) biblioteca padrão, com muitos módulos, este é um dos motivos que a linguagem é bastante utilizada. A documentação da biblioteca padrão do Python está disponível em <https://docs.python.org/3/library/index.html>. \pause

Por hora, vamos ver apenas algumas funções do módulo [`math`](https://docs.python.org/3/library/math.html).


# Piso e teto

<div class="columns">
<div class="column" width="50%">

```python
>>> import math
>>> # Piso
>>> # maior inteiro <= ao número
>>> math.floor(4.2)
4
>>> math.floor(-2.3)
-3
```

\pause

</div>
<div class="column" width="50%">

```python
>>> # Teto
>>> # menor inteiro >= ao númeo
>>> math.ceil(4.2)
5
>>> math.ceil(-2.3)
-2
```

</div>
</div>


# Cadeia de caracteres

Outro tipo de dado pré-definido em Python é a cadeia de caracteres (`str`{.python}) -- _string_ em inglês. \pause

Geralmente usamos strings para armazenar informações simbólicas, como por exemplo palavras e textos. \pause

Uma string em Python é escrita entre apóstrofo ou aspas \pause

```python
>>> 'casa'
'casa'
>>> "gota d'agua"
"gota d'agua"
>>> "mesa"
'mesa'
```


# Operações com strings

Assim como existem operações pré-definidas para números, também existem operações pré-definidas para strings. \pause

<div class="columns">
<div class="column" width="50%">

```python
>>> # Concatenação
>>> 'casa' + ' da ' + 'sogra'
'casa da sogra'
```

\pause

```python
>>> # Repetição
>>> 'abc' * 3
'abcabcabc'
```

\pause

```python
>>> 'algum' * 0
''
>>> 'algum' * -4
''
```

\pause

</div>
<div class="column" width="50%">

```python
>>> # Quantidade de caracteres
>>> len('ciência da computação')
21
```

\pause

```python
>>> # Conversão maiúscula
>>> 'José'.upper() # ou str.upper('José')
'JOSÉ'
>>> # Conversão minúscula
>>> 'José'.lower() # ou str.lower('José')
'josé'
```

</div>
</div>


# Substrings

```python
>>> # Indexação de caractere
>>> # O primeiro caractere tem índice 0
>>> 'casa'[0] # ou str.__getitem__('casa', 0)
'c'
```

\pause

```python
>>> 'casa'[1]
'a'
```

\pause

```python
>>> # Acesso de índice fora do intervalo
>>> 'casa'[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```


# Substrings

```python
>>> # Substring do início até 3 - 1
>>> 'veja isso'[:3] # ou str.__getitem__('veja isso', slice(None, 3))
'vej'
```

\pause

```python
>>> # Substring de 4 até o final
>>> 'veja isso'[4:] # ou str.__getitem__('veja isso', slice(4, None))
' isso'
```

\pause

```python
>>> # Substring de 2 até 6 - 1
>>> 'veja isso'[2:6] # ou str.__getitem__('veja isso', slice(7, 9))
'ja i'
```


# Conversão entre strings e números

<div class="columns">
<div class="column" width="50%">

```python
>>> # Conversão de int para str
>>> str(127)
'127'
>>> # Conversão de float para str
>>> str(4.1)
'4.1'
```

\pause

```python
>>> # Concatenação de str e int
>>> 'Idade: ' + str(19)
'Idade: 19'
```

\pause

</div>
<div class="column" width="50%">

```python
>>> # Conversão de str para int
>>> int('127')
127
```

\pause

```python
>>> # Conversão de str para float
>>> float('25')
25.0
>>> float('12.67')
12.67
```

</div>
</div>


# Formas de expressões

Inicialmente as expressões (cálculos) que vimos usavam apenas operadores matemáticos \pause

```python
30 * 2
```

\pause

Depois vimos que as expressões podem conter chamadas de funções \pause

```python
round(3.5)
```

\pause

e chamadas de métodos

```python
'José'.lower()
```

\pause

Por fim, vimos que strings podem ser indexadas \pause

```python
'veja isso'[2:6]
```


# Formas de expressões

Embora a forma de utilizar operadores, funções, métodos e indexação seja diferente, o propósito dessas construções é o mesmo: computar valores de saída a partir de valores de entrada.


# Formas de expressões

<div class="columns">
<div class="column" width="50%">
![](imagens/operacoes-entrada-saida.pdf){width=6cm}
\pause
</div>
<div class="column" width="50%">
\small
Se o propósito é o mesmo, por que não usar a mesma forma? \pause

Por conveniência! \pause

Por exemplo, se não tivéssemos a forma de operadores e apenas a forma de chamada de funções, então deveríamos escrever

```python
from operator import add, mull
add(mul(30, 2), 3)
```

ao invés de `30 * 2 + 3`{.python}, o que seria inconveniente. \pause

Além da conveniência de escrita, a forma de chamada métodos e indexação tem outras vantagens, que não vamos discutir nessa disciplina.
</div>
</div>


# Exercício

Qual é o resultado de cada expressão a seguir?

\small

```python
>>> len('casa') * 'x'

>>> str(10) + 2 * '*' + str(2.0)

>>> 'Jose da Silva'[:4].upper()

>>> 'Jose da Silva'[8:].lower()

>>> str(int('12') * 100)[1:3]

>>> int(('1' * 3 + 3 * '2').upper()[2:5])

```


# Exercício

Qual é o resultado de cada expressão a seguir?

\small

```python
>>> len('casa') * 'x'
'xxxx'
>>> str(10) + 2 * '*' + str(2.0)
'10**2.0'
>>> 'Jose da Silva'[:4].upper()
'JOSE'
>>> 'Jose da Silva'[8:].lower()
'silva'
>>> str(int('12') * 100)[1:3]
'20'
>>> int(('1' * 3 + 3 * '2').upper()[2:5])
12
```


# Definindo novas funções

Além de podermos usar as funções pré-definidas no Python, também podemos definir as nossas próprias funções.

\pause

Apesar de ser possível definir uma nova função na janela de interações, nos vamos fazer isso na janela de edição de código. Isso nos permite salvar o código para uso/edição posterior.


# Definindo novas funções

Para abrir a janela de edição de código selecionamos o menu File $\rightarrow$ New File (crtl + n). \pause

![](imagens/editor.png){width=9cm}


# Definindo novas funções

Vamos criar uma função que calcule o dobro de um dado número. \pause

O que precisamos para definir tal função? \pause

- O nome da função (`dobro`) \pause
- O nome e tipo da entrada (`x: int`{.python}) \pause
- O tipo da saída (`int`{.python}) \pause
- As instruções que calculam o valor da saída a partir da entrada (`2 * x`{.python}) \pause

Com essas informações, definimos a função usando a forma

```python
def nome(entrada1: tipo, entrada2: tipo, ...) -> tipo:
    return exp
```


# Definindo novas funções

<div class="columns">
<div class="column" width="50%">
Escrevemos o código da função na janela de código e salvamos o arquivo (File $\rightarrow$ Save - crtl\ +\ s).

![](imagens/dobro.png){width=6.5cm}

\pause
</div>
<div class="column" width="50%">

Para testar a função executamos o arquivo (Run $\rightarrow$ Run Module - F5) e chamamos a função na janela de interações. \pause

![](imagens/dobro-ex.png){width=6.5cm}
</div>
</div>


# Diferenças entre a janela de interações e a de edição de código

O que acontece se escrevermos o exemplo de execução de `dobro` após a sua definição e executarmos o arquivo?

```python
def dobro(x: int) -> int:
    return 2 * x

dobro(4)
```

\pause

A função `dobro` será executada para o valor `4`{.python} mais nenhum resultado será exibido na tela. \pause

Por que na execução do exemplo na janela de interações o resultado é exibido e aqui não? \pause

Por que o modo de interação a exibição é feita automaticamente (o P -- _print_ -- de REPL) para facilitar a interação com o Python. \pause No arquivo de código, precisamos indicar explicitamente que queremos que o resultado seja exibido.


# Instrução de saída

A forma mais comum de exibir um valor em Python é utilizando a função `print`{.python}. \pause

```python
def dobro(x: int) -> int:
    return 2 * x

print(dobro(4))
```

\pause

Ao executar o código, o valor `8` será exibido na tela. \pause

Note que o `print`{.python} posiciona o cursor no início da próxima linha, dessa forma, a próxima informação começara a ser exibida no início da próxima linha.


# Instrução de saída

A função `print`{.python}, pode ser utilizada com mais de um argumento e os argumentos pode ser de tipos diferentes. Nesse caso, os argumentos são exibidos separados por espaço. \pause

```python
def dobro(x: int) -> int:
    return 2 * x

print("O dobro de 4 é:", dobro(4))
```

Saída

```
O dobro de 4 é: 8
```


# Programas

Agora que aprendemos algumas das construções básicas do Python, podemos avançar e ver como fazer um programa completo. \pause

Para isso, vamos precisar de mais três coisas

- Variáveis
- Instrução de entrada


<!--
# Operações relacionais

Além das operações aritméticas, também podemos fazer operações relacionais com números. \pause

Que resposta você espera a comparação `3 > 4`{.python}? \pause E para `3 < 4`{.python}? \pause

Em Python a resposta da primeira comparação é `False`{.python} (falso) e da segunda `True`{.python} (verdadeiro). \pause

```python
>>> 3 > 4
False
>>> 3 < 4
True
```

\pause

Na computação os valores verdadeiro e falso são chamados de booleanos. Em Python, o tipo dos valores booleanos é `bool`{.python}. As operações relacionais produzem como resposta um valor booleano.


# Operações relacionais

<div class="columns">
<div class="column" width="50%">

```python
>>> # Maior e maior ou igual
>>> 4 > 4
False
>>> 4 >= 4
True
```

\pause

```python
>>> # Menor e menor ou igual
>>> 6 < 6
False
>>> 6 <= 6
True
```

\pause

</div>
<div class="column" width="50%">

```python
>>> # Igual
>>> 5 == 
False
>>> 9 == 4 + 2 ** 2
True
```

\pause

```python
>>> # Igual
>>> 3 * 2 != 4 + 2 ** 2
True
>>> 9 != 4 + 2 ** 2
False
```

</div>
</div>

\pause

Note que as operações relacionais tem prioridade menor do que as operações aritméticas.


# Operações lógicas

Podemos combinar operações relacionais.

-->

# Variáveis

Uma **variável** é um nome para uma região da memória (célula) que é utilizada para armazenar valores. \pause

Cada variável tem um tipo, que determina o conjunto de valores que podem ser armazenados na memória associada com ela. \pause

Uma variável pode ser primeiro declarada e depois inicializa ou pode ser declarada e inicializada de uma vez só. \pause

A forma geral para declaração de variável é (o `valor inicial` é opcional)

```python
nome: tipo [= valor inicial]
```

# Variáveis

```python
>>> a: int = 10
>>> b: int = 2 * a
>>> b
20
```

\pause

As variáveis `a` e `b` foram declaradas com tipo `int`{.python} e inicializadas na declaração. A variável `a` foi inicializada com o valor `10`{.python} e a variável `b` com o valor `2 * a`{.python}. \pause

O símbolo `=` representa **atribuição**. Para executar uma atribuição o Python primeiro avalia a expressão do lado direito para obter um valor, e depois associa a memória que armazena esse valor com o nome da variável.


# Sequenciação de instruções

O Python executa as instruções de forma sequencial, uma linha após a outra, por isso, a ordem das instruções é importante. \pause

Qual o resultado da execução das instruções abaixo?

```python
>>> x: int = 2 * y
>>> y: int = 10
>>> x
?
```

\pause

Um erro de execução! Quando o Python avalia a expressão `2 * y`{.python} a variável `y` ainda não foi definida, então não é possível calcular o valor da expressão.


# Sequenciação de instruções

Qual o resultado de `b` no seguinte trecho de código?

```python
>>> a: int = 10
>>> b: int = 2 * a
>>> a = 30
>>> b
?
```

\pause

`20`{.python}. \pause O Python executar uma linha por vez, na primeira linha a variável `a` é criada referenciando uma célula de memória com o valor `10`{.python}. \pause Depois a expressão `2 * a`{.python} é avaliada com resultado `20`{.python} e a variável `b` é criada referenciado a célula de memória que armazena esse valor. \pause Depois a variável `a` é alterada, passando a referenciar a célula de memória com o valor `30`{.python}. \pause Por vim, o valor armazenado na célula de memória associada com `b`, que é `20`{.python}, é exibido.


# Instrução de entrada

A forma mais comum de ler um valor digitado pelo usuário em Python é utilizando a função `input`{.python}. \pause

```python
nome: str = input('Qual o seu nome?: ')
print('Olá', nome)
```


# Programa para calcular o dobro de um número

```python
def dobro(x: int) -> int:
    return 2 * x

# Entrada
numero: int = int(input('Digite um número inteiro:'))

# Processamento
d: int = dobro(numero)

# Saída
print('O dobro de', numero, 'é', d)
```


# Entrada

A instrução de entrada, assim como a instrução de saída, está na biblioteca `iostream`. \pause Para ler um número de entrada fazemos \pause

<div class="columns">
<div class="column" width="48%">
```cpp
#include <iostream>

using namespace std;

int main()
{
    int a;
    cin >> a;
    cout << a << endl;
}
```

</div>

\pause

<div class="column" width="48%">
O que veremos na tela após a execução desse programa? \pause

O mesmo número repetido duas vezes, na primeira vez é a digitação do usuário e a segunda vez é pelo uso do `cout`. \pause

O que tem de errado com esse programa? \pause

O usuário não é informado sobre o que digitar e nem o que a saída significa.
</div>
</div>

# Entrada (arquivo `echo.cpp`)

```cpp
#include <iostream>

using namespace std;

int main()
{
    cout << "Digite um número: ";
    int a;
    cin >> a;
    cout << "O número que você digitou foi " << a << "." <<endl;
}
```


# Exercício

Agora já podemos fazer um programa completo! \pause

Escreva um programa que calcule a área de um retângulo.


# Exercício (arquivo `area-retangulo.cpp`)

\scriptsize

```cpp
#include <iostream>

using namespace std;

int main()
{
    cout << "Digite a medida da base: ";
    double base;
    cin >> base;

    cout << "Digite a medida da altura: ";
    double altura;
    cin >> altura;

    double area = base * altura;
    cout << "A area do retangulo e "
         << area
         << "."
         << endl;
}
```


# Erros

Vamos parar um pouco e pensar sobre erros. \pause

Durante a compilação de um programa, podem ocorrer dois tipos de erros: \pause

- Sintáticos
- Semânticos


# Erros sintáticos

Um erro sintático ocorre quando não seguimos as regras sintáticas da linguagem e o compilador não consegue "entender" a estrutura do programa.

<div class="columns">
<div class="column" width="30%">

```cpp
int x
cin >> x;
```

\pause

Qual é o erro nesse código? \pause

Falta `;` no final da sentença.

\pause

</div>
<div class="column" width="68%">

\small

Erro gerado pelo `g++`

```
x.cpp: In function ‘int main()’:
x.cpp:8:5: error: expected initializer before ‘cin’
    8 |     cin >> x;
      |     ^~~
```

\pause

Erro gerado pelo `clang++`

```
x.cpp:7:10: error: expected ';' at end of declaration
    int x
         ^
         ;
1 error generated.
```

</div>
</div>



# Erros sintáticos

<div class="columns">
<div class="column" width="30%">

```cpp
int x = (10 + 4;
```

\pause

Qual é o erro nesse código? \pause

Faltou fechar o parêntese.


\pause

</div>
<div class="column" width="68%">

\small

Erro gerado pelo `g++`

```
x.cpp: In function ‘int main()’:
x.cpp:7:20: error: expected ‘)’ before ‘;’ token
    7 |     int x = (10 + 4;
      |             ~      ^
      |                    )
```

\pause

Erro gerado pelo `clang++`

```
x.cpp:7:20: error: expected ')'
    int x = (10 + 4;
                   ^
x.cpp:7:13: note: to match this '('
    int x = (10 + 4;
            ^
1 error generated.
```

</div>
</div>


# Erros sintáticos

<div class="columns">
<div class="column" width="32%">

\footnotesize

```cpp
int nome com espaco = 10;
double namespace = 20.3;
```

\normalsize

Quais os erros nesse código? \pause

Usar nomes inválidos para variáveis. \pause

Um nome não pode ter espaços e nem ser uma palavra chave (como `namespace`{.cpp}).

\pause

</div>
<div class="column" width="66%">

\scriptsize

Erro gerado pelo `g++`

```
x.cpp: In function ‘int main()’:
x.cpp:7:14: error: expected initializer before ‘com’
    7 |     int nome com espaco = 10;
      |              ^~~
x.cpp:8:12: error: expected unqualified-id before ‘namespace’
    8 |     double namespace = 20.3;
      |            ^~~~~~~~~
```

\pause

Erro gerado pelo `clang++`

```
x.cpp:7:13: error: expected ';' at end of declaration
    int nome com espaco = 10;
            ^
            ;
x.cpp:8:12: error: expected unqualified-id
    double namespace = 20.3;
           ^
```

</div>
</div>


# Erros semânticos

Um erro semântico ocorre quando o compilador não "consegue" atribuir um significado para uma construção. \pause


```cpp
int a = 10 + "3";
```

Qual é o erro nesse código? \pause Usar operandos de tipos inválidos para uma operação.

\pause

Erro gerado pelo `g++`

\scriptsize

```
x.cpp: In function ‘int main()’:
x.cpp:7:16: error: invalid operands of types ‘int’ and ‘const char [2]’ to binary ‘operator*’
    7 |     int a = 10 * "3";
      |             ~~ ^ ~~~
      |             |    |
      |             int  const char [2]
```


# Erros semânticos

```cpp
int a = 10.6;
```

\pause

Qual o erro nesse código? \pause Por padrão, esta construção é válida e não gera erro! \pause

Nesse caso, apesar de ir contra a nossa intuição, o compilador atribui um significado para a construção, que é armazenar apenas a parte inteira de `10.6`{.cpp} em `a`. \pause

Às vezes o comportamento da linguagem não está de acordo com a nossa intuição, por isso precisamos conhecer com precisão a semântica da linguagem!


# Erros semânticos

Algumas construções que podem ser propensas a erros são aceitas por padrão pelos compiladores do C++. \pause Como programadores iniciantes, é bom termos um compilador mais "exigente", que nos ajude a identificar essas construções. \pause

Então, para compilarmos os nossos programas, vamos utilizar as opções `-Wall -Wextra -Wconversion -Werror`, que faz o compilador apontar como erro mais construções que não são muito claras.


# Erros semânticos

```cpp
int main()
{
    int a = 10.6;
}
```

Compilando o programa acima com o comando

```
g++ -Wall -Wextra -Wconversion -Werror arquivo.cpp
```

Produz a seguinte mensagem de erro

\scriptsize

```
x.cpp: In function ‘int main()’:
x.cpp:7:13: error: conversion from ‘double’ to ‘int’ changes value from ‘1.06e+1’ to ‘10’
    7 |     int a = 10.6;
      |             ^~~~
```


# Erros de execução

Se um programa foi compilado corretamente, isto é, não tem erros de sintaxe ou semântica, significa que ele não tem erros? \pause Não! \pause Erros podem ocorrer durante a execução do programa. \pause

Um erro de execução pode fazer o programa \pause

- Ser interrompido e exibir uma mensagem de erro (crashar) \pause
- Entrar em um laço infinito e nunca terminar (travar) \pause
- Continuar a execução e produzir a resposta errada


# Erros de execução

No programa que calcula a área do retângulo, o que acontece se o usuário digitar um número muito grande ou digitar algo que não é um número? \pause O programa executa até o final mas produz uma resposta incorreta. \pause

Como garantir que um programa não terá erros em tempo de execução? \pause Veremos isso ao longo da disciplina.


# Construções

Vamos voltar para o programa que calcula a área de um retângulo. \pause

<div class="columns">
<div class="column" width="50%">
\footnotesize
```cpp
#include <iostream>
using namespace std;
int main() {
    cout << "Digite a medida da base: ";
    double base;
    cin >> base;

    cout << "Digite a medida da altura: ";
    double altura;
    cin >> altura;

    double area = base * altura;
    cout << "A area do retangulo e "
         << area  << "." << endl;
}
```
</div>
<div class="column" width="50%">
\pause
\small

Quais construções da linguagem usamos nesse programa? \pause

- Uso de biblioteca e namespace; \pause
- Comandos de entrada e saída; \pause
- Tipo de dado e variáveis numéricos; \pause
- Operações com números. \pause

O que precisamos para escrever programas mais interessantes? \pause

- Outras operações com números; \pause
- Outros tipos de dados e operações; \pause
- Maneira de criar e nomear novas operações;

</div>
</div>


# Outras operações com números

As quatro operações aritméticas podem ser usadas com número inteiros ou de ponto flutuante. \pause Se os dois operandos são `int`{.cpp}, então o resultado é `int`{.cpp}. \pause Se pelo menos um dos operandos é `double`{.cpp}, então o resultado é `double`{.cpp}.

# Outras operações com números

<div class="columns">
<div class="column" width="50%">
\small

```cpp
// Soma e subtração
10 + 3 - 20.5; // -7.5
// Multiplicação
13 * 3; // 39
// Divisão "real"
21 / 3.0; // 7.0
21 / 8.0; // 2.625
// Divisão inteira
21 / 3; // 7;
21 / 8; // 2;
// Menos e mais unário
int a = 10;
-a; // -10;
+a; // +10;
```
\pause

</div>
<div class="column" width="50%">
Para números inteiros, também temos a operação de módulo (resto da divisão) \pause

```cpp
21 % 3; // 0
21 % 8; // 5
```
</div>
</div>


# Outras operações com números

Outras operações estão disponíveis na biblioteca [`cmath`](https://en.cppreference.com/w/cpp/header/cmath). \pause Alguns exemplos

\small

```cpp
// Função piso - maior inteiro que não é maior que o número
floor(1.0); // 1.0
floor(1.3); // 1.0
floor(1.5); // 1.0
floor(1.7); // 1.0
// Função teto - menor inteiro que não é menor que o número
ceil(1.3); // 2.0
ceil(1.5); // 2.0
ceil(1.7); // 2.0
ceil(2.0); // 2.0
// Função de aredondadmento - inteiro mais próximo do número
round(1.3); // 1.0
round(1.5); // 2.0
round(1.7); // 2.0
```

# Outras operações com números

```cpp
// Módulo (resto da divisão) para double
fmod(5.5, 2.0); // 1.5
fmod(15.0, 5.0); // 0.0
// Seno (o argumento é em radianos)
sin(3.14); // 0.00159265
// Raiz quadrada
sqrt(2.0); // 1.41421
// Exponencial
pow(2, 4); // 16
```

\pause

Podemos fazer muitas coisas com valores numéricos! \pause Mas também temos outros tipos de valores.


# Strings

Informações textuais podem ser representas por cadeias de caracteres. \pause

Usamos o tipo `string`, definido na biblioteca `string`, para armazenar cadeia de caracteres. \pause

Valores literais de strings são delimitados por `"`{.cpp}. \pause

```cpp
#include <string>

using namespace std;

int main()
{
    string nome = "Joao da Silva";
}
```


# Strings

Assim como podemos fazer operações com números, também podemos fazer operações com strings. \pause

```cpp
string nome = "Joao da Silva";

// Concatenação de strings
string junior = nome + " Filho"; // "Joao da Silva Filho"

// Extração de substring
// A partir da primeira letra, que está no índice 0,
// pegue 4 bytes (nesse caso, caracteres)
string primeiro_nome = nome.substr(0, 4); // "Joao"
```


# Strings

```cpp
string nome = "Joao da Silva";
```

Como extrair a substring `"Silva"` de `nome`? \pause `nome.substr(8, 5)`{.cpp}. \pause

Note que o segundo argumento para `substr` representa a quantidade de bytes (nesse caso, caracteres) a serem extraídos. \pause

O que acontece se especificarmos uma quantidade de bytes para extrair maior do que o "disponível", como por exemplo, `nome.substr(8, 7)`{.cpp}? \pause O método retorna apenas o que está disponível, nesse caso, `"Silva"`{.cpp}.


# Strings

Escreva um programa que leia um nome de uma pessoa e escreva uma mensagem de boas vindas para a pessoa.

\pause

Para ler uma string é necessário usar a função `getline` da biblioteca `string` da seguinte forma:

```cpp
string s;
getline(cin, s);
```


# Strings

```cpp
#include <iostream>
#include <string>

using namespace std;

int main()
{
    cout << "Nome: ";
    string nome;
    getline(cin, nome);

    cout << "Ola " << nome <<  ", seja bem vindo!" << endl;
}
```


# Booleanos

Qual resposta você daria para as seguintes expressões? \pause

`5 < 10`{.cpp} \pause, Verdadeiro. \pause

`9 + 2 > 7 * 2`{.cpp} \pause, Falso. \pause

O tipo `bool`{.cpp} (booleano) tem dois valores, verdadeiro (`true`{.cpp}) e falso (`false`{.cpp}). Assim como números e strings, os valores do tipo booleano podem ser armazenados e manipulados.


# Booleanos

```{.cpp}
bool a = true;
bool b = false;

string nome = "Jose";
// O operador == verifica se dois valores são iguais
bool chama_jose = nome == "Jose"; // true

// Operador >= (maior ou igual)
int idade = 17;
bool maior_de_idade = idade >= 18; // false
// Também podemos usar >, < e <=
```

# Booleanos

Os operadores de `==`{.cpp} (igual) e `!=`{.cpp} (diferente) também podem ser usados para números e outros tipos de dados. \pause

```{.cpp}
bool a = true;
bool b = false;
```

Qual o resultado de `a == b`{.cpp}? \pause O resultado é `false`{.cpp} pois o valor armazenado em `a`{.cpp} não é igual ao valor armazenado em `b`{.cpp}. \pause

Qual o resultado de `a != b`{.cpp}? \pause O resultado é `true`{.cpp} pois o valor armazenado em `a`{.cpp} é diferente do valor armazenado em `b`{.cpp}.


# Booleanos

Três operações são comuns com valores booleanos: \pause

- Negação \pause
- E lógico (conjunção) \pause
- Ou lógico (disjunção)


# Booleanos - Negação

Em C++ o símbolo da operação de negação é `!`{.cpp}. \pause

Qual o valor da expressão `4 < 5`{.cpp}? \pause `true`{.cpp}. \pause E da expressão `!(4 < 5)`{.cpp}? \pause `false`{.cpp}. \pause

Qual o valor da expressão `2 == 1 + 2`{.cpp}? \pause `false`{.cpp}. \pause E da expressão `!(2 == 1 + 2)`{.cpp}? \pause `true`{.cpp}.  \pause

Tabela verdade

a        | !a
---------|---------
 `false` | `true`
 `true`  | `false`


# Booleanos - Conjunção

Em C++ o símbolo da operação de conjunção é `&&`{.cpp} \pause


Tabela verdade

a        |  b      | a && b
---------|---------|---------
 `false` | `false` | `false`
 `false` | `true ` | `false`
 `true`  | `false` | `false`
 `true`  | `true`  | `true`


# Booleanos - Disjunção

Em C++ o símbolo da operação de disjunção é `||`{.cpp} \pause


Tabela verdade

a        |  b      | a && b
---------|---------|---------
 `false` | `false` | `false`
 `false` | `true ` | `true`
 `true`  | `false` | `true`
 `true`  | `true`  | `true`


# Booleanos

Em uma determinada cidade o transporte público é gratuito para crianças menores de 10 anos, adultos a partir de 60 anos e professores a partir de 50 anos. Escreva um programa que leia a idade de uma pessoa e se ela é professor e indique se essa pessoa pode usar o transporte público de forma gratuita. \pause

Em C++ na entrada e saída de valores booleanos `0`{.cpp} é usado para indicar `false`{.cpp} e `1`{.cpp} é usado para indicar `true`{.cpp}.


# Booleanos

\scriptsize

```cpp
#include <iostream>

using namespace std;

int main()
{
    cout << "Idade: ";
    int idade;
    cin >> idade;

    cout << "E professor? ";
    bool eh_professor;
    cin >> eh_professor;

    // Note que && tem priodade sobre ||
    bool livre = idade < 10 || idade >= 60 || idade >= 50 && eh_professor;

    cout << "Pode usar o transporte publico de forma gratuita? " << livre << endl;
}
```


# Combinado dados de tipo diferente

Podemos usar tipos diferentes na mesma expressão. \pause

```cpp
string texto = "1023"

// texto.length() produz a quantidade de bytes em texto
bool tem_4_caracteres = texto.length() == 4; // true

// stoi converte uma string que representa um número inteiro
// em um número inteiro
int x = stoi(texto) + 10; // 1033

// to_string converte um número para uma string
string r = texto + to_string(x); // "10231033"
```


# Criar e nomear novas operações

Vimos que para escrever programas mais interessantes vamos precisar de:

- Outras operações com números; \pause
- Outros tipos de dados e operações; \pause
- Maneira de criar e nomear novas operações; \pause Ou seja, nós vamos criar as nossas próprias funções!


# Criação de funções

A forma geral para definição de funções é \pause

\small

```cpp
TipoSaida nome_da_funcao(TipoEntrada1 entrada1, TipoEntrada2 entrada2, ...)
{
    return saida_da_funcao;
}
```

\pause

\normalsize

Baseado no programa que calcula a área de um retângulo, vamos criar uma função para calcular a área de um retângulo. (Solução desenvolvida em sala)


# Criação de funções

\small

```cpp
// Calcula a área do retângulo com a base b e a altura a.
// 10.0 5.0 -> 50.0
// 2.0 3.0 -> 6.0
double area_retangulo(double b, double a) {
    return b * a;
}

int main()
{
    // entrada omitida para economizar espaço no slide
    double area = area_retangulo(base, altura);
    // saída omitida para economizar espaço no slide
}
```


# Exercício

Projete um programa que a partir de um tempo especificado em número de horas, minutos e segundos, calcule o total de segundos do tempo.

\pause

Projeto feito em sala.


# Exercício

```cpp
// As h, m, s serão representados por inteiros positivos

// Calcula o total de segundos do tempo com h horas,
// m minutos e s segundos.
// Exemplos
// h=0 m=0 s=4 -> 4 + 0 * 60 + 0 * 3600 -> 4
// h=0 m=10 s=5 -> 5 + 10 * 60 + 0 * 3600 -> 605
// h=3 m=2 s=25 -> 25 + 2 * 60 + 3 * 3600 -> 10945
int total_segundos(int h, int m, int s)
{
    return s + m * 60 + h * 3600;
}
```

# Referências

Referências

- [Tutorial C++ - W3 Schools](https://www.w3schools.com/cpp/)

https://docs.microsoft.com/pt-br/cpp/?view=msvc-160

https://docs.microsoft.com/pt-br/cpp/cpp/cpp-language-reference?view=msvc-160

https://docs.microsoft.com/pt-br/cpp/cpp/welcome-back-to-cpp-modern-cpp

https://devdocs.io/

https://www.cplusplus.com

https://cppreference.com
!>
