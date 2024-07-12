---
# vim: set spell spelllang=pt_br:
title: Outras formas de repetição
---


# Introdução

Agora veremos outras formas de repetição diferente do "para cada".


# Exemplo - Índice máximo

Projete uma função que encontre o índice (posição) da primeira ocorrência do valor máximo de uma lista não vazia de números.


# Exemplo - Índice máximo - Especificação

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def indice_maximo(lst: list[int]) -> int:
    '''
    Encontra o índice da primeira ocorrência
    do valor máximo de *lst*.
    Requer que *lst* seja não vazia.
    Exemplos
    >>> indice_maximo([5])
    0
    >>> indice_maximo([5, 6])
    1
    >>> indice_maximo([5, 6, 6])
    1
    >>> indice_maximo([5, 6, 6, 8])
    3
    '''
    return 0
```

\pause

\normalsize

Qual estratégia podemos utilizar? \pause A incremental. \pause

</div>
<div class="column" width="48%">

Qual o resultado queremos calcular? \pause O índice `imax` do máximo de `lst`. \pause

Com qual valor iniciamos `imax`? \pause `0`{.python}. \pause

Se estamos analisando um elemento `n` de `lst`, como atualizamos `imax`? \pause Não tem como! \pause Precisamos atualizar `imax`, que é um índice, mas só temos acesso ao elemento `n`. \pause

Como procedemos?

</div>
</div>


# Exemplo - Índice máximo - Especificação

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def indice_maximo(lst: list[int]) -> int:
    '''
    Encontra o índice da primeira ocorrência
    do valor máximo de *lst*.
    Requer que *lst* seja não vazia.
    Exemplos
    >>> indice_maximo([5])
    0
    >>> indice_maximo([5, 6])
    1
    >>> indice_maximo([5, 6, 6])
    1
    >>> indice_maximo([5, 6, 6, 8])
    3
    '''
    return 0
```

\normalsize

Qual estratégia podemos utilizar? A incremental.

</div>
<div class="column" width="48%">

Vamos calcular duas coisas simultaneamente, o índice `imax` do máximo e o índice `i` do elemento atual. \pause

Com qual valor iniciamos `imax` e `i`? \pause `0`{.python}. \pause

Se estamos analisando um número `n` de `lst`, como atualizamos `imax` e `i`? \pause Atribuímos `i` para `imax` se `n > lst[imax]`{.pause} \pause e `i` é incrementado de `1`{.python}.
</div>
</div>


# Exemplo - Índice máximo - Implementação

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def indice_maximo(lst: list[int]) -> int:
    assert len(lst) != 0
    i = 0
    imax = 0
    for n in lst:
        if n > lst[imax]:
            imax = i
        i = i + 1
    return imax
```

\pause

\normalsize

Revisão: \pause não está claro qual é a relação entre `n` e `i`... \pause

Podemos mudar `n` para `lst[i]`{.python}.

\pause

</div>
<div class="column" width="48%">
\scriptsize

```python
def indice_maximo(lst: list[int]) -> int:
    assert len(lst) != 0
    i = 0
    imax = 0
    for n in lst:
        if lst[i] > lst[imax]:
            imax = i
        i = i + 1
    return imax
```

\pause

\normalsize

Revisão: \pause `n` não é mais utilizado... \pause

A questão é que não queremos mais acessar os elementos da lista diretamente, queremos usar um índice para acessar os elementos. Vamos utilizar uma variante do “para cada” que é mais apropriada para essa situação.
</div>
</div>


# Para cada no intervalo

Podemos escrever o "para cada" com a seguinte forma alternativa: \pause

\small

```python
for var in range(inicio, fim):
    instruções
```

\pause

\normalsize

O funcionamento dessa forma é a seguinte: \pause

- `var` é inicializado com `inicio` \pause
- Se `var < fim`, as `instruções` são executadas, `var` é incrementado de `1`{.python} e esse processo é executado novamente \pause
- Senão, o "para cada" é finalizado \pause

O valor `inicio` pode ser omitido, nesse caso, `var` é inicializado com `0`{.python}. \pause

Vamos ver um exemplo.


# Para cada no intervalo

<div class="columns">
<div class="column" width="48%">

\footnotesize

```python
def soma(lst: list[int]) -> int:
    soma = 0
    for n in lst:
        soma = soma + n
    return soma
```

\pause

</div>
<div class="column" width="48%">

\footnotesize

```python
def soma(lst: list[int]) -> int:
    soma = 0
    for i in range(len(lst)):
        soma = soma + lst[i]
    return soma
```

</div>
</div>

\ 

\pause

Qual das duas soluções é mais simples? \pause A da esquerda. \pause

Quando usamos o "para cada no intervalo"? \pause

Quando estamos interessados em um intervalo dos elementos da lista (que pode ser todos) junto com seus índices



# Exemplo - Índice máximo - Implementação

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def indice_maximo(lst: list[int]) -> int:
    assert len(lst) != 0
    i = 0
    imax = 0
    for n in lst:
        if lst[i] > lst[imax]:
            imax = i
        i = i + 1
    return imax
```

\normalsize

\pause

Como nesse caso estamos interessados nos índices dos elementos, então é mais adequado utilizar o "para cada no intervalo". \pause

Além disso, não precisamos analisar o primeiro elemento. \pause

</div>
<div class="column" width="48%">

\scriptsize

```python
def indice_maximo(lst: list[int]) -> int:
    assert len(lst) != 0
    imax = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[imax]:
            imax = i
    return imax
```

\pause

\normalsize

\ 

Qual das duas soluções é mais simples? \pause A da direita.

</div>
</div>



