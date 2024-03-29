---
# vim: set spell spelllang=pt_br:
title: Seleção, enumerações e estruturas
# TODO: deixar claro que cada bloco pode ter mais de uma instrução
# TODO: dar nome ao processo de criar a implementação analisando as formas de resposta
# TODO: falar do contrato de função, entre o fornecedor e o usuário da função
# TODO: explicar diretamente como escrever os exemplos para funções que retornam enum
# TODO: apresentar match/case?
# TODO: adicionar mais exemplos (juntando estruturas e enumerações, contagem de tipos de sorvertes?)
#       a questão é que atualizar uma contagem pode requerer passagem por referência.
# TODO: adicionar exemplos com tipos dos campos diferentes
# TODO: deixar claro que valores dos tipos estruturas são mutáveis por padrão?
---

# Introdução

Antes de estudarmos instruções de seleção, vamos revisar como o Python executa um programa.


# Execução de funções

<div class="columns">
<div class="column" width="48%">
\small

```{.python .number-lines}
def dobro_mais_um(n: int) -> int:
    a = 2 * n
    return a + 1

def main():
   a = 5
   n = dobro_mais_um(a + 4) + 1
   print(n)

main()
```
</div>
<div class="column" width="48%">
\pause
Qual o valor exibido pelo programa? \pause

Não tente "executar" a chamada da função `dobro_mais_um`, pense apenas no seu propósito, sem olhar para o seu corpo. \pause

Então, qual é o valor exibido na tela? \pause 20. \pause

Qual é a ordem que as linhas são executadas? \pause

10, \pause 6, \pause 7, \pause 2, \pause 3, \pause 7, \pause 8, \pause 10

</div>
</div>


# Seleção

O fluxo "normal" de execução de um programa é sequencial, isto é, a execução é de uma linha após a outra. Algumas instruções alteram esse fluxo, como por exemplo, as chamadas e retornos de funções. \pause

Agora veremos a **instrução de seleção** `if else`{.python} (se e senão em inglês), que permite, a partir de uma condição, escolher qual conjunto de instruções executar.


# Seleção

<div class="columns">
<div class="column" width="48%">

A forma geral do `if else`{.python} é:

```python
if condição:
    instruções então
else:
    instruções senão
```

\pause

</div>
<div class="column" width="48%">

Como a instrução `if else`{.python} é executada? \pause O Python avalia a condição e verifica o resultado \pause

- Se o resultado for `True`{.python}, então as instruções do bloco "instruções então" são executadas; \pause
- Senão (o resultado é `False`{.python}), as instruções do bloco "instruções senão" são executadas;

</div>
</div>


# Exemplo

<div class="columns">
<div class="column" width="48%">

```{.python .number-lines}
a = 10
b = 20;
if a > b:
    m = a
else:
    m = b
print(m)
```

\pause

Qual o valor exibido pelo programa? \pause 20. \pause

Em que ordem as linhas são executas para gerar esse resultado? \pause 1, 2, 3, 6, 7. \pause
</div>
<div class="column" width="48%">

```{.python .number-lines}
a = 15
b = 8;
if a > b:
    m = a
else:
    m = b
print(m)
```

\pause

Qual o valor exibido pelo programa? \pause 15. \pause

Em que ordem as linhas são executas para gerar esse resultado? \pause 1, 2, 3, 4, 7 \pause
</div>
</div>

\ 

Qual é o propósito do `if else`{.python} nesses exemplos? \pause Determinar o valor máximo entre `a` e `b`.


# Máximo

Vamos projetar uma função para encontrar o máximo entre dois números. \pause

<div class="columns">
<div class="column" width="50%">

\footnotesize

```{.python .number-lines}
def maximo(a: int, b: int) -> int:
    '''Devolve o valor máximo entre *a* e *b*.
    Exemplos
    >>> # a é o máximo
    >>> maximo(10, 8)
    10
    >>> # b é o máximo
    >>> maximo(-2, -1)
    -1
    '''
    if a > b:
        m = a
    else:
        m = b
    return m
```

</div>
<div class="column" width="46%">
\pause

Vamos treinar mais uma vez a execução passo a passo. \pause

Qual é a ordem que as linhas são executadas para o exemplo `maximo(10, 8)`{.python}? \pause

11, \pause 12, \pause 15 \pause

Qual é a ordem que as linhas são executadas para o exemplo `maximo(-2, -1)`{.python}? \pause

11, \pause 14, \pause 15

</div>
</div>


# Atualização número de telefone

Como "descobrimos" que precisamos utilizar uma instrução de seleção? \pause

Vamos voltar ao exemplo da atualização do número do telefone. \pause

No período de 2015 à 2016 todos os números de telefones celulares no Brasil passaram a ter nove dígitos. Na época, os números de telefones que tinham apenas oito dígitos foram alterados adicionando-se o 9 na frete do número. Embora oficialmente todos os número de celulares tenham nove dígitos, na agenda de muitas pessoas ainda é comum encontrar números registrados com apenas oito dígitos. Projete uma função que adicione o nono dígito em um dado número de telefone celular caso ele ainda não tenha o nono dígito. Considere que os números de entrada são dados com o DDD entre parênteses e com um hífen separando os últimos quatro dígitos. Exemplos de entradas: (44) 9787-1241, (51) 95872-9989, (41) 8876-1562. A saída deve ter o mesmo formato, mas garantindo que o número do telefone tenha 9 dígitos.


# Especificação

\footnotesize

```python
def ajusta_numero(numero: str) -> str:
    '''
    Ajusta *numero* adicionando o 9 como nono dígito se necessário, ou seja, se
    *numero* tem apenas 8 dígitos (sem contar o DDD).

    Requer que numero esteja no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX, onde
    X pode ser qualquer dígito.

    Exemplos
    >>> # não precisa de ajuste, a saída e a própria entrada
    >>> ajusta_numero('(51) 95872-9989')
    '(51) 95872-9989'
    >>> # '(44) 9787-1241'[:5] + '9' + '(44) 9787-1241'[5:]
    >>> ajusta_numero('(44) 9787-1241')
    '(44) 99787-1241'
    '''
    return numero
```


# Implementação

Até agora, todas as funções que projetamos tinham apenas uma "forma" de gerar o resultado. \pause

Na função `ajusta_numero`, existem duas "formas" para a resposta: o próprio número ou o número ajustado. \pause

Como escolher quando cada forma deve ser utilizada na resposta da função? \pause Utilizando um condição: \pause

