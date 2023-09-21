---
# vim: set spell spelllang=pt_br:
# TODO: colocar uma revisão do método incremental antes do exemplo da soma
# TODO: separar em diversos arquivos
# TODO: adicionar definição de arranjo?
# TODO: apresentar de forma mais detalhada como identificar a forma da atualização
#       mostrar o arranjo, a resposta até então e a "chegada" do novo elemento
title: Repetição, arranjos e conjuntos
---

# Introdução

Vimos anteriormente que devemos definir uma estrutura para representar uma informação quando ela consiste de dois ou mais itens que juntos descrevem uma entidade. \pause

- No problema da conversão de segundos para horas, minutos e segundos, definimos a estrutura `Tempo`. \pause

- No problema da loteria, definimos a estrutura `SeisNumeros`.


# Introdução

O `Tempo` era composto de três "itens" que foram representados pelos campos horas, minutos e segundos. \pause

Já para `SeisNumeros` cada item não tinha uma interpretação particular, então não usamos nomes significativos, tivemos que "inventar" os nomes de `a`, ..., `f`. \pause

Como faríamos se ao invés de 6 itens tivéssemos 20? \pause E 1.000? \pause E 1.000.000? \pause Ou ainda, uma quantidade indefinida? \pause E como escrever o código para processar esse tipo de dado? \pause

Vamos ver como fazer essas coisas!


# Arranjos

Quando precisamos representar uma coleção de valores da mesma natureza (todos os itens são notas, nomes, pontos, janelas, etc), utilizamos arranjos. \pause

Os arranjos em Python são dinâmicos, isto é, podem mudar de tamanho, e são representados pelo tipo `list`{.python}. \pause

Vamos ver algumas operações com listas.


# Listas - inicialização e indexação

<div class="columns">
<div class="column" width="48%">

\footnotesize

```python
>>> # Inicialização
>>> x: list[int] = [9 + 1, 1, 7, 2]
>>> x
[10, 1, 7, 2]
```

\pause

```python
>>> # Lista vazia
>>> y = [] # ou list()
>>> y
[]
```

\pause

```python
>>> # Número de elementos
>>> len(x)
4
>>> len(y)
0
```

\pause

</div>
<div class="column" width="48%">

\footnotesize

```python
>>> # Indexação
>>> nomes = ['Maria', 'João', 'Paulo']
>>> nomes[1]
'João'
>>> # Acesso fora da faixa
>>> nomes[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

\pause

```python
>>> # Sublistas
>>> x = [4, 1, 5, 7, 3]
>>> x[:2]
[4, 1]
>>> x[2:]
[5, 7, 3]
```

</div>
</div>


# Listas - alteração, acréscimo e concatenação

<div class="columns">
<div class="column" width="45%">

\footnotesize

```python
>>> # Substituição de um elemento
>>> y = [4, 2]
>>> y[1] = 7
>>> y
[4, 7]
```

\pause

```python
>>> # Acrésimo de um elemento
>>> y.append(5) # list.append(y, 5)
>>> y
[4, 7, 5]
>>> y.append(3)
>>> y
[4, 7, 5, 3]
```

\pause

```python
>>> # Concatenação
>>> [1, 2, 3] + [4, 5]
[1, 2, 3, 4, 5]
```

\pause

</div>
<div class="column" width="55%">

Note que a função (método) `append` não produz valor de saída. \pause

Mas qual é a utilidade de uma função que não produz valor de saída!? \pause

Além de produzir uma saída, as funções podem ter **efeitos colaterais**, como por exemplo, modificar algum dos seus argumentos (função `append`), exibir algo na tela (função `print`{.python}), etc. \pause Uma função que produz uma saída também pode ter um efeito colateral, que o caso da função `input`{.python}. \pause

Então, utilizamos funções sem saída pelo efeito colateral que elas produzem.
</div>
</div>


# Valores mutáveis e imutáveis

Nós vimos que os valores do tipo lista e de tipos estruturas podem ser alterados depois que são criados, por isso são chamados de valores **mutáveis**. \pause

Já alguns valores não podem ser alterados, que é o caso dos valores dos tipos `int`{.python}, `float`{.python}, `bool`{.python} e `str`{.python}. \pause Chamamos esses valores de **imutáveis**. \pause

Essa diferenciação é importante na prática. Vamos discutir mais sobre isso em breve.


# Estruturas vs Arranjos

Tanto as estruturas quanto os arranjos são utilizados para representar informações com dois ou mais itens. \pause Então, como escolher qual utilizar? \pause

- Usamos estruturas quando cada item da informação tem uma interpretação particular (na estrutura `Tempo`, temos os componentes `horas`, `minutos` e `segundos`) \pause

- Usamos arranjos quando os itens da informação são da mesma natureza (todos são nomes, notas, etc)

\pause

No exemplo da loteria, os itens da aposta e dos sorteios têm a mesma natureza, são todos números, então devemos utilizar arranjos ao invés de estruturas. \pause Vamos alterar o código!


# Loteria

<div class="columns">
<div class="column" width="48%">
\footnotesize

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
\footnotesize

```python
def sorteado(n: int,
             sorteados: list[int])
             -> bool:
    em_sorteados = False
    if n == sorteados[0]:
        em_sorteados = True
    if n == sorteados[1]:
        em_sorteados = True
    if n == sorteados[2]:
        em_sorteados = True
    if n == sorteados[3]:
        em_sorteados = True
    if n == sorteados[4]:
        em_sorteados = True
    if n == sorteados[5]:
        em_sorteados = True
    return em_sorteados