# Exemplo: verificação de ordem

Projete uma função que verifique se os elementos de uma lista estão em ordem não decrescente.


# Exemplo: verificação de ordem

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def nao_decrescente(lst: list[int]) -> bool:
    '''
    Produz True se os elementos de lst estão em
    ordem não decrescente, False caso contrário.
    Exemplos
    >>> nao_decrescente([])
    True
    >>> nao_decrescente([4])
    True
    >>> nao_decrescente([4, 6])
    True
    >>> nao_decrescente([4, 2])
    False
    >>> nao_decrescente([4, 6, 6])
    True
    >>> nao_decrescente([4, 6, 5])
    False
    >>> nao_decrescente([4, 3, 5])
    False
    '''
```

\pause

</div>
<div class="column" width="48%">

\small

Como proceder com a implementação dessa função? \pause Usando a estratégia incremental. \pause

Como calculamos manualmente a resposta dos exemplos? \pause Comparando cada elemento com o próximo (ou anterior). \pause

Essa forma parece diferente... \pause Antes era necessário analisar um elemento da lista a cada iteração, agora temos que analisar dois elementos. \pause

Como proceder nesse caso? \pause

Vamos implementar a função para uma lista de 5 elementos usando repetição física de código e depois vamos transformar a repetição física em repetição lógica.

</div>
</div>


# Exemplo: verificação de ordem

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def nao_decrescente(lst: list[int]) -> bool:
    assert len(lst) == 5
    # Assumimos com em_ordem = True que lst
    # está em ordem não decrescente, se
    # encontramos um elemento "fora de ordem",
    # mudamos em_ordem para False.
    em_ordem = True
    if lst[0] > lst[1]:
        em_ordem = False
    if lst[1] > lst[2]:
        em_ordem = False
    if lst[2] > lst[3]:
        em_ordem = False
    if lst[3] > lst[4]:
        em_ordem = False
    return em_ordem
```

\pause


</div>
<div class="column" width="48%">

\small

Vamos transformar essa repetição física de código em uma repetição lógica. \pause

Devemos usar o "para cada" ou o "para cada no intervalo"? \pause Precisamos dos índices, então "para cada no intervalo". \pause

Qual é o intervalo? \pause `range(0, 4)`{.python} ou `range(1, 5)`{.python}. \pause

\scriptsize

```python
def nao_decrescente(lst: list[int]) -> bool:
    assert len(lst) == 5
    em_ordem = True
    for i in range(1, 5):
        if lst[i - 1] > lst[i]:
            em_ordem = False
    return em_ordem
```
</div>
</div>


# Exemplo: verificação de ordem

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def nao_decrescente(lst: list[int]) -> bool:
    assert len(lst) == 5
    em_ordem = True
    for i in range(1, 5):
        if lst[i - 1] > lst[i]:
            em_ordem = False
    return em_ordem
```

\pause

\normalsize

Como **generalizar** esse código para que ele funcione para listas de qualquer tamanho? \pause Modificando o limite do intervalo de `5`{.python} para `len(lst)`{.python}. \pause


</div>
<div class="column" width="48%">

\scriptsize

```python
def nao_decrescente(lst: list[int]) -> bool:
    em_ordem = True
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            em_ordem = False
    return em_ordem
```

\pause

\normalsize

Revisão: \pause mesmo encontrando valores "fora de ordem" a repetição continua e analisa toda a lista...

</div>
</div>


# Enquanto

Usamos o "para cada" e o "para cada no intervalo" quando queremos analisar todos os elementos (de um intervalo) da lista. \pause

Nesse tipo de repetição a condição de parada é analisar todos os elementos (do intervalo) da lista. \pause

Para situações que precisamos de um processo incremental que depende de uma condição mais geral utilizamos o `while`{.python} (enquanto em inglês).


# Enquanto

A forma geral do `while`{.python} é: \pause

```python
while condição:
    instruções
```

\pause

O funcionamento do `while`{.python} é o seguinte: \pause

- A `condição` é avaliada \pause

- Se ela for `True`{.python}, as `instruções` são executadas e o processo se repete \pause

- Senão, o `while`{.python} termina


# Enquanto - Exemplo

<div class="columns">
<div class="column" width="48%">

\footnotesize

```python
def nao_decrescente(lst: list[int]) -> bool:
    em_ordem = True
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            em_ordem = False
    return em_ordem
```

\pause

\small

Vamos reescrever o corpo da função usando o `while`{.python}.

</div>
<div class="column" width="48%">

\footnotesize

\pause

```python
def nao_decrescente(lst: list[int]) -> bool:
    em_ordem = True
    i = 1
    while i < len(lst):
        if lst[i - 1] > lst[i]:
            em_ordem = False
        i = i + 1
    return em_ordem
```

\pause

</div>
</div>

\ 


\small

O código está mais simples? \pause Não, \pause o controle do índice `i`, que era automático, agora é feito explicitamente. \pause

Resolvemos o problema do processamento continuar após um elemento fora de ordem ser encontrado? \pause Não... \pause Como podemos resolver esse problema? \pause Alterando a condição do `while`{.python} para prosseguir apenas se `em_ordem` for `True`{.python}.


# Enquanto - Exemplo

<div class="columns">
<div class="column" width="48%">

\footnotesize


```python
# Versão com for
def nao_decrescente(lst: list[int]) -> bool:
    em_ordem = True
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            em_ordem = False
    return em_ordem
```

</div>
<div class="column" width="48%">

\footnotesize

```python
# Versão com enquanto
def nao_decrescente(lst: list[int]) -> bool:
    em_ordem = True
    i = 1
    while i < len(lst):
        if lst[i - 1] > lst[i]:
            em_ordem = False
        i = i + 1
    return em_ordem