- Se a quantidade de caracteres de `numero` for 15, então a resposta é `numero`; \pause

- Senão a resposta é `numero[:5] + '9' + numero[5:]`{.python}. \pause

Quando a resposta depende de uma ou mais condições, usamos uma instrução de seleção!


# Implementação

\small

```python
def ajusta_numero(numero: str) -> str:
    if len(numero) == 15:
        ajustado = numero
    else:
        ajustado = numero[:5] + '9' + numero[5:]
    return ajustado
```


# Máximo de 3

Projete uma função que encontre o valor máximo entre três números.


# Análise e definição de tipos de dados

Análise \pause

- Encontrar o valor máximo entre três número dados \pause

Tipos de dados \pause

- Os valores serão números inteiros \pause

Especificação (assinatura e propósito) \pause

\small

```python
def maximo3(a: int, b: int, c: int) -> int:
    '''
    Encontra o valor máximo entre *a*, *b* e *c*.
    '''
```


# Exemplos e implementação

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
>>> maximo3(20, 10, 12) # a é o máximo
20
>>> maximo3(20, 12, 10)
20
>>> maximo3(20, 12, 12)
20
>>> maximo3(20, 20, 20)
20
>>> maximo3(5, 12, 3) # b é o máximo
12
>>> maximo3(3, 12, 5)
12
>>> maximo3(5, 12, 5)
12
>>> maximo3(4, 8, 18) # c é o máximo
18
>>> maximo3(8, 4, 18)
18
>>> maximo3(8, 8, 18)
18
```

\pause
</div>
<div class="column" width="48%">

\small

Implementação \pause

Quantas "formas" de resposta nós temos? \pause 3. \pause Ou a resposta é `a`, ou a resposta é `b`, ou a resposta é `c`. \pause

Se temos formas de respostas diferentes, então a resposta depende de uma ou mais condições. \pause Então, usamos instruções de seleção. \pause

Qual é a condição para a resposta ser `a`? \pause `a >= b and a >= c`{.python} \pause

Qual é a condição para a resposta ser `b`? \pause `b >= a and b >= c`{.python} \pause

Qual é a condição para a resposta ser `c`? \pause `c >= a and c >= b`{.python} \pause

Agora podemos escrever o corpo da função!

</div>
</div>


# Implementação

<div class="columns">
<div class="column" width="55%">
\footnotesize

```{.python .number-lines}
def maximo3(a: int, b: int, c: int) -> int:
    '''
    Encontra o valor máximo entre
    *a*, *b* e *c*.
    '''
    if a >= b and a >= c:
        m = a
    else:
        if b >= a and b >= c:
            m = b
        else: # c >= a and c >= b
            m = c
    return m
```

\pause

</div>
<div class="column" width="45%">

Vamos treinar mais uma vez a execução passo a passo. \pause

Qual é a ordem que as linhas são executadas para o exemplo a seguir:

`maximo(10, 6, 8)`{.python}? \pause 6, \pause 7, \pause 13 \pause

`maximo(10, 15, 8)`{.python}? \pause 6, \pause 9, \pause 10, \pause 13 \pause

`maximo(10, 15, 20)`{.python}? \pause 6, \pause 9, \pause 12, \pause 13
</div>
</div>


# Verificação e revisão

<div class="columns">
<div class="column" width="60%">
\footnotesize

```python
def maximo3(a: int, b: int, c: int) -> int:
    '''
    Encontra o valor máximo entre
    *a*, *b* e *c*.
    '''
    if a >= b and a >= c:
        m = a
    else:
        if b >= a and b >= c:
            m = b
        else: # c >= a and c >= b
            m = c
    return m
```

</div>
<div class="column" width="40%">

\pause

Verificação: \pause ok. \pause

Revisão \pause

Podemos modificar o código para torná-lo mais fácil de ler e entender? \pause Sim!

O Python permite "juntar" um `else`{.python} seguido de um `if`{.python} em um `elif`{.python}. Isto ajuda a diminuir os níveis de indentação, facilitando a escrita e leitura do código.
</div>
</div>


# Revisão

\footnotesize

```python
def maximo3(a: int, b: int, c: int) -> int:
    '''
    Encontra o valor máximo entre
    *a*, *b* e *c*.
    '''
    if a >= b and a >= c:
        m = a
    elif b >= a and b >= c:
        m = b
    else: # c >= a and c >= b
        m = c
    return m
```


# Implementação

Vamos parar por um momento e relembrar como fazemos a implementação de uma função. \pause

Olhamos para a especificação, com atenção especial para os exemplos, e perguntamos: quantas formas de resposta temos nos exemplos? \pause

- Se existe apenas uma forma de resposta, isto é, a resposta dos exemplos são sempre calculadas da mesma forma, então usamos essa forma para implementar a função. \pause

- Se existe mais de uma forma, isto é, a resposta para pelo menos dois exemplos tem a forma distinta, então precisamos usar seleção. \pause Para cada forma de resposta identificamos uma condição e usamos as condições e as formas de resposta para implementar a função (o que fizemos na implementação da função `maximo3`).


# Implementação

No caso de mais de uma forma de resposta, a condição de cada forma pode ser composta, como no exemplo `maximo3`, onde a condição para a resposta ser `a`{.python} era `a >= b and a >= c`{.python} (a condição é composta por duas partes). \pause

Nesses casos, podemos verificar cada parte da condição de forma separada. A cada verificação, dividimos as formas de resposta em dois grupos, as que precisam da condição e as que não precisam da condição. Usando verificação subsequentes, vamos restringindo as opções de forma de resposta até chegar em apenas uma forma. \pause

Vamos tentar utilizar essa abordagem para fazer um implementação alternativa da função `maximo3`.


# Implementação alternativa

Se `a >= b`{.python} é `True`{.python}, quais valores podem ser o máximo? \pause Os valores de `a` e `c`. \pause E como descobrimos quem é o máximo entre `a` e `c`? \pause Fazendo outra seleção. \pause

Se `a >= b`{.python} é `False`{.python}, quais valores podem ser o máximo? \pause Os valores de `b` e `c`. \pause E como descobrimos quem é o máximo entre `b` e `c`? \pause Fazendo outra seleção.


# Implementação alternativa

<div class="columns">
<div class="column" width="48%">

Versão alternativa

\footnotesize

```python
def maximo3(a: int, b: int, c: int) -> int:
    if a >= b:
        if a >= c:
            m = a
        else:
            m = c
    else:
        if b >= c:
            m = b
        else:
            m = c
    return m
