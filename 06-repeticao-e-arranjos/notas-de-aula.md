---
# vim: set spell spelllang=pt_br:
# TODO: adicionar definição de arranjo?
# TODO: colocar uma revisão do método incremental antes do exemplo da soma
# TODO: apresentar de forma mais detalhada como identificar a forma da atualização
#       mostrar o arranjo, a resposta até então e a "chegada" do novo elemento
# TODO: adicionar exemplo de teste para respostas que são listas com enumerações e/ou estruturas
title: Repetição e arranjos
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

Agora vamos trocar a repetição física do código por uma repetição lógica usando uma nova estrutura de controle. Isso é possível porque os elementos de um arranjo têm a mesma natureza.


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


# Exemplo - soma

Projete uma função que some os números de uma lista.


# Exemplo - soma - especificação

<div class="columns">
<div class="column" width="45%">
\footnotesize

```python
def soma(lst: list[int]) -> int:
    '''Soma os elementos de *lst*.
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

Qual é o resultado que queremos computar? \pause A `soma` dos elementos de `lst`. \pause

Com qual valor iniciamos `soma`? \pause `0`{.python}. \pause

Se estamos analisando um elemento `n` de `lst`, como atualizamos `soma`? \pause Adicionando `n` em `soma`,  isto é, `soma = soma + n`{.python}.
</div>
</div>


# Exemplo - soma - implementação

<div class="columns">
<div class="column" width="45%">
\footnotesize

```python
def soma(lst: list[int]) -> int:
    '''Soma os elementos de *lst*.
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
    soma = 0
    for n in lst:
        soma = soma + n
    return soma
```

</div>
<div class="column" width="50%">
Qual abordagem podemos utilizar para implementar essa função? A incremental.

Na abordagem incremental, iniciamos o resultado com um valor, e vamos atualizando o resultado conforme processamos os dados de entrada, no final, temos o resultado da função.

Qual é o resultado que queremos computar? A `soma` dos elementos de `lst`.

Com qual valor iniciamos `soma`? `0`{.python}.

Se estamos analisando um elemento `n` de `lst`, como atualizamos `soma`? Adicionando `n` em `soma`,  isto é, `soma = soma + n`{.python}.
</div>
</div>


# Exemplo - soma - execução passo a passo

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

3 (`n = 5`{.python}), \pause 4 (`soma = 5`{.python}), \pause

3 (`n = 1`{.python}), \pause 4 (`soma = 6`{.python}), \pause

3 (`n = 4`{.python}), \pause 4 (`soma = 10`{.python}), \pause

3 (identifica que não tem mais elementos), \pause 5 (devolve `10`{.python}), \pause

7
</div>
</div>


# Exemplo - strings que começam com A

Projete uma função que encontre as strings que começam com `'A'`{.python} de uma lista de strings.


# Exemplo - strings que começam com A - especificação

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

Qual é o resultado que queremos computar? \pause A lista `comeca_a` com os elementos de `lst` que começam com `'A'`{.python}. \pause

Com qual valor iniciamos `comeca_a`? \pause `[]`{.python}. \pause

Se estamos analisando um elemento `s` de `lst`, como atualizamos `comeca_a`? \pause Adicionando `s` em `comeca_a` (`comeca_a.append(s)`) se `s` começa com `'A'`{.python}, isto é, `s != '' and s[0] == 'A'`{.python}.
</div>
</div>


# Exemplo - strings que começam com A - implementação

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


# Exemplo - máximo

Projete uma função que encontre o valor máximo em uma lista não vazia de inteiros.


# Exemplo - máximo - Especificação

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

</div>
<div class="column" width="48%">

Qual abordagem podemos utilizar para implementar essa função? \pause A incremental. \pause

Qual é o resultado que queremos computar? \pause O valor `maximo` de `lst`. \pause

Com qual valor iniciamos `maximo`? \pause `lst[0]`{.python}. \pause

Se estamos analisando um elemento `n` de `lst`, como atualizamos `maximo`? \pause Atribuindo `n` para `maximo` se `n > maximo`{.python}.
</div>
</div>


# Exemplo - máximo - implementação

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
    assert len(lst) != 0
    maximo = lst[0]
    for n in lst:
        if n > maximo:
            maximo = n
    return maximo
```



</div>
<div class="column" width="48%">

Qual abordagem podemos utilizar para implementar essa função? A incremental.

Qual é o resultado que queremos computar? O valor `maximo` de `lst`.

Com qual valor iniciamos `maximo`? `lst[0]`{.python}.

Se estamos analisando um elemento `n` de `lst`, como atualizamos `maximo`?  Atribuindo `n` para `maximo` se `n > maximo`{.python}.
</div>
</div>


# Exemplo - média tamanho strings

Projete uma função que calcule a média dos tamanhos das strings de uma lista não vazia de strings.


# Exemplo - média tamanho strings - especificação

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

Qual é o resultado que queremos computar? \pause A `media` dos tamanhos das strings de `lst`. \pause

Com qual valor iniciamos a `media`? \pause Não está claro. \pause

Se estamos analisando o elemento `s` de `lst`, como atualizamos `media`? \pause Não tem com! \pause Se `media` é `100.0`{.python} e `s` é `'nova'`{.python}, qual é o novo valor de `media`? \pause Não temos informações suficientes para responder essa pergunta! \pause

Como procedemos então? \pause Vamos discutir duas possibilidades: ajustar o processo incremental e separar o processo.

</div>
</div>


# Exemplo - média tamanho strings

Ajustando o processo incremental. \pause

Não conseguimos aplicar o processo incremental na primeira tentativa porque não conseguimos definir como atualizar `media` quando o próximo elemento `s` de `lst` é processado. \pause

O que precisamos saber além da `media` para conseguir atualizar a `media`? \pause A quantidade de elementos `quant` que já foram considerados no cálculo da `media`. \pause

Nós temos essa informação? \pause Não. \pause Como fazer então? \pause Computar `quant` de forma incremental junto com a `media`.


# Exemplo - média tamanho strings

Como inicializar `media` e `quant`? \pause Não está claro ainda. \pause

Como atualizar `media` e `quant`? \pause Considere por exemplo `media = 4`{.media} e `quant = 3`{.media} e o próximo elemento `s = 'processo'`{.python} de `lst`, quais devem ser os novos valores de `media` e `quant`? \pause `5`{.python} e `4`{.python}. \pause

Como atualizar a `media`? \pause `(quant * media + len(s)) / (quant + 1)`{.python} \pause

Como atualizar a `quant`? \pause `quant + 1`{.python} \pause

Como inicializar `media` e `quant`? \pause Com `0`{.python} (verifique que com esses valores iniciais o processo de atualização funciona quando o primeiro elemento da lista é processado).


# Exemplo - média tamanho strings

\footnotesize

```python
def media_tamanho(lst: list[str]) -> float:
    assert len(lst) != 0
    # quantidade de elementos que já
    # foram incluídos na media
    quant = 0
    media = 0.0
    for s in lst:
        media = (quant * media + len(s)) / (quant + 1)
        quant = quant + 1
    return media
```

\pause

\normalsize

A implementação está boa? \pause Parece confusa... \pause

Podemos melhorar? \pause Sim!


# Esboço de solução

Como determinamos manualmente as repostas dos exemplos? \pause Primeiro computamos a soma dos tamanhos e depois fizemos a média dividindo a soma pela quantidade de elementos. \pause

Podemos utilizar essa estratégia? \pause Sim! \pause

Isso é o que chamamos de **plano** ou **esboço de solução**, isto é, uma descrição em alto nível das etapas do processamento da função. \pause

Depois que temos um esboço, implementamos cada uma das etapas utilizando uma estratégias, ou seja, a implementação final é uma combinação de estratégias.


# Exemplo - média tamanho strings - implementação

<div class="columns">
<div class="column" width="45%">
\scriptsize

```python
def media_tamanho(lst: list[str]) -> float:
    assert len(lst) != 0
    # Calcular a soma dos tamanhos
    # Calcular a média
    return 0.0
```

</div>
<div class="column" width="52%">

\pause

**Soma dos tamanhos** \pause

Qual estratégia podemos utilizar? \pause A incremental. \pause Qual é o resultado que queremos computar? \pause A `soma` dos tamanhos. \pause Com qual valor iniciamos `soma`? \pause `0`{.python}. \pause Se estamos analisando o elemento `s` de `lst`, como atualizamos `soma`? \pause

`soma = soma + len(s)`{.python}. \pause

**Média** \pause

Como computamos a média? \pause Diretamente. \pause

`soma / len(lst)`{.python}.

</div>
</div>


# Exemplo - média tamanho strings - implementação

<div class="columns">
<div class="column" width="45%">
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

</div>
<div class="column" width="52%">

**Soma dos tamanhos**

Qual estratégia podemos utilizar? A incremental. Qual é o resultado que queremos computar? A `soma` dos tamanhos. Com qual valor iniciamos `soma`?  `0`{.python}. Se estamos analisando o elemento `s` de `lst`, como atualizamos `soma`?

`soma = soma + len(s)`{.python}.

**Média**

Como computamos a média? Diretamente.

`soma / len(lst)`{.python}.

</div>
</div>


# Exemplo - aprovados

O professor Alberto tem uma lista com os nomes dos alunos junto com a média final e a frequência de cada um. Agora ele precisa da sua ajuda para determinar os alunos que foram aprovados. Para ser aprovado um aluno deve ter média final maior ou igual a 6 e pelo menos 75% de frequência. \pause

a) Projete um tipo de dado para representar um aluno na lista do professor

a) Projete uma função que determine os nomes dos alunos aprovados na lista do professor


# Exemplo - aprovados

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
@dataclass
class Aluno:
    '''
    Representa um aluno e o resultado que ele
    obteve em uma disciplina.

    Requer que media esteja entre 0 e 10.
    Requer que frequencia esteja entre 0 e 100.
    '''
    nome: str
    media: float
    frequencia: float
```

\pause

```python
def aprovados(alunos: list[Aluno]) -> list[str]:
    '''
    Determina o nome dos *alunos* que foram
    aprovados, isto é, obteveram
    média >= 6 e frequência >= 75.
    '''
```

\pause

</div>
<div class="column" width="48%">

\scriptsize

```python
def aprovados(alunos: list[Aluno]) -> list[str]:
    '''
    >>> aprovados([])
    []
    >>> aprovados([
    ...     Aluno('Alfredo', 6.0, 74.0),
    ...     Aluno('Bianca', 5.9, 75.0),
    ...     Aluno('Jorge', 6.0, 75.0),
    ...     Aluno('Leonidas', 5.9, 74.0),
    ...     Aluno('Maria', 8.0, 90.0)])
    ['Jorge', 'Maria']
    '''
```

\pause

```python
    aprovados = []
    for aluno in alunos:
        if aluno.media >= 6 and \
                aluno.frequencia >= 75:
            aprovados.append(aluno.nome)
    return aprovados
```
</div>
</div>


# Revisão

Quando utilizamos a abordagem incremental? \pause

Quando precisamos computar algo de forma incremental! \pause Ou seja, quando não é possível computar a resposta de forma direta ou usando apenas seleção. \pause

O que precisamos determinar quando vamos utilizar a abordagem incremental? \pause

- Quais valores queremos computar; \pause
- Como os valores são inicializados; \pause
- Como os valores são atualizados.


# Revisão

O quê pode nos impedir de utilizar a abordagem incremental? \pause

- Se não conseguirmos definir como os valores são inicializados \pause
- Se não conseguirmos definir como os valores são atualizados, que foi o caso de `media_tamanhos` \pause

Como procedemos nesses casos? \pause

Ao invés de computar a resposta final de forma incremental, definimos um esboço de solução, que computa valores intermediários que serão utilizados para computar o valor final. \pause

No caso de `media_tamanhos`, primeiro computamos a soma dos tamanhos de forma incremental, e depois computamos a média diretamente.


# Revisão

Por enquanto, vimos uma forma de implementar a abordagem incremental no Python, \pause o "para cada", \pause que utilizamos quando estamos interessados em analisar todos os elementos de uma lista.

\pause

Essa forma pode não ser adequada ou suficiente para resolver alguns problemas.

\pause

Veremos a seguir outras possibilidades.