```

\pause

</div>
</div>

\footnotesize

\vspace{-0.7cm}


```python
# Versão com enquanto e ajuste da condição
def nao_decrescente(lst: list[int]) -> bool:
    em_ordem = True
    i = 1
    while i < len(lst) and em_ordem:
        if lst[i - 1] > lst[i]:
            em_ordem = False
        i = i + 1
    return em_ordem
```


# Enquanto - execução passo a passo

<div class="columns">
<div class="column" width="48%">

\footnotesize

```{.python .number-lines}
def nao_decrescente(lst: list[int]) -> bool:
    em_ordem = True
    i = 1
    while i < len(lst) and em_ordem:
        if lst[i - 1] > lst[i]:
            em_ordem = False
        i = i + 1
    return em_ordem

nao_decrescente([1, 3, 3, 2, 7, 8])
```

</div>
<div class="column" width="48%">
Qual é a ordem que as linhas são executadas? \pause

\small

10 \pause

2 (`em_ordem = True`{.python}) \pause

3 (`i = 1`{.python}) \pause

4 \pause, 5 \pause, 7 (`i = 2`{.python}) \pause

4 \pause, 5 \pause, 7 (`i = 3`{.python}) \pause

4 \pause, 5 \pause, 6 (`em_ordem = False`{.python}) \pause, 7 (`i = 4`{.python}) \pause

4 \pause

8 (produz `False`{.python})\pause

10

</div>
</div>


# Implementação de funções com `while`{.python}

Para implementar uma função com o método incremental usando o `while`{.python} precisamos determinar as mesmas três coisas \pause

- Quais valores queremos calcular; \pause
- Como os valores são inicializados; \pause
- Como os valores são atualizados; \pause

e mais \pause

- Qual é a condição da repetição.


# Exemplo: palíndromo

Projete uma função que verifique se uma lista de inteiros é palíndromo, isto é, tem os mesmos elementos quanto vistos da direita para esquerda ou da esquerda para a direita.


# Exemplo: palíndromo

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def palindromo(lst: list[int]) -> bool:
    '''Produz True se *lst* é palíndromo, isto
    é, tem os mesmos elementos quando vistos
    da direira para esquerda e da esquerda
    para direita. Produz False caso contrário.
    >>> palindromo([])
    True
    >>> palindromo([4])
    True
    >>> palindromo([1, 1])
    True
    >>> palindromo([1, 2])
    False
    >>> palindromo([1, 2, 1])
    True
    >>> palindromo([1, 5, 5, 1])
    True
    >>> palindromo([1, 5, 1, 5])
    False
    '''
```

\pause

</div>
<div class="column" width="48%">

\small

Como proceder com a implementação dessa função? \pause Usando a estratégia incremental. \pause

Como calculamos manualmente as respostas dos exemplos? \pause Comparando o primeiro com o último, o segundo com o penúltimo, etc. \pause

Vamos implementar a função para uma lista de 7 elementos usando repetição física de código e depois vamos transformar a repetição física em repetição lógica.

</div>
</div>


# Exemplo: palíndromo

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def palindromo(lst: list[int]) -> bool:
    '''
    >>> palindromo([3, 2, 1, 7, 5, 2, 3])
    False
    '''
    assert len(lst) == 7
    eh_palindromo = True
    if lst[0] != lst[6]:
        eh_palindromo = False
    if lst[1] != lst[5]:
        eh_palindromo = False
    if lst[2] != lst[4]:
        eh_palindromo = False
    return eh_palindromo
```

\pause

</div>
<div class="column" width="48%">

\small

Como transformar essa repetição física de código em uma repetição lógica? \pause

Nas transformações que fizemos em `sorteado`, `numero_acertos` e `nao_decrescente` introduzimos uma repetição diretamente. \pause

Nesse exemplo parece que isso é mais complicado pois o código que se repete é menos parecido. \pause

Vamos deixar os trechos que se repetem mais parecidos introduzindo variáveis para os índices.

</div>
</div>


# Exemplo: palíndromo

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def palindromo(lst: list[int]) -> bool:
    '''
    >>> palindromo([3, 2, 1, 7, 5, 2, 3])
    False
    '''
    assert len(lst) == 7
    eh_palindromo = True
    if lst[0] != lst[6]:
        eh_palindromo = False
    if lst[1] != lst[5]:
        eh_palindromo = False
    if lst[2] != lst[4]:
        eh_palindromo = False
    return eh_palindromo
```

</div>
<div class="column" width="48%">

\scriptsize

```python
def palindromo(lst: list[int]) -> bool:
    assert len(lst) == 7
    eh_palindromo = True
    i = 0
    j = 6
    if lst[i] != lst[j]:
        eh_palindromo = False


    if lst[i] != lst[j]:
        eh_palindromo = False


    if lst[i] != lst[j]:
        eh_palindromo = False


    return eh_palindromo
```

</div>
</div>

\pause

Como os índice `i` e `j` devem ser atualizados?


# Exemplo: palíndromo

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def palindromo(lst: list[int]) -> bool:
    '''
    >>> palindromo([3, 2, 1, 7, 5, 2, 3])
    False
    '''
    assert len(lst) == 7
    eh_palindromo = True
    if lst[0] != lst[6]:
        eh_palindromo = False
    if lst[1] != lst[5]:
        eh_palindromo = False
    if lst[2] != lst[4]:
        eh_palindromo = False
    return eh_palindromo