```

\pause
</div>
<div class="column" width="48%">

Primeira versão

\footnotesize

```python
def maximo3(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        m = a
    elif b >= a and b >= c:
        m = b
    else: # c >= a and c >= b
        m = c
    return m
```

\pause

\small

Qual versão é mais fácil de entender? \pause A primeira... \pause

Podemos melhorar? \pause Sim!
</div>
</div>


# Revisão

<div class="columns">
<div class="column" width="60%">

\footnotesize

```{.python .number-lines}
def maximo3(a: int, b: int, c: int) -> int:
    if a >= b:
        if a >= c:
            m = a
        else:
            m = c
    else:
        if b >= c:
            m = b
        else:
            m = c
    return m
```
</div>
<div class="column" width="40%">
\pause
Qual o propósito do bloco das linhas de 3 à 6? \pause Encontrar o máximo entre `a` e `c`. \pause

Qual o propósito do bloco das linhas de 8 à 11? \pause Encontrar o máximo entre `b` e `c`. \pause

Já temos uma função para encontrar o máximo entre dois números? \pause Sim! \pause A função `maximo` que fizemos anteriormente. \pause

Então vamos usar a função!
</div>
</div>


# Revisão

<div class="columns">
<div class="column" width="60%">

\footnotesize

```{.python .number-lines}
def maximo3(a: int, b: int, c: int) -> int:
    if a >= b:
        m = maximo(a, c)
    else:
        m = maximo(b, c)
    return m
```
</div>
<div class="column" width="40%">
\pause
Qual o propósito da seleção da linha 2? \pause Encontrar o máximo entre `a` e `b`... \pause Nós já temos uma função para fazer isso!
</div>
</div>


# Revisão

```python
def maximo3(a: int, b: int, c: int) -> int:
    return maximo(maximo(a, b), c)
```

\ 

\pause

Poderíamos ter chegado nessa implementação na primeira vez? \pause

Sim, mas nesse caso, deveríamos ter visto que as três formas de resposta distintas poderiam ter sido generalizadas em uma única forma, que é `maximo(maximo(a, b), c)`{.python}. Essa generalização direta requer prática, por enquanto, podemos fazer os casos distintos e tentar, durante a revisão, simplificar o código.


# Execução passo a passo

<div class="columns">
<div class="column" width="60%">

\small

```{.python .number-lines}
def maximo(a: int, b: int) -> int:
    if a > b:
        m = a
    else:
        m = b
    return a

def maximo3(a: int, b: int, c: int) -> int:
    return maximo(maximo(a, b), c)

maximo3(10, 2, 15)
```
</div>
<div class="column" width="40%">
\pause

Vamos treinar mais uma vez a execução passo a passo. \pause

Qual é a ordem que as linhas são executadas para o exemplo ao lado? \pause

11, 9, 2, 3, 6, 9, 2, 5, 6, 9, 11.

</div>
</div>


# Ponto final

<div class="columns">
<div class="column" width="48%">
Em um determinado programa é necessário que o texto digitado pelo usuário termine com um ponto. Projete uma função que coloque um ponto final em um texto se ele ainda não terminar com ponto.
</div>
<div class="column" width="48%">
\pause

Análise \pause

- Colocar um ponto final em um texto caso ele ainda não termine com ponto. \pause

Definição dos tipos de dados \pause

- O texto é representado por uma string.
</div>
</div>


# Ponto final - especificação

<div class="columns">
<div class="column" width="48%">

\footnotesize

```python
def ponto_final(texto: str) -> str:
    '''
    Coloca um ponto final em *texto* se
    *texto* não termina com ponto final.

    Exemplos
    >>> # Não adiciona o ponto
    >>> ponto_final('Talvez.')
    'Talvez.'
    >>> # Adiciona ponto
    >>> ponto_final('Sim, eu gostaria')
    'Sim, eu gostaria.'
    '''
```

</div>
<div class="column" width="48%">

\pause

Essa especificação está completa? \pause Não! \pause

Está faltando considerar um caso extremo, quando `texto` é vazio. \pause

Como proceder nesse caso? \pause Temos duas opções: \pause

- Definimos que vazio não é uma entrada válida; ou \pause

- Definimos uma saída para a entrada vazia. \pause

Vamos explorar as duas possibilidades.

</div>
</div>


# Ponto final - especificação - vazio inválido

<div class="columns">
<div class="column" width="48%">

\footnotesize

```python
def ponto_final(texto: str) -> str:
    '''
    Coloca um ponto final em *texto* se
    *texto* não termina com ponto final.
    Requer que *texto* não seja vazio.

    Exemplos
    >>> # Não adiciona o ponto
    >>> ponto_final('Talvez.')
    'Talvez.'
    >>> # Adiciona ponto
    >>> ponto_final('Sim, eu gostaria')
    'Sim, eu gostaria.'
    '''
```

</div>
<div class="column" width="48%">

\pause

Implementação

\pause

Como temos duas formas de resposta, adiciona ou não o ponto, usamos seleção. \pause A condição para não adicionar ponto é que `texto` termine com ponto. \pause

\footnotesize

```python
def ponto_final(texto: str) -> str:
    assert texto != ''
    if texto[len(texto) - 1] == '.':
        com_ponto = texto
    else:
        com_ponto = texto + '.'
    return com_ponto
```
</div>
</div>


# `assert`{.python}

Usamos o `assert`{.python} quando queremos expressar uma condição que precisa ser verdadeira para que o código continue executando. Caso a condição não seja verdadeira, o programa é interrompido (crasha) com uma mensagem de erro. \pause

O que acontece na função `ponto_final` se não utilizarmos o `assert`{.python} e a função for chamada com o argumento `''`{.python}? \pause

Vai crashar na expressão `texto[len(texto) - 1]`{.python}, pois estamos querendo acessar o último caractere de uma string vazia. \pause

Se usando ou não o `assert`{.python} o programa crasha, porque utilizar o `assert`{.python}? \pause Para que a falha tenha uma causa mais precisa, facilitando a depuração do programa.


# Ponto final - especificação - vazio válido

<div class="columns">
<div class="column" width="48%">

\footnotesize

```python
def ponto_final(texto: str) -> str:
    '''
    Coloca um ponto final em *texto* se
    *texto* não termina com ponto final
    e não é ''. Devolve *texto* caso
    contrário.

    Exemplos
    >>> # Não adiciona o ponto
    >>> ponto_final('')
    ''
    >>> ponto_final('Talvez.')
    'Talvez.'
    >>> # Adiciona ponto
    >>> ponto_final('Sim, eu gostaria')
    'Sim, eu gostaria.'
    '''
```

</div>
<div class="column" width="48%">

\pause

Implementação

\pause

Como temos duas formas de resposta, adiciona ou não o ponto, usamos seleção. \pause A condição para não adicionar ponto é que `texto` seja `''`{.python} ou termine com ponto. \pause

\footnotesize

```python
def ponto_final(texto: str) -> str:
    if texto == '' or \
                texto[len(texto) - 1] == '.':
        com_ponto = texto
    else:
        com_ponto = texto + '.'
    return com_ponto
```
</div>
</div>


# Exemplo - Álcool ou Gasolina?

<div class="columns">
<div class="column" width="48%">
Depois que você fez o programa para o André, a Márcia, amiga em comum de vocês, soube que você está oferecendo serviços desse tipo e também quer a sua ajuda. O problema da Márcia é que ela sempre tem que fazer a conta manualmente para saber se deve abastecer o carro com álcool ou gasolina. A conta que ela faz é verificar se o preço do álcool é até 70% do preço da gasolina, se sim, ela abastece o carro com álcool, senão ela abastece o carro com gasolina. Você pode ajudar a Márcia também?
\pause
</div>
<div class="column" width="48%">
Análise \pause

- Determinar o combustível que será utilizado. Se o preço do álcool for até 70% do preço da gasolina, então deve-se usar álcool, senão gasolina.

\pause

Definição de tipos de dados \pause

- O preço do litro do combustível será representado por um número positivo; \pause

- O tipo de combustível será representado por uma string.
</div>
</div>


# Especificação

\footnotesize

```python
def indica_combustivel(preco_alcool: float, preco_gasolina: float) -> str:
    '''
    Indica o combustível que deve ser utilizado no abastecimento. Produz
    'alcool' se *preco_alcool* for menor ou igual a 70% do *preco_gasolina*,
    caso contrário produz 'gasolina'.

    Exemplos
    >>> # 'alcool'
    >>> indica_combustivel(4.00, 6.00) # 4.00 <= 0.7 * 6.00 é True
    'alcool'
    >>> indica_combustivel(3.50, 5.00) # 3.50 <= 0.7 * 5.00 é True
    'alcool'
    >>> # 'gasolina'
    >>> indica_combustivel(4.00, 5.00) # 4.00 <= 0.7 * 5.00 é False
    'gasolina'
    '''
```


# Implementação

Quantas formas para a resposta existem? \pause Duas: `'alcool'`{.python} e `'gasolina'`{.python}. \pause Então precisamos usar seleção. \pause Qual é a condição para que a resposta seja `'alcool'`{.python}? \pause `preco_alcool <= 0.7 * preco_gasolina`{.python} \pause

\small

```python
def indica_combustivel(preco_alcool: float, preco_gasolina: float) -> str:
    if preco_alcool <= 0.7 * preco_gasolina:
        combustivel = "alcool"
    else:
        combustivel = "gasolina"
    return combustivel
```


# Verificação e revisão

Verificação: \pause ok. \pause

Revisão: \pause string não parece ser um tipo de dado apropriado... \pause

Vamos parar um momento e conversar sobre a etapa de definição de tipos de dados.


# Definição de tipos de dados

Durante a etapa de definição de tipos de dados identificamos as informações e definimos como elas são representadas no programa. \pause

Essa etapa pode ter parecido, até então, muito simples ou talvez até desnecessária, isto porque as informações que precisávamos representar eram "simples". \pause

No entanto, essa etapa é muito importante no projeto de programas, de fato, uma representação adequada pode facilitar a escrita do programa e diminuir as possibilidades de erros, aumentando a confiabilidade do programa. \pause

Mas o que exatamente é um tipo de dado e como projetar um tipo de dado adequado para representar uma informação?


# Tipos de dados

Um **tipo de dado** é o conjunto de valores que uma variável pode assumir. \pause

Exemplos \pause

- `bool`{.python} $= \{$ `True`{.python} , `False`{.python} $\}$ \pause
- `int`{.python} = $\{\dots, -2, -1, 0, 1, 2, \dots \}$ \pause
- `float`{.python} = $\{\dots, -0.1, -0.0, 0.0, 0.1, \dots \}$ \pause
- `str`{.python} = $\{$ `''`{.python}, `'a'`{.python}, `'b'`{.python}, $\dots \}$


<!--
# Tipos de dados

Para uma variável do tipo `bool`{.python}, apenas dois valores são válidos. \pause

Para uma variável do do tipo `int`{.python}, qualquer número inteiro é válido (na prática existe um limite). \pause Em outras linguagens, como C/C+++, um `int`{.c} só pode armazenar inteiros no intervalo de $-2.147.483.648$ a $2.147.483.647$. \pause

Uma variável do tipo `float`{.python} pode assumir um de pouco menos do que $2^{64}$ valores (esses valores estão distribuídos no intervalo de $2.2250738585072014 \times 10^{-308}$ a $1.7976931348623157 \times 10^{308}$).
-->


# Requisitos de um tipo de dado

Um inteiro é adequado para representar a quantidade de pessoas em um planeta? \pause

- Não é adequado pois um número inteiro pode ser negativo mas a quantidade de pessoas em um planeta não pode, ou seja, o tipo de dado permite a representação de valores inválidos. \pause

O ideal seria um número natural, mas o Python não tem um tipo de dado específico para representar apenas números naturais. \pause Outras linguagens oferecem outras opções. Por exemplo, em Rust temos `u32`{.rust} ($0$ a $4.294.967.296$) e `u64`{.rust} ($0$ a $18.446.744.073.709.551.616$). \pause

`u32`{.rust} seria adequado para representar a quantidade de pessoas em um planeta? \pause

- Não pois o número pessoas no planeta terra não está no intervalo de valores válidos para o tipo, ou seja, nem todos os valores válidos poder ser representados.


# Requisitos de um tipo de dado

Durante a etapa de definição de tipos de dados temos que levar em consideração as seguintes diretrizes:

- Faça os valores válidos representáveis.

- Faça os valores inválidos irrepresentáveis.

\pause

Quando fizemos o projeto da função `indica_combustivel` escolhemos o tipo `str`{.python} para representar a informação do tipo de combustível. Essa escolha é adequada? \pause

Não! Muitos valores válidos para `str`{.python} não correspondem a nenhum valor válido para a informação do tipo de combustível. \pause

Como proceder nesse caso? \pause Vamos definir um novo tipo onde apenas os valores para álcool e gasolina são válidos.


# Tipos enumerados

Em um **tipo enumerado** todos os valores válidos para o tipo são enumerados explicitamente. \pause

A forma geral para definir tipos enumerados é

\small

```python
from enum import Enum, auto

class NomeDoTipo(Enum):
    VALOR1 = auto()
    ...
    VALORN = auto()
```

\pause

\normalsize

Vamos definir um tipo enumerado para representar o tipo de combustível.


# Definição do tipo `Combustivel`

\small

```python
class Combustivel(Enum):
    '''O tipo do combustivel em um abastecimento'''
    ALCOOL = auto()
    GASOLINA = auto()
```

\pause

\normalsize

`auto()` é utilizado para associar automaticamente um número com o valor da enumeração. \pause Se quisermos, podemos escolher um número explicitamente. \pause

Sempre vamos adicionar um comentário sobre o propósito do tipo, se necessário, adicionamos comentários para os valores da enumeração.


# Uso de tipo enumerado

Cada valor da enumeração tem dois atributos: `name` e `value`. \pause

<div class="columns">
<div class="column" width="48%">

\small

```python
>>> c = Combustivel.ALCOOL
>>> c
<Combustivel.ALCOOL: 1>
>>> c.value
1
>>> c.name
'ALCOOL'
```

</div>
<div class="column" width="48%">

\pause

\small

```python
>>> c = Combustivel.GASOLINA
>>> c
<Combustivel.GASOLINA: 2>
>>> c.value
2
>>> c.name
'GASOLINA'
```

</div>
</div>


# Tipos enumerados

Assim como uma variável do tipo `bool`{.python} só pode armazenar os valores `True`{.python} e `False`{.python}, uma variável do tipo `Combustivel` só pode armazenar o valor `Combustivel.ALCOOL` ou `Combustivel.GASOLINA`, se tentarmos atribuir um valor diferente, o `mypy` indicará um erro. \pause

\small

```python
c: Combustivel = "Alcool"
```

\pause

\normalsize

Erro

\small

```
error: Incompatible types in assignment (expression has type "str",
                                         variable has type "Combustivel")
```


# Quando usar tipos enumerados?

Quando usar tipos enumerados? \pause

Quando todos os valores válidos para o tipo podem ser nomeados. \pause

Por que utilizar tipos enumerados? \pause

Para expressar mais claramente o propósito do código e evitar a utilização de valores inválidos (como `'alcoo'`{.python} em uma variável string que representa o tipo do combustível).


# Revisão do projeto de `indica_combustivel`

\footnotesize

```python
def indica_combustivel(preco_alcool: float, preco_gasolina: float) -> Combustivel:
    '''
    Exemplos
    >>> indica_combustivel(4.00, 6.00).name
    'ALCOOL'
    >>> indica_combustivel(3.50, 5.00).name
    'ALCOOL'
    >>> indica_combustivel(4.00, 5.00).name
    'GASOLINA'
    '''
    if preco_alcool <= 0.7 * preco_gasolina:
        combustivel = Combustivel.ALCOOL
    else:
        combustivel = Combustivel.GASOLINA
    return combustivel
```


# Exemplo - Semáforo

Projete uma função que receba como entrada a cor atual de um semáforo de trânsito e devolva a próxima cor que será exibida (considere um semáforo com três cores: verde, amarelo e vermelho).

\pause

Análise \pause

- Determinar a próxima cor de um semáforo dado a cor atual \pause

Projeto de tipos de dados \pause

- Quais são as informações? \pause A cor do semáforo. \pause

- Como representar essa informação? \pause Com um tipo enumerado.


# Exemplo - Semáforo

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
from enum import Enum, auto

class Cor(Enum):
    '''O cor de um semáforo de trânsito'''
    VERDE = auto()
    VERMELHO = auto()
    AMARELO = auto()
```

\pause

```python
def proxima_cor(atual: Cor) -> Cor:
    '''
    Produz a próxima cor de uma semáfaro que
    está na cor *atual*.
    Exemplos
    >>> proxima_cor(Cor.VERDE).name
    'AMARELO'
    >>> proxima_cor(Cor.AMARELO).name
    'VERMELHO'
    >>> proxima_cor(Cor.VERMELHO).name
    'VERDE'
    '''
```
</div>
<div class="column" width="48%">

\pause

Implementação

\pause

São três formas de resposta, então usamos seleção com uma condição para cada forma.

\pause

\scriptsize

```python
def proxima_cor(atual: Cor) -> Cor:
    if atual == Cor.VERDE:
        proxima = Cor.AMARELO
    elif atual == Cor.AMARELO:
        proxima = Cor.VERMELHO
    elif atual == Cor.VERMELHO:
        proxima = Cor.VERDE
    return proxima
```

\pause

\small

Verificação: \pause Ok. \pause

Revisão: \pause Ok.

</div>
</div>


# Exemplo - tempo

Em um determinado programa é necessário exibir para o usuário o tempo que uma operação demorou. Esse tempo está disponível em segundos, mas exibir essa informação em segundos para o usuário pode não ser interessante, afinal, ter uma noção razoável de tempo para 14678 segundos é difícil! \pause

a) Projete uma função que converta uma quantidade de segundos para uma quantidade de horas, minutos e segundos equivalentes. \pause