```
</div>
</div>


# Loteria

<div class="columns">
<div class="column" width="48%">
\footnotesize

```python
def numero_acertos(aposta: SeisNumeros,
                   sorteados: SeisNumeros)
                   -> int:
    acertos = 0
    if sorteado(aposta.a, sorteados):
        acertos = acertos + 1
    if sorteado(aposta.b, sorteados):
        acertos = acertos + 1
    if sorteado(aposta.c, sorteados):
        acertos = acertos + 1
    if sorteado(aposta.d, sorteados):
        acertos = acertos + 1
    if sorteado(aposta.e, sorteados):
        acertos = acertos + 1
    if sorteado(aposta.f, sorteados):
        acertos = acertos + 1
    return acertos
```

</div>
<div class="column" width="48%">
\pause

\footnotesize

```python
def numero_acertos(aposta: list[int],
                   sorteados: list[int])
                   -> int:
    acertos = 0
    if sorteado(aposta[0], sorteados):
        acertos = acertos + 1
    if sorteado(aposta[1], sorteados):
        acertos = acertos + 1
    if sorteado(aposta[2], sorteados):
        acertos = acertos + 1
    if sorteado(aposta[3], sorteados):
        acertos = acertos + 1
    if sorteado(aposta[4], sorteados):
        acertos = acertos + 1
    if sorteado(aposta[5], sorteados):
        acertos = acertos + 1
    return acertos
```
</div>
</div>


# Loteria

E então, o código melhorou? \pause Ainda não! Ele continua repetitivo! \pause

Agora vamos trocar a repetição física do código por uma repetição lógica, usando uma nova estrutura de controle. Isso é possível porque os elementos de um arranjo têm a mesma natureza.


# Para cada

Em Python, uma das construções de repetição é o "para cada", que tem a seguinte forma geral \pause

\small

```python
for var in lista:
    instruções
```

\pause

\normalsize

O "para cada" funciona da seguinte maneira: \pause

- O primeiro valor de `lista` é atribuído para `var` e as `instruções` são executadas; \pause
- O segundo valor de `lista` é atribuído para `var` e as `instruções` são executadas; \pause
- ... \pause
- E assim por diante até que todos os valores de `lista` tenham sidos atribuídos para `var`. \pause

Ou seja, o "para cada" executa as mesmas instruções atribuindo cada valor de `lista` para `var`, por isso ele chama "para cada"!


# Para cada

<div class="columns">
<div class="column" width="48%">
\footnotesize

```python
def sorteado(n: int,
             sorteados: list[int])
             -> bool:
    em_sorteados = False
    if n == sorteados[0]:
        em_sorteados = True
    if n == sorteados[1]:
        em_sorteados = True
    if n == sorteados[2]:
        em_sorteados = True
    if n == sorteados[3]:
        em_sorteados = True
    if n == sorteados[4]:
        em_sorteados = True
    if n == sorteados[5]:
        em_sorteados = True
    return em_sorteados
```
</div>
<div class="column" width="48%">

\pause

Nesse código, queremos executar as mesmas instruções, uma vez para cada valor de `sorteados`, então, podemos utilizar o "para cada".

\pause

\footnotesize

```python
def sorteado(n: int,
             sorteados: list[int])
             -> bool:
    em_sorteados = False
    for x in sorteados:
        if n == x:
            em_sorteados = True
    return em_sorteados