```

</div>
<div class="column" width="48%">

\scriptsize

```python
def palindromo(lst: list[int]) -> bool:
    assert len(lst) == 7
    eh_palindromo = True
    i = 0
    j = 6
    if lst[i] != lst[j]:
        eh_palindromo = False
    i = i + 1
    j = j - 1
    if lst[i] != lst[j]:
        eh_palindromo = False
    i = i + 1
    j = j - 1
    if lst[i] != lst[j]:
        eh_palindromo = False
    i = i + 1
    j = j - 1
    return eh_palindromo
```

</div>
</div>

Como os índice `i` e `j` devem ser atualizados? Somando e subtraindo 1.


# Exemplo: palíndromo

<div class="columns">
<div class="column" width="40%">

\scriptsize

```python
def palindromo(lst: list[int]) -> bool:
    assert len(lst) == 7
    eh_palindromo = True
    i = 0
    j = 6
    if lst[i] != lst[j]:
        eh_palindromo = False
    i = i + 1
    j = j - 1
    if lst[i] != lst[j]:
        eh_palindromo = False
    i = i + 1
    j = j - 1
    if lst[i] != lst[j]:
        eh_palindromo = False
    i = i + 1
    j = j - 1
    return eh_palindromo
```

\pause

</div>
<div class="column" width="56%">

\footnotesize

Agora podemos transformar essa repetição física de código para repetição lógica. \pause

Os valores que são calculados, a inicialização e a atualização já estão claras no código. O que precisamos determinar? \pause A condição de repetição\pause, que é `i < j`{.python} ` and eh_palindromo`{.python}. \pause

\scriptsize

```python
def palindromo(lst: list[int]) -> bool:
    assert len(lst) == 7
    eh_palindromo = True
    # começa dos extremos
    i = 0
    j = 6
    while i < j and eh_palindromo:
        if lst[i] != lst[j]:
            eh_palindromo = False
        # vai para o centro
        i = i + 1
        j = j - 1
    return eh_palindromo
```

</div>
</div>


# Exemplo: palíndromo

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def palindromo(lst: list[int]) -> bool:
    assert len(lst) == 7
    eh_palindromo = True
    # começa dos extremos
    i = 0
    j = 6
    while i < j and eh_palindromo:
        if lst[i] != lst[j]:
            eh_palindromo = False
        # vai para o centro
        i = i + 1
        j = j - 1
    return eh_palindromo
```

\pause

\small

Como **generalizar** esse código para que ele funcione para listas de qualquer tamanho? \pause Modificando a inicialização `j = 6`{.python} para `j = len(lst) - 1`{.python}. \pause

</div>
<div class="column" width="48%">

\scriptsize

```python
def palindromo(lst: list[int]) -> bool:
    eh_palindromo = True
    # começa dos extremos
    i = 0
    j = len(lst) - 1
    while i < j and eh_palindromo:
        if lst[i] != lst[j]:
            eh_palindromo = False
        # vai para o centro
        i = i + 1
        j = j - 1
    return eh_palindromo
```

</div>
</div>


# Repetição sem arranjos

Até agora todos os problemas que utilizamos a abordagem incremental (repetição) envolviam uma lista de valores. \pause

Agora veremos o uso da abordagem incremental em problemas que não envolvem uma lista de valores.


# Exemplo: fatorial

O fatorial de um número natural $n$ é o produto de todos os números naturais de $1$ até $n$, isto é, $1 \times \cdots \times (n - 1) \times n$. Projete uma função que determine o fatorial de um número $n$.


# Exemplo: fatorial

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def fatorial(n: int) -> int:
    '''
    Calcula o produto de todos os naturais
    entre 1 e n, isto é, 1 * ... * (n - 1) * n.
    Exemplos
    >>> fatorial(0)
    1
    >>> fatorial(1)
    1
    >>> fatorial(2)
    2
    >>> fatorial(3)
    6
    >>> fatorial(4)
    24
    '''
    return 0
```

\pause


</div>
<div class="column" width="48%">

Como fazer a implementação? \pause Generalizando soluções específicas! \pause

Como determinar de forma incremental o fatorial de 5? \pause

\scriptsize

```python
def fatorial(n: int) -> int:
    assert n == 5
    fat = 1
    fat = fat * 2
    fat = fat * 3
    fat = fat * 4
    fat = fat * 5
    return fat
```

</div>
</div>


# Exemplo: fatorial

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def fatorial(n: int) -> int:
    assert n == 5
    fat = 1
    fat = fat * 2
    fat = fat * 3
    fat = fat * 4
    fat = fat * 5
    return fat
```

\pause

\normalsize

Que construção de repetição podemos utilizar para transformar essa repetição física de código em uma repetição lógica? \pause

O "para cada no intervalo". \pause E qual é o intervalo? \pause `range(2, 6)`{.python}

\pause

</div>
<div class="column" width="48%">

\scriptsize

```python
def fatorial(n: int) -> int:
    assert n == 5
    fat = 1
    for i in range(2, 6):
        fat = fat * i
    return fat
```

\pause

\normalsize

Como **generalizar** esse código para que ele funcione para qualquer valor de `n`? \pause Alterando o limite do intervalo de `6`{.python} para `n + 1`{.python}. \pause

\scriptsize

```python
def fatorial(n: int) -> int:
    fat = 1
    for i in range(2, n + 1):
        fat = fat * i
    return fat
```

</div>
</div>


# Exemplo: número primo

Um número inteiro positivo $n$ é primo se ele tem exatamente dois divisores distintos, $1$ e $n$. Projete uma função que verifique se um número inteiro positivo é primo.