b) Projete uma função que converta uma quantidade de horas, minutos e segundos em uma string amigável para o usuário (algo como 1 hora, 10 minutos e 2 segundos). A string não deve conter valores zeros.


# Exemplo - tempo - parte a

Análise \pause

- Converter uma quantidade de segundos em horas, minutos e segundos. \pause

Definição de tipos de dados \pause

- Os segundos da entrada serão representados com números inteiros positivos \pause

- A saída são três números inteiros positivos... \pause As funções em Python só podem produzir um valor de saída, como proceder? \pause Vamos criar um novo tipo de dado que agrupa esses três valores.



# Tipos de dados

Vamos relembrar alguns tipos de dados que utilizamos até agora:

- Tipos atômicos pré-definidos na linguagem: `int, float, bool, str`{.python}
- Tipos enumerados definidos pelo usuário: `Combustivel`, `Cor`

\pause

Os tipos atômicos têm esse nome porque não são compostos por partes. \pause

Podemos criar novos tipos agregando partes (campos) de tipos já existentes. \pause

Uma forma de fazer isso é através de tipos compostos (estruturas).


# Tipos compostos

Um **tipo composto** é um tipo de dado composto por um conjunto fixo de campos com nome e tipo.

\pause

A forma geral para definir um tipo composto é