```

</div>
</div>


# Para cada

<div class="columns">
<div class="column" width="48%">
\footnotesize

```python
def numero_acertos(aposta: list[int],
                   sorteados: list[int])
                   -> int:
    acertos = 0
    if sorteado(aposta[0], sorteados):
        acertos = acertos + 1
    if sorteado(aposta[1], sorteados):
        acertos = acertos + 1
    if sorteado(aposta[2], sorteados):
        acertos = acertos + 1
    if sorteado(aposta[3], sorteados):
        acertos = acertos + 1
    if sorteado(aposta[4], sorteados):
        acertos = acertos + 1
    if sorteado(aposta[5], sorteados):
        acertos = acertos + 1
    return acertos
```
</div>
<div class="column" width="48%">
\pause

Nesse código, queremos executar as mesmas instruções, uma vez para cada valor de `aposta`, então, podemos utilizar o "para cada".

\pause

\footnotesize

```python
def numero_acertos(aposta: list[int],
                   sorteados: list[int])
                   -> int:
    acertos = 0
    for n in aposta:
        if sorteado(n, sorteados):
            acertos = acertos + 1
    return acertos
```
</div>
</div>


# Execução passo a passo do "para cada"

<div class="columns">
<div class="column" width="48%">

\footnotesize

```{.python .number-lines}
def sorteado(n: int,
             sorteados: list[int])
             -> bool:
    em_sorteados = False
    for x in sorteados:
        if n == x:
            em_sorteados = True
    return em_sorteados

sorteado(35, [1, 7, 32, 35, 50, 51])
```

\pause

</div>
<div class="column" width="48%">

Vamos ver como a execução passo a passo funciona para o "para cada". \pause

Qual é a ordem que as linhas são executadas? \pause

\small

10, \pause 4 (`em_sorteados = False`{.python}) \pause

5 (`x = 1`{.python}), \pause 6, \pause

5 (`x = 7`{.python}), \pause 6, \pause

5 (`x = 32`{.python}), \pause 6, \pause

5 (`x = 35`{.python}), \pause 6, \pause 7 (`em_sorteados = True`{.python}), \pause

5 (`x = 50`{.python}), \pause 6, \pause

5 (`x = 51`{.python}), \pause 6, \pause

5 (identifica que não tem mais elementos), \pause 8 (devolve `True`{.python}), \pause 10.
</div>
</div>


# Como projetar funções que processam arranjos usando o "para cada"

No exemplo da loteria, vimos como uma repetição física de código pode ser substituída por uma repetição lógica. \pause

Em geral, não precisamos ter uma repetição física de código para depois trocarmos por uma repetição lógica, podemos projetar uma função usando uma repetição lógica diretamente. \pause

Vamos ver como fazer isso!


# Exemplo - Soma

Projete uma função que some os números de uma lista.


# Exemplo - Soma - Especificação

<div class="columns">
<div class="column" width="45%">
\footnotesize

```python
def soma(lst: list[int]) -> int:
    '''
    Soma os elementos de *lst*.
    Exemplos
    >>> soma([])
    0
    >>> soma([3])
    3
    >>> soma([3, 7])
    10
    >>> soma([3, 7, 2])
    12
    '''
    return 0
```

\pause

</div>
<div class="column" width="50%">
Qual abordagem podemos utilizar para implementar essa função? \pause A incremental. \pause

Na abordagem incremental, iniciamos o resultado com um valor, e vamos atualizando o resultado conforme processamos os dados de entrada, no final, temos o resultado da função. \pause

Qual é o resultado que queremos calcular? \pause A `soma` dos elementos de `lst`. \pause

Com qual valor iniciamos `soma`? \pause `0`{.python}. \pause

Se estamos analisando um número `n` de `lst`, como atualizamos `soma`? \pause Adicionando `n` em `soma`,  isto é, `soma = soma + x`{.python}.
</div>
</div>


# Exemplo - Soma - Implementação

<div class="columns">
<div class="column" width="48%">
\footnotesize

```{.python .number-lines}
def soma(lst: list[int]) -> int:
    soma = 0
    for n in lst:
        soma = soma + n
    return soma