# Exemplo: número primo

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def primo(n: int) -> bool:
    '''
    Produz True se *n* é um número primo,
    isto é, tem exatamente dois divisores
    distintos, 1 e ele mesmo. Produz False
    se *n* não é primo.
    Exemplos
    >>> primo(1) # 1
    False
    >>> primo(2) # 1 2
    True
    >>> primo(3) # 1 3
    True
    >>> primo(5) # 1 5
    True
    >>> primo(8) # 1 2 4 8
    False
    >>> primo(11) # 1 11
    True
    '''
```

</div>
<div class="column" width="48%">
\pause

Como fazer a implementação? \pause Generalizando soluções específicas! \pause

Como determinar de forma incremental se o número 5 é primo? \pause

\scriptsize

```python
def primo(n: int) -> bool:
    assert n == 5
    num_divisores = 0
    if n % 1 == 0:
        num_divisores = num_divisores + 1
    if n % 2 == 0:
        num_divisores = num_divisores + 1
    if n % 3 == 0:
        num_divisores = num_divisores + 1
    if n % 4 == 0:
        num_divisores = num_divisores + 1
    if n % 5 == 0:
        num_divisores = num_divisores + 1
    return num_divisores == 2
```

</div>
</div>


# Exemplo: número primo

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def primo(n: int) -> bool:
    assert n == 5
    num_divisores = 0
    if n % 1 == 0:
        num_divisores = num_divisores + 1
    if n % 2 == 0:
        num_divisores = num_divisores + 1
    if n % 3 == 0:
        num_divisores = num_divisores + 1
    if n % 4 == 0:
        num_divisores = num_divisores + 1
    if n % 5 == 0:
        num_divisores = num_divisores + 1
    return num_divisores == 2
```

\small

\pause

Que construção de repetição podemos utilizar para transformar essa repetição física de código em uma repetição lógica? \pause

</div>
<div class="column" width="48%">

\small

O "para cada no intervalo". \pause E qual é o intervalo? \pause `range(1, 6)`{.python} \pause

\scriptsize

```python
def primo(n: int) -> bool:
    assert n == 5
    num_divisores = 0
    for i in range(1, 6):
        if n % i == 0:
            num_divisores = num_divisores + 1
    return num_divisores == 2
```

\small

Como **generalizar** esse código para que ele funcione para qualquer valor de `n`? \pause Alterando o limite do intervalo de `6`{.python} para `n + 1`{.python}.

</div>
</div>


# Exemplo: número primo

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def primo(n: int) -> bool:
    num_divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            num_divisores = num_divisores + 1
    return num_divisores == 2
```

\pause

\small

Revisão: \pause quando `num_divisores` fica maior que 2 a repetição pode ser interrompida.

\pause

\scriptsize

```python
def primo(n: int) -> bool:
    num_divisores = 0
    i = 1
    while i < n + 1 and num_divisores <= 2:
        if n % i == 0:
            num_divisores = num_divisores + 1
        i = i + 1
    return num_divisores == 2
```

\pause

</div>
<div class="column" width="48%">

\small

Revisão: \pause `1`{.python} e `n`{.python} são sempre divisores de `n`, além disso, nenhum divisor de `n` (exceto `n`), é maior que `n // 2`{.python}. \pause Vamos verificar se não existe nenhum divisor de `n` no intervalo de `2`{.python} a `n // 2`{.python}. \pause

\scriptsize

```python
def primo(n: int) -> bool:
    num_divisores = 0
    i = 2
    while i < n // 2 and num_divisores == 0:
        if n % i == 0:
            num_divisores = num_divisores + 1
        i = i + 1
    return num_divisores == 0
```

\pause

\small

Verificação: \pause a função falha para `n = 1`{.python}... \pause

Vamos alterar o `return`{.python} para `n != 1 and num_divisores == 0`{.python}.
</div>
</div>


# Exemplo: número primo

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def primo(n: int) -> bool:
    num_divisores = 0
    i = 2
    while i < n // 2 and num_divisores == 0:
        if n % i == 0:
            num_divisores = num_divisores + 1
        i = i + 1
    return n != 1 and num_divisores == 0
```

\pause

\footnotesize

Revisão: \pause `num_divisores` só pode assumir dois valores: `0`{.python} ou `1`{.python}. \pause Então vamos mudar para `bool`{.python}.

\pause

\scriptsize

```python
def primo(n: int) -> bool:
    eh_primo = True
    i = 2
    while i < n // 2 and eh_primo:
        if n % i == 0:
            eh_primo = False
        i = i + 1
    return n != 1 and eh_primo
```

</div>
<div class="column" width="48%">

\pause

\small

Revisão: \pause `eh_primo` não diz de fato se é primo pois ainda depende da condição `n != 1`{.python}. \pause

\scriptsize

```python
def primo(n: int) -> bool:
    eh_primo = n != 1
    i = 2
    while i < n // 2 and eh_primo:
        if n % i == 0:
            eh_primo = False
        i = i + 1
    return eh_primo