\small

```python
from dataclasses import dataclass

@dataclass
class NomeDoTipo:
    campo1: Tipo1
    ...
    campon: TipoN
```


# Tipos compostos

\small

Podemos definir um novo tipo para representar um tempo da seguinte forma

```python
@dataclass
class Tempo:
    '''
    Representa o tempo de duração de um evento.
    horas, minutos e segundos devem ser positivos.
    minutos e segundos devem ser menores que 60.
    '''
    horas: int
    minutos: int
    segundos: int
```

\pause

Assim como para definição de tipos enumerados, sempre vamos adicionar um comentário sobre o propósito do tipo.


# Tipos compostos

Para inicializar uma variável de um tipo composto, chamamos o construtor (função) para o tipo e especificamos os valores dos campos na ordem que eles foram declarados. \pause

\small

```python
>>> t1: Tempo = Tempo(0, 20, 10)
>>> t1
Tempo(horas=0, minutos=20, segundos=10)
```

\pause

```python
>>> # A anotação do tipo é opcional
>>> t2 = Tempo(4, 0, 20)
>>> t2
Tempo(horas=4, minutos=0, segundos=20)
```


# Tipos compostos

Como valores do tipo `Tempo` são compostos de outros valores (campos), podemos acessar e alterar cada campo de forma separada. \pause