soma([5, 1, 4])
```

</div>
<div class="column" width="48%">
Vamos exercitar mais uma vez a execução passo a passo. \pause

Qual é a ordem que as linhas são executadas? \pause

\footnotesize

7, \pause 2 (`soma = 0`{.python}), \pause

3 (`x = 5`{.python}), \pause 4 (`soma = 5`{.python}), \pause

3 (`x = 1`{.python}), \pause 4 (`soma = 6`{.python}), \pause

3 (`x = 4`{.python}), \pause 4 (`soma = 10`{.python}), \pause

3 (identifica que não tem mais elementos), \pause 5 (devolve `10`{.python}), \pause

7
</div>
</div>


# Exemplo - Strings que começam com A

Projete uma função que encontre as strings que começam com `'A'`{.python} de uma lista de strings.


# Exemplo - Strings que começam com A - Especificação

<div class="columns">
<div class="column" width="55%">
\scriptsize

```python
def encontra_comeca_a(lst: list[str]) -> list[str]:
    '''
    Encontra os elementos de *lst* que começam com 'A'.
    Exemplos
    >>> encontra_comeca_a([])
    []
    >>> encontra_comeca_a(['Ali'])
    ['Ali']
    >>> encontra_comeca_a(['Ali', 'ala'])
    ['Ali']
    >>> encontra_comeca_a(['Ali', 'ala', 'Alto'])
    ['Ali', 'Alto']
    >>> encontra_comeca_a(['Ali', 'ala', 'Alto', ''])
    ['Ali', 'Alto']
    '''
    return []
```

\pause

\normalsize

Qual abordagem podemos utilizar para implementar essa função? \pause A incremental. \pause
</div>
<div class="column" width="41%">

Qual é o resultado que queremos calcular? \pause A lista `comeca_a` com os elementos de `lst` que começam com `'A'`{.python}. \pause

Com qual valor iniciamos `comeca_a`? \pause `[]`{.python}. \pause

Se estamos analisando uma string `s` de `lst`, como atualizamos `comeca_a`? \pause Adicionando `s` em `comeca_a` (`comeca_a.append(s)`) se `s` começa com `'A'`{.python}, isto é, `s != '' and s[0] == 'A'`{.python}.
</div>
</div>


# Exemplo - Strings que começam com A - Implementação

\scriptsize

```python
def encontra_comeca_a(lst: list[str]) -> list[str]:
    '''
    Encontra os elementos de *lst* que começam com 'A'.
    Exemplos
    >>> encontra_comeca_a([])
    []
    >>> encontra_comeca_a(['Ali'])
    ['Ali']
    >>> encontra_comeca_a(['Ali', 'ala'])
    ['Ali']
    >>> encontra_comeca_a(['Ali', 'ala', 'Alto'])
    ['Ali', 'Alto']
    >>> encontra_comeca_a(['Ali', 'ala', 'Alto', ''])
    ['Ali', 'Alto']
    '''
    comeca_a = []
    for s in lst:
        if s != '' and s[0] == 'A':
            comeca_a.append(s)
    return comeca_a
```


# Exemplo - Máximo

Projete uma função que encontre o valor máximo em uma lista não vazia de inteiros.


# Exemplo - Máximo - Especificação

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def maximo(lst: list[int]) -> int:
    '''
    Encontra o valor máximo de *lst*.
    Requer que *lst* seja não vazia.
    Exemplos
    >>> maximo([2])
    2
    >>> maximo([2, 4])
    4
    >>> maximo([2, 4, 3])
    4
    >>> maximo([2, 4, 3, 7])
    7
    '''
    return 0
```

\pause

\normalsize

Qual abordagem podemos utilizar para implementar essa função? \pause A incremental. \pause
</div>
<div class="column" width="48%">

Qual é o resultado que queremos calcular? \pause O valor `maximo` de `lst`. \pause

Com qual valor iniciamos `maximo`? \pause `lst[0]`{.python}. \pause

Se estamos analisando um número `n` de `lst`, como atualizamos `maximo`? \pause Atribuindo `n` para `maximo` se `n > maximo`{.python}.
</div>
</div>


# Exemplo - Máximo - Implementação

\scriptsize

```python
def maximo(lst: list[int]) -> int:
    '''
    Encontra o valor máximo de *lst*.
    Requer que *lst* seja não vazia.
    Exemplos
    >>> maximo([2])
    2
    >>> maximo([2, 4])
    4
    >>> maximo([2, 4, 3])
    4
    >>> maximo([2, 4, 3, 7])
    7
    '''
    assert len(lst) != 0
    maximo = lst[0]
    for n in lst:
        if n > maximo:
            maximo = n
    return maximo
```


# Exemplo - Média tamanho strings

Projete uma função que calcule a média dos tamanhos das strings de uma lista não vazia de strings.