```

</div>
</div>


# Matrizes

O tipo `list`{.python} (arranjo) que vimos é unidimensional. Algumas linguagens suportam arranjos com mais dimensões. Os arranjos bidimensionais são chamados de matrizes. \pause

O Python não suporta nativamente matrizes, mas podemos usar lista de listas como matrizes.


# Matrizes

Por exemplo, para representar matriz

$$
A = \left [
  \begin{array}{cccc}
  1 & 4 & 2 & 8 \\
  -1 & 0 & 9 & 1 \\
  4 & 7 & -2 & 0
  \end{array}
  \right ]
$$

em Python fazemos \pause

\small

```python
>>> m: list[list[int]] = [[1, 4, 2, 8], [-1, 0, 9, 1], [4, 7, -2, 0]]
```


# Matrizes

Usamos as operações que já conhecemos para acessar e modificar a matriz

\small

```python
>>> m: list[list[int]] = [[1, 4, 2, 8], [-1, 0, 9, 1], [4, 7, -2, 0]]
>>> m[1]
[-1, 0, 9, 1]
>>> m[1][2]
9
>>> len(m)
3
>>> len(m[0])
4
>>> m[2][1] = 0
>>> m
[[1, 4, 2, 8], [-1, 0, 9, 1], [4, 0, -2, 0]]
```


# Exemplo: matriz nula

Projete uma função que receba dois números inteiros positivos, $m$ e $n$, e crie uma matriz $A_{m \times n}$, com $m$ linhas e $n$ colunas, com todos os elementos zeros.


# Exemplo: matriz nula

<div class="columns">
<div class="column" width="56%">
\scriptsize

```{.python .number-lines}
def cria_matriz_nula(m: int, n: int) -> list[list[int]]:
    '''
    Cria uma matriz nula com *m* linhas e *n* colunas.

    Requer que m > 0 e n > 0.

    Exemplos
    >>> cria_matriz_nula(2, 3)
    [[0, 0, 0], [0, 0, 0]]
    '''
    a = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(0)
        a.append(linha)
    return a
```

\pause

\footnotesize

Para a chamada `cria_matriz_nula(2, 3)`{.python}, qual é a ordem que as linhas são executas?

\pause

</div>
<div class="column" width="42%">

\small

11 (`m = []`{.python}) \pause

12 (`i = 0`{.python}) \pause

13 (`linha = []`{.python}) \pause

14 (`j = 0`{.python}), \pause 15 (`linha = [0]`{.python}), \pause 14 (`j = 1`{.python}), \pause 15 (`linha = [0, 0]`{.python}), \pause 14 (`j = 2`{.python}), \pause 15 (`linha = [0, 0, 0]`{.python}), \pause 14 (`j = 3`{.python}) \pause

16 (`m = [[0, 0, 0]]`), \pause 12 (`i = 1`{.python}) \pause

13 (`linha = []`{.python}) \pause

14 (`j = 0`{.python}), \pause 15 (`linha = [0]`{.python}), \pause 14 (`j = 1`{.python}), \pause 15 (`linha = [0, 0]`{.python}), \pause 14 (`j = 2`{.python}), \pause 15 (`linha = [0, 0, 0]`{.python}), \pause 14 (`j = 3`{.python}) \pause


16 (`m = [[0, 0, 0], [0, 0, 0]]`), \pause 12 (`i = 2`{.python}), \pause 17

</div>
</div>


# Exemplos: matriz regular

Uma matriz é regular quando todos as linhas têm a mesma quantidade de elementos. Projete uma função que verifique se uma matriz é regular.

\pause

Feito em sala.

\pause

Daqui para frente só vamos utilizar matrizes regulares.


# Exemplos: quantidade de zeros

Projete uma função que conte a quantidade de elementos nulos de uma matriz.

\pause

Feito em sala.


# Exemplos: matriz transposta

Projete uma função que crie a matriz transposta de uma data matriz.

\pause

Feito em sala.


# Conjuntos

Vimos o tipo `list`{.python}, pré-definido em Python, que serve para representar uma sequência de valores.

\pause

Um conjunto em Python é semelhante a uma lista, mas não contém elementos repetidos, a ordem dos elementos não é definida, os elementos não são indexados e os elementos precisam ser imutáveis.


# Conjuntos

<div class="columns">
<div class="column" width="48%">
\footnotesize

```python
>>> # conjunto vazio
>>> a: set[int] = set()
>>> a
{}
```

\pause

```python
>>> # inicialização com elementos
>>> a = {10, 4}
>>> a
{10, 4}
```

\pause

```python
>>> # adição de elementos
>>> a.add(3)
>>> a.add(4)
>>> a
{10, 3, 4}
```

\pause

</div>
<div class="column" width="48%">
\footnotesize

```python
>>> # pertinência
>>> 4 in a
True
>>> 20 in a
False
```

\pause

```python
>>> # tamanho
>>> len(a)
3
```

\pause

```python
>>> # iteração
>>> soma = 0
>>> for e in a:
...     soma = soma + e
...
>>> soma
17
```

</div>
</div>


<!--

# Como projetar funções que processam arranjos usando o "para cada"

Quando precisamos processar um arranjo, geralmente queremos calcular valores de forma incremental, analisando um por um os elementos do arranjo. \pause

Esses valores podem ser o resultado final da função ou podem ser usados em outras instruções para determinar o resultado final da função. \pause

Então, para escrever o código que processa os elementos de um arranjo com o "para cada" precisamos responder três perguntas \pause

1) Quais variáveis (valores) queremos calcular? \pause
2) Como as variáveis são inicializadas? \pause
3) Como as variáveis são atualizadas? \pause

Para responder cada pergunta, usamos os exemplos e perguntas auxiliares.


# Como projetar funções que processam arranjos usando o "para cada"

a) Quais variáveis (valores) queremos calcular? \pause

   Podemos calcular o resultado final da função apenas analisando os elementos do arranjo, sem precisar fazer nada depois? \pause

   Se sim, então esse é o valor que queremos calcular. \pause

   Se não, temos que pensar em valores que podem nos ajudar com a resposta da função e esses são os valores que queremos calcular. \pause

   Em ambos os casos, criamos variáveis para armazenar esses valores.


# Como projetar funções que processam arranjos usando o "para cada"

b) Como as variáveis são inicializadas? \pause

   Se o arranjo não tiver nenhum elemento, qual é o valor esperado para as variáveis? \pause

   Use esses valores para inicializar as variáveis.


# Como projetar funções que processam arranjos usando o "para cada"

c) Como as variáveis são atualizadas? \pause

   Pegue alguns exemplos e suponha que o "para cada" já tenha processado de forma correta todos os elementos do arranjo, exceto o último, e determine os valores que as variáveis devem ter. \pause

   Em seguida, considere que o último elemento está sendo processado e determine quais operações são necessárias para modificar os valores das variáveis para que elas fiquem com o valor final esperado. \pause

   Generalize e escreva o código para fazer essas operações.



# Eleições

Uma eleição é realizada com apenas dois candidatos. Cada eleitor pode votar ou no primeiro candidato, ou no segundo candidato, ou ainda, votar em branco. O candidato que tiver mais votos ganha a eleição. Se os votos em branco forem mais do que 50% do total de votos, novas eleições devem ser convocadas. Projete uma função que receba como entrada uma lista não vazia de votos e determine qual foi o resultado da eleição. Dica: deseje uma função auxilar que conte votos de um tipo especificado por parâmetro.


# Análise

Determinar o resultado de uma eleição. \pause

- O voto pode ser em um de dois candidatos ou em branco; \pause
- Se mais que 50% dos votos forem brancos ou se os candidatos tiverem o mesmo número de votos, é necessário uma nova eleição; \pause
- Se não for necessário uma nova eleição, ganha quem tiver mais votos.


# Definição dos tipos de dados

\footnotesize

```cpp