<div class="columns">
<div class="column" width="48%">
\small

```python
>>> t1 = Tempo(0, 20, 10)
>>> t1.segundos
10
>>> t1.minutos
20
>>> t1.horas
0
```

\pause

</div>
<div class="column" width="48%">

\small

```python
>>> t1.horas = 3
>>> t1
Tempo(horas=3, minutos=20, segundos=10)
>>> # Podemos deixar o valor em um
>>> # estado inconsistente...
>>> t1.segundos = 70
Tempo(horas=3, minutos=20, segundos=70)
```

</div>
</div>


# Especificação e implementação

<div class="columns">
<div class="column" width="55%">
\scriptsize

```python
def segundos_para_tempo(segundos: int) -> Tempo:
    '''
    Converte a quantidade *segundos* para o tempo
    equivalente em horas, minutos e segundos.
    A quantidade de segundos e minutos da resposta
    é sempre menor que 60.
    Requer que segundos seja não negativo.

    Exemplos
    >>> # 160 // 60 -> 2 mins, 160 % 60 -> 40 segs
    >>> segundos_para_tempo(160)
    Tempo(horas=0, minutos=2, segundos=40)
    >>> # 3760 // 3600 -> 1 hora
    >>> # 3760 % 3600 -> 160 segundos que sobraram
    >>> # 160 // 60 -> 2 mins, 160 % 60 -> 40 segs
    >>> segundos_para_tempo(3760)
    Tempo(horas=1, minutos=2, segundos=40)
    '''
    return Tempo(0, 0, 0)
```

</div>
<div class="column" width="45%">
\pause

Quantas formas de resposta nós temos? \pause Podemos generalizar para apenas uma forma que utiliza uma sequência de instruções. \pause

\scriptsize

```python
def segundos_para_tempo(int segundos) -> Tempo:
    h = segundos / 3600
    # segundos que não foram
    # convertidos para hora
    restantes = segundos % 3600
    m = restantes / 60
    s = restantes % 60
    return Tempo(h, m, s)
```

\pause

\normalsize

Verificação: ok \pause

Revisão: ok
</div>
</div>


# Dados compostos

Quando utilizamos dados compostos? \pause

Quando a informação consiste de dois ou mais itens que juntos descrevem uma entidade.


# Exemplo - tempo - parte b

Em um determinado programa é necessário exibir para o usuário o tempo que uma operação demorou. Esse tempo está disponível em segundos, mas exibir essa informação em segundos para o usuário pode não ser interessante, afinal, ter uma noção razoável de tempo para 14678 segundos é difícil!

a) Projete uma função que converta uma quantidade de segundos para uma quantidade de horas, minutos e segundos equivalentes.

b) Projete uma função que converta uma quantidade de horas, minutos e segundos em uma string amigável para o usuário (algo como 1 hora, 10 minutos e 2 segundos). A string não deve conter valores zeros.

\pause

Agora vamos fazer o item b.


# Especificação

\scriptsize

```python
def tempo_para_string(t: Tempo) -> str:
    '''
    Converte *t* em uma mensagem para o usuário. Cada componente de *t* aparece
    com a sua unidade, mas se o valor do componente for 0, ele não aparece na
    mensagem. Os componentes são separados com "e" ou "," respeitando as regras
    do Português. Se *t* for Tempo(0, 0, 0), devolve "0 segundo(s)".
    '''
    return ''
```

# Especificação

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
>>> # horas == 0 and minutos == 0
>>> tempo_para_string(Tempo(0, 0, 0))
'0 segundo(s)'
>>> tempo_para_string(Tempo(0, 0, 1))
'1 segundo(s)'
>>> tempo_para_string(Tempo(0, 0, 10))
'10 segundo(s)'

>>> # horas == 0 and minutos != 0 \
>>> #            and segundos != 0
>>> tempo_para_string(Tempo(0, 1, 20))
'1 minuto(s) e 20 segundo(s)'

>>> # horas == 0 and minutos != 0 \
>>> #            and segundos == 0
>>> tempo_para_string(Tempo(0, 2, 0))
'2 minuto(s)'
```

</div>
<div class="column" width="48%">

\scriptsize

```python
>>> # horas != 0 and minutos != 0 and segundos != 0
>>> tempo_para_string(Tempo(1, 2, 1))
'1 hora(s), 2 minuto(s) e 1 segundo(s)'

>>> # horas != 0 and minutos == 0 and segundos != 0
>>> tempo_para_string(Tempo(4, 0, 25))
'4 hora(s) e 25 segundo(s)'

>>> # horas != 0 and minutos != 0 and segundos == 0
>>> tempo_para_string(Tempo(2, 4, 0))
'2 hora(s) e 4 minuto(s)'