# Exemplo - Média tamanho strings - Especificação

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def media_tamanho(lst: list[str]) -> float:
    '''
    Calcula a média dos tamanhos das
    strings de *lst*.
    Requer que *lst* seja não vazia.
    Exemplos
    >>> media_tamanho(['casa'])
    4.0
    >>> media_tamanho(['casa', 'da'])
    3.0
    >>> media_tamanho(['casa', 'da', ''])
    2.0
    >>> media_tamanho(['casa', 'da', '', 'onça'])
    2.5
    '''
    return 0.0
```

\pause

\normalsize

Qual abordagem podemos utilizar para implementar essa função? \pause A incremental. \pause
</div>
<div class="column" width="48%">

Qual é o resultado que queremos calcular? \pause A `media` dos tamanhos das strings de `lst`. \pause

Com qual valor iniciamos a `media`? \pause `len(lst[0])`{.python}. \pause

Se estamos analisando o elemento `s` de `lst`, como atualizamos `media`? \pause Não tem com! \pause Se `media` é `100.0`{.python} e `s` é `'nova'`{.python}, qual é o novo valor de `media`? \pause Não temos informações suficientes para responder essa pergunta! \pause

Como procedemos então? \pause Como calculamos as respostas dos exemplos? \pause Primeiro calculamos a soma dos tamanhos das strings e depois a média.
</div>
</div>


# Emboço de solução

Quando a solução de um problema não pode ser expressa apenas com uma das formas que vimos até agora (direta, seleção direta, seleção aninhada e incremental), então podemos tentar uma combinação dessas formas. \pause

Para isso, primeiro criamos um **esboço de solução**, que é uma descrição em alto nível das etapas do processamento da função, e depois implementamos cada etapa usando a forma apropriada.


# Exemplo - Média tamanho strings - Implementação

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def media_tamanho(lst: list[str]) -> float:
    '''
    Calcula a média dos tamanhos das
    strings de *lst*.
    Requer que *lst* seja não vazia.
    Exemplos
    >>> media_tamanho(['casa'])
    4.0
    >>> media_tamanho(['casa', 'da'])
    3.0
    >>> media_tamanho(['casa', 'da', ''])
    2.0
    >>> media_tamanho(['casa', 'da', '', 'onça'])
    2.5
    '''
    # Calcular a soma dos tamanhos
    # Calcular a média
    return 0.0
```

</div>
<div class="column" width="48%">

\pause

**Soma dos tamanhos** \pause

Qual estratégia podemos utilizar? \pause A incremental. \pause Qual é o resultado que queremos calcular? \pause A `soma` dos tamanhos. \pause Com qual valor iniciamos `soma`? \pause `0`{.python}. \pause Se estamos analisando o elemento `s` de `lst`, como atualizamos `soma`? \pause `soma = soma + len(s)`{.python}. \pause

**Média** \pause

Como calculamos a média? \pause `soma / len(lst)`{.python}.

</div>
</div>


# Exemplo - Média tamanho strings - Implementação

\scriptsize

```python
def media_tamanho(lst: list[str]) -> float:
    assert len(lst) != 0

    # Soma dos tamanhos
    soma = 0
    for s in lst:
        soma = soma + len(s)

    # Média
    return soma / len(lst)
```


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


# Revisão

Quando utilizamos a abordagem incremental? \pause

Quando precisamos computar algo de forma incremental! \pause Ou seja, quando não é possível calcular a resposta de forma direta ou usando apenas seleção. \pause

O que precisamos determinar quando vamos utilizar a abordagem incremental? \pause

- Quais valores queremos calcular; \pause
- Como os valores são inicializados; \pause
- Como os valores são atualizados.


# Revisão

Por enquanto, vimos duas formas de implementar a abordagem incremental no Python: \pause

- O "para cada", que utilizamos quando estamos interessados em analisar todos os elementos de uma lista \pause
- O "para cada no intervalo", quando estamos interessados em analisar um intervalo dos elementos de uma lista (que pode ser todos) junto com seus índices


# Revisão

O quê pode nos impedir de utilizar a abordagem incremental? \pause

- Se não conseguirmos definir como os valores são inicializados \pause
- Se não conseguirmos definir como os valores são atualizados, que foi o caso de `media_tamanhos` \pause

Como procedemos nesses casos? \pause

Ao invés de computar a resposta final de forma incremental, definimos um esboço de solução, que calcula valores intermediários que serão utilizados para calcular o valor final. \pause

No caso de `media_tamanhos`, primeiro calculamos a soma dos tamanhos de forma incremental, e depois calculamos a média diretamente.


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
    assert n = 5
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
    assert n = 5
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
    assert n = 5
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