// Os votos serão representados por vector<Voto>.

// Um voto em uma eleição.
enum Voto {
    Candidato1,
    Candidato2,
    Branco,
};

// O resultado de uma eleição.
enum ResultadoEleicao {
    Venceu1,
    Venceu2,
    NovasEleicoes,
};
```


# Especificação

\scriptsize

```cpp
// Apura o resultado da eleicao considerando os votos no arranjo votos.
// - Produz NovasEleicoes se mais do que 50% do total de votos for branco ou se a
// quantidade de votos do Candidato1 for igual ao do Candidato2.
// - Senão, produz Venceu1 se o Candidato1 teve mais votos ou Venceu2 se o
// Candidato2 teve mais votos.
ResultadoEleicao apura_eleicao(vector<Voto> votos)
{
    return NovasEleicoes;
}

examples
{
    check_expect(apura_eleicao({Candidato1, Candidato2, Candidato1, Branco}), Venceu1);
    check_expect(apura_eleicao({Candidato2, Candidato2, Candidato1, Branco}), Venceu2);
    check_expect(apura_eleicao({Candidato2, Candidato1, Candidato1, Candidato2}), NovasEleicoes);
    check_expect(apura_eleicao({Candidato1, Candidato1, Branco, Branco}), Venceu1);
    check_expect(apura_eleicao({Candidato2, Candidato2, Branco, Branco}), Venceu2);
    check_expect(apura_eleicao({Candidato1, Candidato2, Branco, Branco}), NovasEleicoes);
    check_expect(apura_eleicao({Candidato2, Candidato2, Branco, Branco, Branco}), NovasEleicoes);
}
```


# Implementação

Vamos seguir a dica do enunciado e desejar a função `conta_votos`, que conta um determinado tipo de voto.

\scriptsize

```cpp
ResultadoEleicao apura_eleicao(vector<Voto> votos) {
    int num_votos1 = conta_votos(votos, Candidato1);
    int num_votos2 = conta_votos(votos, Candidato2);
    int num_brancos = conta_votos(votos, Branco);

    ResultadoEleicao resultado;
    if (num_brancos > votos.size() / 2) {
        resultado = NovasEleicoes;
    } else if (num_votos1 > num_votos2) {
        resultado = Venceu1;
    } else if (num_votos2 > num_votos1) {
        resultado = Venceu2;
    } else {
        resultado = NovasEleicoes;
    }
    return resultado;
}
```


# Lista de pendências

Adicionamos `conta_votos` na lista de pendências e fazemos o projeto da função.

\pause

\scriptsize

```cpp
// Conta quantos votos no arranjo votos é igual ao alvo.
int conta_votos(vector<Voto> votos, Voto alvo)
{
    return 0;
}