>>> # horas != 0 and minutos == 0 and segundos == 0
>>> tempo_para_string(Tempo(3, 0, 0))
'3 hora(s)'
```

</div>
</div>


# Implementação

Quantas formas de resposta existem? \pause 7! \pause Então temos que usar seleção. \pause

A implementação direta usando as condições de cada forma fica com exercício. \pause

A implementação a seguir usa condições aninhadas.

#

<div class="columns">
<div class="column" width="48%">
Implementação

\tiny

```python
def tempo_para_string(Tempo t) -> str:
    h = str(t.horas) + ' hora(s)'
    m = str(t.minutos) + ' minuto(s)'
    s = str(t.segundos) + ' segundo(s)'
    # Temos 7 formas distintas
    if t.horas > 0:
        if t.minutos > 0:
            if t.segundos > 0:
                msg = h + ', ' + m + ' e ' + s
            else:
                msg = h + ' e ' + m
        elif t.segundos > 0:
            msg = h + ' e ' + s
        else:
            msg = h
    elif t.minutos > 0:
        if t.segundos > 0:
            msg = m + ' e ' + s
        else:
            msg = m
    else:
        msg = s
    return msg
```

</div>
<div class="column" width="48%">
\pause

Implementação alternativa

\tiny

```python
def tempo_para_string(Tempo t) -> str:
    # usado para separar cada componente de t
    sep = ''
    msg = ''
    if t.segundos > 0:
        sep = ' e '
        msg = str(t.segundos) + ' segundo(s)'

    if t.minutos > 0:
        msg = str(t.minutos) + ' minuto(s)' + sep + msg
        if t.segundos > 0:
            sep = ', '
        else:
            sep = ' e '

    if t.horas > 0:
        msg = str(t.horas) + ' hora(s)' + sep + msg

    if msg == '':
        msg = '0 segundo(s)'

    return msg
```
</div>
</div>


# Exercício

Modifique a especificação e implementação da função anterior para que o plural dos componentes fique de acordo com o Português.


# Exemplo - Loteria

Em um jogo de loteria os apostadores fazem apostas escolhendo 6 números distintos entre 1 e 60. No sorteio são sorteados 6 números de forma aleatória. Os apostadores que acertam 4, 5 ou 6 números são contemplados com prêmios.

a) Projete uma função que verifique se um número está entre os sorteados.

b) Projete uma função que determine quantos números uma determinada aposta acertou.


# Exemplo - Loteria

Análise \pause

- Determinar se um número está entre 6 números sorteados.

- Determinar o número de acertos de uma aposta de 6 números sendo que 6 números foram sorteados; \pause

- Os números estão entre 1 e 60;

\pause

Definição de tipos de dados \pause

- Quais são as informações? \pause A aposta e os sorteados, as duas informações são compostas de 6 números. \pause

- Como representar a aposta de 6 números? E os 6 número sorteados? \pause Com um dado composto.


# Definição de tipos de dados

\scriptsize

```python
from dataclasses import dataclass

@dataclass
class SeisNumeros:
    '''Coleção de 6 números distintos entre 1 e 60.'''
    a: int
    b: int
    c: int
    d: int
    e: int
    f: int
```

\pause

\normalsize

As apostas e os números sorteados serão representados pela estrutura `SeisNumeros`. \pause

Vamos fazer a especificação da primeira função.


# Exemplo - Loteria - Especificação `sorteado`

\scriptsize

```python
def sorteado(n: int, sorteados: SeisNumeros) -> bool:
    '''
    Produz True se *n* é um dos números
    em *sorteados*. False caso contrário.
    '''
    return False
```

\pause

\normalsize

Quantos exemplos precisamos? \pause 7, `n` igual a cada um dos sorteados e `n` diferentes de todos.


# Exemplo - Loteria - Especificação `sorteado`

<div class="columns">
<div class="column" width="60%">
\scriptsize

```python
def sorteado(n: int, sorteados: SeisNumeros) -> bool:
    '''
    >>> sorteados = SeisNumeros(1, 7, 10, 40, 41, 60)
    >>> sorteado(1, sorteados)
    True
    >>> sorteado(7, sorteados)
    True
    >>> sorteado(10, sorteados)
    True)
    >>> sorteado(40, sorteados)
    True
    >>> sorteado(41, sorteados)
    True
    >>> sorteado(60, sorteados)
    True
    >>> sorteado(2, sorteados)
    False
    '''
    return False
```

</div>
<div class="column" width="40%">
\pause
Quantas formas de respostas nós temos? \pause Duas, ou a resposta é `True`{.python} ou a resposta é `False`{.python}. \pause

Então precisamos usar seleção. Qual a condição para a resposta `True`{.python}? \pause

\scriptsize

```python
n == sorteados.a or \
    n == sorteados.b or \
    n == sorteados.c or \
    n == sorteados.d or \
    n == sorteados.e or \
    n == sorteados.f
```

\pause

\normalsize

Agora podemos fazer a implementação.
</div>
</div>


# Exemplo - Loteria - implementação `sorteado`

<div class="columns">
<div class="column" width="60%">
\scriptsize

```python
def sorteado(n: int, sorteados: SeisNumeros) -> bool:
    if n == sorteados.a or \
        n == sorteados.b or \
        n == sorteados.c or \
        n == sorteados.d or \
        n == sorteados.e or \
        n == sorteados.f:
        em_sorteados = True
    else:
        em_sorteados = False
    return em_sorteados
```

</div>
<div class="column" width="40%">
\pause
Verificação: ok \pause

Revisão: podemos melhorar o código? \pause Sim! \pause

O código de `sorteado` tem forma:

\scriptsize

```python
if condição:
    r = True
else:
    r = False
return r
```

\normalsize

\pause

que pode ser simplificada para

\scriptsize

```python
return condição
```
</div>
</div>


# Exemplo - Loteria - implementação `sorteado`

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def sorteado(n: int,
             sorteados: SeisNumeros)
             -> bool:
    return n == sorteados.a or \
        n == sorteados.b or \
        n == sorteados.c or \
        n == sorteados.d or \
        n == sorteados.e or \
        n == sorteados.f
```

</div>
<div class="column" width="48%">
\pause
Podemos fazer uma implementação alternativa? \pause Sim, fazendo seleções aninhadas uma condição por vez: \pause

Se `n == a`{.python}, então a resposta é `True`{.python}; \pause

