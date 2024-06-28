---
# vim: set spell spelllang=pt_br:
title: Tipos de dados
# TODO: explicar diretamente como escrever os exemplos para funções que retornam enum
# TODO: apresentar match/case?
# TODO: adicionar mais exemplos (juntando estruturas e enumerações, contagem de tipos de sorvertes?)
#       a questão é que atualizar uma contagem pode requerer passagem por referência.
# TODO: adicionar exemplos com tipos dos campos diferentes
# TODO: deixar claro que valores dos tipos estruturas são mutáveis por padrão?
---

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
        acertos = acertos + 1
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