examples
{
    vector<Voto> votos = {Candidato2, Candidato1, Branco, Candidato1, Candidato2, Candidato1};
    check_expect(conta_votos(votos, Candidato1), 3);
    check_expect(conta_votos(votos, Candidato2), 2);
    check_expect(conta_votos(votos, Branco), 1);
}
```


# Implementação

<div class="columns">
<div class="column" width="48%">
1) Quais variáveis (valores) queremos calcular? \pause A quantidade de votos iguais ao alvo. \pause
2) Como as variáveis são inicializadas? \pause A quantidade é inicializada com 0. \pause
3) Como as variáveis são atualizadas? \pause A quantidade é atualizada em 1 quanto o elemento atual for igual ao alvo. \pause
</div>
<div class="column" width="48%">
\scriptsize
```cpp
int conta_votos(vector<Voto> votos, Voto alvo)
{
    int num = 0;
    for (Voto voto : votos) {
        if (voto == alvo) {
            num = num + 1;
        }
    }
    return num;
}
```
</div>
</div>

\pause

Verificação: \pause Ok. \pause

Revisão: \pause Ok.


# Execução do programa

O programa está pronto! Agora podemos compilar e testar. \pause

Quando o programa é executado ele fica esperando os ditos serem digitados, um por linha. Para sinalizar que não serão digitados mais ditos, pressionamos "crtl + d". \pause

Compile e teste o programa dessa forma. \pause Qual a sua impressão sobre a "facilidade" de uso do programa?


# Redirecionamento de entrada

Parece repetitivo ter que digitar os ditos, afinal, estes ditos já foram coletados e estão salvos em algum arquivo. \pause

Quando temos um arquivo `.txt`, podemos utilizar o seu conteúdo como entrada do nosso programa. Nesse caso, tudo o que está no arquivo aparece para o programa como se tivesse sido digitado pelo usuário. \pause

Se o arquivo com os ditos chama `"ditos.txt"`, podemos utilizar o conteúdo do arquivo como entrada para o programa da seguinte forma \pause

```
./ditos < ditos.txt
```

\pause

O símbolo `<` é interpretado pelo shell como redirecionamento da entrada, então, ao invés de esperar o usuário digitar a entrada para o programa, o shell utiliza o conteúdo do arquivo como entrada do programa.


# Redirecionamento de saída

Da mesma forma que existe redirecionamento de entrada, também existe redirecionamento de saída. \pause

Quando utilizamos redirecionamento de saída, ao invés do resultado do programa ser exibido na tela, ele é salvo em um arquivo. \pause

Para ler a entrada do arquivo `"ditos.txt"` e salvar o resultado no arquivo `"ditos-unicos.txt"`, executamos \pause

```
./ditos < ditos.txt > ditos-unicos.txt
```

\pause

O símbolo `>` é interpretado pelo shell como redirecionamento da saída.


# Momento de apreciação

\pause

Aprecie esse momento. \pause Temos um programa completo que pode ser utilizado por um usuário final para realizar uma tarefa útil!


# Exercício

Projete uma função que separe as "partes" de uma string usando um espaço como delimitador.


# Especificação

\scriptsize

```cpp
// Produz uma lista das "partes" de s usando um espaço como delimitador.
vector<string> separa(string s)
{
    return {};
}

examples
{
    check_expect(separa(""), (vector<string> {}));
    check_expect(separa("casa"), (vector<string> {"casa"}));
    check_expect(separa("Seu Jorge cantou a musica."),
                 (vector<string> {"Seu", "Jorge", "cantou", "a", "musica."}));
}
```


# Implementação

Como fazer a implementação? \pause Vamos precisar de uma repetição, \pause mas qual tipo? \pause Diferente das repetições que fizemos anteriormente, esta não depende de uma "coleção" de valores, então vamos usar o "enquanto". \pause

E como fazer a repetição? \pause Vamos tentar generalizar a solução de alguns exemplos específicos.


# Implementação

\scriptsize

```cpp
string s = "Seu Jorge cantou a musica.";
vector<string> palavras = {};
```

\pause

```cpp
s.find(" ", 0); // a partir do indice 0 ("S"), encontra o indice do primeiro " ", que é 3
palavras.push_back(s.substr(0, 3 - 0)); // "Seu"
```

\pause

```cpp
s.find(" ", 3 + 1); // a partir do indice 4 ("J"), encontra o indice do primeiro " ", que é 9
palavras.push_back(s.substr(4, 9 - 4)); // "Jorge"
```

\pause

```cpp
s.find(" ", 9 + 1); // a partir do indice 10 ("c"), encontra o indice do primeiro " ", que é 16
palavras.push_back(s.substr(10, 16 - 10)); // "cantou"
```

\pause

```cpp
s.find(" ", 16 + 1); // a partir do indice 17 ("a"), encontra o indice do primeiro " ", que é 18
palavras.push_back(s.substr(17, 18 - 17)); // "a"
```

\pause

```cpp
s.find(" ", 18 + 1); // a partir do indice 18 ("m"), não tem mais " ", produz -1.
palavras.push_back(s.substr(17, 26 - 19)); // "musica." 26 é o tamanho de s
```


# Implementação

Quais informações (variáveis) são necessárias a cada iteração? \pause O índice de início (`inicio`{.cpp}) e o valor produzido pela busca do espaço (`fim`{.cpp}). \pause

Como as variáveis são inicializadas? \pause `inicio = 0`{.cpp}. \pause

O que precisa ser feito a cada iteração? \pause Calcular `fim`, extrair e adicionar a substring em `palavras`. \pause O que mais? \pause Atualizar o `inicio` para a próxima iteração! \pause

Todas as iterações são iguais? \pause Não, a última iteração é diferente. \pause Como identificar se estamos na última iteração? \pause `find` produz `-1`{.cpp}. \pause

Como o `inicio` é atualizado? \pause No caso geral, `inicio = fim + 1`{.cpp}. \pause E no último caso? \pause `inicio = s.length()`{.cpp}. \pause

Qual a condição para o laço continuar a execução? \pause `inicio < s.length()`{.cpp}


# Implementação

\scriptsize

```cpp
// Separa uma string usando um espaço como delimitador.
vector<string> separa(string s)
{
    vector<string> palavras = {};
    int inicio = 0;
    int fim;
    while (inicio < s.length()) {
        fim = s.find(" ", inicio);
        if (fim != -1) {
            palavras.push_back(s.substr(inicio, fim - inicio));
            inicio = fim + 1;
        } else {
            palavras.push_back(s.substr(inicio, s.length() - inicio));
            inicio = s.length();
        }
    }
    return palavras;
}
```

\pause

\small

Podemos melhorar? \pause Sim! \pause Como `fim` é usado apenas dentro do laço, mudamos o local da declaração.


# Exercício

Modifique a função `separa` de maneira que a string seja separada por um ou mais espaços:

\scriptsize

```cpp
check_expect(separa("mais   de  um "), (vector<string> { "mais", "de", "um" }));
```

-->