Senão, quais podem ser as respostas? \pause `True`{.python} ou `False`{.python} \pause, então precisamos de outra seleção: \pause

- Se `n == b`{.python}, então a resposta é `True`{.python}; \pause
- Senão, quais podem ser as respostas? \pause `True`{.python} ou `False`{.python}...

</div>
</div>


# Exemplo - Loteria - implementação `sorteado`

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def sorteado(n: int,
             sorteados: SeisNumeros)
             -> bool:
    if n == sorteados.a:
        em_sorteados = True
    elif n == sorteados.b:
        em_sorteados = True
    elif n == sorteados.c:
        em_sorteados = True
    elif n == sorteados.d:
        em_sorteados = True
    elif n == sorteados.e:
        em_sorteados = True
    elif n == sorteados.f:
        em_sorteados = True
    else:
        em_sorteados = False
    return em_sorteados
```

</div>
<div class="column" width="48%">
\pause
Podemos fazer outra implementação? \pause Sim!
</div>
</div>


# Forma de implementação de função

Até agora vimos três formas de implementar uma função: \pause

- Direta, uma única expressão (ou sequência de expressões): `custo_viagem`, `massa_tubo_ferro`, `segundos_para_tempo`, `sorteado` - uma versão, etc. \pause

- Seleção direta, seleção com uma condição para cada forma de resposta: `maximo`, `ajusta_numero`, `indica_combustivel`, `maximo3` - uma versão, `sorteado` - uma versão, etc. \pause

- Seleção aninhada, seleção aninhada até determinar a forma da resposta: `maximo3` - uma versão, `tempo_para_string`, `sorteado` - uma versão, etc. \pause

Agora veremos uma nova forma de implementação: a forma incremental.


# Abordagem incremental

Na **abordagem incremental**, iniciamos a resposta com um valor e vamos atualizando a resposta conforme o processamento avança, no final, temos a resposta da função. \pause

Vamos aplicar esse abordagem para implementar a função `sorteado`. \pause

A resposta que queremos é se o número `n` está entre os `sorteados`. \pause O que precisamos? \pause

- Um valor inicial para a resposta; \pause

- Uma forma de atualizar a resposta conforme analisamos a entrada. \pause

Começamos a resposta com `False`{.python}, \pause se `n == a`{.python} mudamos a resposta pra `True`{.python}, \pause se `n == b`{.python} mudamos a resposta pra `True`{.python}, \pause e assim por diante.


# Exemplo - Loteria - implementação `sorteado`

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def sorteado(n: int,
             sorteados: SeisNumeros)
             -> bool:
    em_sorteados = False
    if n == sorteados.a:
        em_sorteados = True
    if n == sorteados.b:
        em_sorteados = True
    if n == sorteados.c:
        em_sorteados = True
    if n == sorteados.d:
        em_sorteados = True
    if n == sorteados.e:
        em_sorteados = True
    if n == sorteados.f:
        em_sorteados = True
    return em_sorteados
```

</div>
<div class="column" width="48%">
\pause
Observe que, apesar do código ser semelhante ao da implementação anterior, o processo pelo qual escrevemos esse código foi diferente. \pause

Além disso, essa forma vai nos permitir um tipo de simplificação que veremos em breve. \pause

Agora podemos ir para a segunda função do problema da loteria: determinar o número de acertos de uma aposta.

</div>
</div>


# Exemplo - Loteria - Especificação `num_acertos`

\scriptsize

```python
def numero_acertos(aposta: SeisNumeros, sorteados: SeisNumeros) -> int:
    '''
    Determina quantos números da *aposta* estão em *sorteados*.
    Exemplos
    >>> numero_acertos(SeisNumeros(1, 2, 3, 4, 5, 6), SeisNumeros(8, 12, 20, 41, 52, 57))
    0
    >>> numero_acertos(SeisNumeros(8, 2, 3, 4, 5, 6), SeisNumeros(8, 12, 20, 41, 52, 57))
    1
    >>> numero_acertos(SeisNumeros(8, 12, 3, 4, 5, 6), SeisNumeros(8, 12, 20, 41, 52, 57))
    2
    >>> numero_acertos(SeisNumeros(8, 12, 20, 4, 5, 6), SeisNumeros(8, 12, 20, 41, 52, 57))
    3
    >>> numero_acertos(SeisNumeros(8, 12, 20, 41, 5, 6), SeisNumeros(8, 12, 20, 41, 52, 57))
    4
    >>> numero_acertos(SeisNumeros(8, 12, 20, 41, 52, 6), SeisNumeros(8, 12, 20, 41, 52, 57))
    5
    >>> numero_acertos(SeisNumeros(8, 12, 20, 41, 52, 57), SeisNumeros(8, 12, 20, 41, 52, 57))
    6
    '''
    return 0
```


# Exemplo - Loteria - Especificação `num_acertos`

Que estratégia nós usamos para calcular as respostas dos exemplos? Ou ainda, que estratégia podemos utilizar para implementar a função? \pause A estratégia incremental! \pause

O que precisamos para implementar a função usando a estratégia incremental? \pause

- Um valor inicial para a resposta; \pause

- Uma forma de atualizar a resposta conforme analisamos a entrada.


# Exemplo - Loteria - Especificação `num_acertos`

Começamos o número de acertos com zero. \pause

Depois verificamos se o primeiro número está entre os sorteados, se sim, aumentamentos os acertos em 1. \pause

Depois verificamos se o segundo número está entre os sorteados, se sim, aumentamentos os acertos em 1. \pause

E assim com o restante dos números. \pause

No final, temos a quantidade de acertos.


# Implementação

\scriptsize

```python
def numero_acertos(aposta: SeisNumeros, sorteados: SeisNumeros) -> int:
    acertos = 0
    if sorteado(aposta.a, sorteados):
        acertos = acertos + 1
    if sorteado(aposta.b, sorteados):
        acertos = acertos + 1
    if sorteado(aposta.c, sorteados):
        acertos = acertos + 1
    if sorteado(aposta.d, sorteados):
        acertos = acertos + 1;
    if sorteado(aposta.e, sorteados):
        acertos = acertos + 1
    if sorteado(aposta.f, sorteados):
        acertos = acertos + 1
    return acertos
```


# Verificação e Revisão

Verificação: \pause ok \pause

Revisão: \pause assim como para a função `sorteado`, o código parece repetitivo... \pause Como resolver essa questão? \pause

Usando instrução de repetição! \pause Vamos continuar na próxima aula.
