---
# vim: set spell spelllang=pt_br:
title: Seleção
# TODO: falar mais sobre quando pensar em alto nível na execução do código e quando fazer o passo a passo
# TODO: dar nome ao processo de criar a implementação analisando as formas de resposta
# TODO: falar do contrato de função, entre o fornecedor e o usuário da função
# TODO: mudar o nome de seleção para análise de casos?
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


\small

\pause
Qual o valor exibido pelo programa? \pause

Não tente "executar" a chamada da função `dobro_mais_um`, pense apenas no seu propósito, sem olhar para o seu corpo. \pause

Então, qual é o valor exibido na tela? \pause 20. \pause

Qual é a ordem que as linhas são executadas? \pause

10, \pause 6, \pause 7, \pause 2, \pause 3, \pause 7, \pause 8, \pause 10. \pause

Confira a [execução](https://pythontutor.com/render.html#code=def%20dobro_mais_um%28n%3A%20int%29%20-%3E%20int%3A%0A%20%20%20%20a%20%3D%202%20*%20n%0A%20%20%20%20return%20a%20%2B%201%0A%0Adef%20main%28%29%3A%0A%20%20%20a%20%3D%205%0A%20%20%20n%20%3D%20dobro_mais_um%28a%20%2B%204%29%20%2B%201%0A%20%20%20print%28n%29%0A%0Amain%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false) desse código no Python Tutor (note que, diferente do fizemos em sala, as linhas do `def` são mostradas como sendo executadas).

</div>
</div>


# Seleção

O fluxo "normal" de execução de um programa é sequencial, isto é, as linhas são executadas uma após a outra. \pause Algumas instruções alteram esse fluxo, como por exemplo, as chamadas e retornos de funções. \pause


Agora veremos a instrução de seleção "se senão" (`if else`{.python} em inglês), que permite, a partir de uma condição, escolher qual conjunto de instruções executar.


# Seleção

<div class="columns">
<div class="column" width="48%">

A forma geral do `if else`{.python} é:

\small

```python
if condição:
    instruções então
else:
    instruções senão
```

\pause

</div>
<div class="column" width="48%">

Como a instrução `if else`{.python} é executada? \pause

O Python avalia a condição e verifica o resultado \pause

- Se o resultado for `True`{.python}, então as instruções do bloco "instruções então" são executadas; \pause
- Senão (o resultado é `False`{.python}), as instruções do bloco "instruções senão" são executadas;

</div>
</div>


# Exemplo

<div class="columns">
<div class="column" width="48%">

\small

```{.python .number-lines}
a = 10
b = 20
if a > b:
    m = a
else:
    m = b
print(m)
```

\pause

\normalsize

Qual o valor exibido pelo programa? \pause 20. \pause

Em que ordem as linhas são executas para gerar esse resultado? \pause 1, 2, 3, 6, 7. \pause
</div>
<div class="column" width="48%">

\small

```{.python .number-lines}
a = 15
b = 8
if a > b:
    m = a
else:
    m = b
print(m)
```

\pause

\normalsize

Qual o valor exibido pelo programa? \pause 15. \pause

Em que ordem as linhas são executas para gerar esse resultado? \pause 1, 2, 3, 4, 7 \pause
</div>
</div>

\ 

Qual é o propósito do `if else`{.python} nesses exemplos? \pause Determinar o valor máximo entre `a` e `b`.


# Exemplo - máximo

Vamos aproveitar esse exemplo e projetar uma função para encontrar o máximo entre dois números.


# Exemplo - máximo

<div class="columns">
<div class="column" width="48%">

\footnotesize

```{.python .number-lines}
def maximo(a: int, b: int) -> int:
    '''
    Devolve o valor máximo entre
    *a* e *b*.
    Exemplos
    >>> maximo(10, 8) # a é o máximo
    10
    >>> maximo(-2, -1) # b é o máximo
    -1
    '''
    if a > b:
        m = a
    else:
        m = b
    return m
```

</div>
<div class="column" width="48%">
\pause

Vamos treinar mais uma vez a execução passo a passo. \pause

Qual é a ordem que as linhas são executadas para o exemplo `maximo(10, 8)`{.python}? \pause

11, \pause 12, \pause 15. \pause

Qual é a ordem que as linhas são executadas para o exemplo `maximo(-2, -1)`{.python}? \pause

11, \pause 14, \pause 15.

</div>
</div>


# Exemplo - atualização número de telefone

Como "descobrimos" que precisamos utilizar uma instrução de seleção? \pause

Vamos voltar ao exemplo da atualização do número do telefone.


# Exemplo - atualização número de telefone

No período de 2015 à 2016 todos os números de telefones celulares no Brasil passaram a ter nove dígitos. Na época, os números de telefones que tinham apenas oito dígitos foram alterados adicionando-se o 9 na frete do número. Embora oficialmente todos os número de celulares tenham nove dígitos, na agenda de muitas pessoas ainda é comum encontrar números registrados com apenas oito dígitos. Projete uma função que adicione o nono dígito em um dado número de telefone celular caso ele ainda não tenha o nono dígito. Considere que os números de entrada são dados com o DDD entre parênteses e com um hífen separando os últimos quatro dígitos. Exemplos de entradas: (44) 9787-1241, (51) 95872-9989, (41) 8876-1562. A saída deve ter o mesmo formato, mas garantindo que o número do telefone tenha 9 dígitos.


# Exemplo - atualização número de telefone

**Análise** \pause

Ajustar o número de um telefone adicionando 9 como o nono dígito se necessário.

\pause

**Definição de tipo de dados** \pause

O número de telefone é uma string no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX, onde X pode ser qualquer dígito.

\pause

**Especificação** \pause

A seguir.


# Exemplo - atualização número de telefone

\footnotesize

```python
def ajusta_numero(numero: str) -> str:
    '''
    Ajusta *numero* adicionando o 9 como nono dígito se necessário, ou seja, se
    *numero* tem apenas 8 dígitos (sem contar o DDD).

    Requer que numero esteja no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX, onde
    X pode ser qualquer dígito.

    Exemplos
    >>>
    >>> ajusta_numero('(51) 95872-9989')
    '(51) 95872-9989'
    >>>
    >>> ajusta_numero('(44) 9787-1241')
    '(44) 99787-1241'
    '''
    return numero
```


# Exemplo - atualização número de telefone

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


# Exemplo - atualização número de telefone

Como "descobrimos" que precisamos utilizar uma instrução de seleção? \pause

Até agora, todas as funções que projetamos tinham apenas uma "forma" de gerar o resultado. \pause

Na função `ajusta_numero`, existem duas "formas" para a resposta: o próprio número ou o número ajustado. \pause

Como escolher quando cada forma deve ser utilizada na resposta da função? \pause Utilizando um condição: \pause

- Se a quantidade de caracteres de `numero` for 15, então a resposta é `numero`; \pause

- Senão a resposta é `numero[:5] + '9' + numero[5:]`{.python}. \pause

Quando a resposta depende de uma ou mais condições, usamos uma instrução de seleção!


# Exemplo - atualização número de telefone

\small

```python
def ajusta_numero(numero: str) -> str:
    if len(numero) == 15:
        ajustado = numero
    else:
        ajustado = numero[:5] + '9' + numero[5:]
    return ajustado
```


# Exemplo - máximo de 3

Projete uma função que encontre o valor máximo entre três números.


# Exemplo - máximo de 3

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


# Exemplo - máximo de 3

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


# Exemplo - máximo de 3

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

\small

`maximo3(10, 6, 8)`{.python}? \pause 6, \pause 7, \pause 13. \pause

`maximo3(10, 15, 8)`{.python}? \pause 6, \pause 9, \pause 10, \pause 13. \pause

`maximo3(10, 15, 20)`{.python}? \pause 6, \pause 9, \pause 12, \pause 13. \pause

Confira a [execução](https://pythontutor.com/render.html#code=def%20maximo3%28a%3A%20int,%20b%3A%20int,%20c%3A%20int%29%20-%3E%20int%3A%0A%20%20%20%20if%20a%20%3E%3D%20b%20and%20a%20%3E%3D%20c%3A%0A%20%20%20%20%20%20%20%20m%20%3D%20a%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20if%20b%20%3E%3D%20a%20and%20b%20%3E%3D%20c%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20m%20%3D%20b%0A%20%20%20%20%20%20%20%20else%3A%20%23%20c%20%3E%3D%20a%20and%20c%20%3E%3D%20b%0A%20%20%20%20%20%20%20%20%20%20%20%20m%20%3D%20c%0A%20%20%20%20return%20m%0A%0Aprint%28maximo3%2810,%206,%208%29%29%0A%0Aprint%28maximo3%2810,%2015,%208%29%29%0A%0Aprint%28maximo3%2810,%2015,%2020%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false) desse código no Python Tutor.
</div>
</div>


# Exemplo - máximo de 3

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


# Exemplo - máximo de 3

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


# Exemplo - máximo de 3

Vamos parar por um momento e relembrar como fazemos a implementação de uma função. \pause

Olhamos para a especificação, com atenção especial para os exemplos, e perguntamos: quantas formas de resposta temos nos exemplos? \pause

- Se existe apenas uma forma de resposta, isto é, a resposta dos exemplos são sempre calculadas da mesma forma, então usamos essa forma para implementar a função. \pause

- Se existe mais de uma forma, isto é, a resposta para pelo menos dois exemplos tem a forma distinta, então precisamos usar seleção. \pause Para cada forma de resposta identificamos uma condição e usamos as condições e as formas de resposta para implementar a função (o que fizemos na implementação da função `maximo3`).


# Exemplo - máximo de 3

No caso de mais de uma forma de resposta, a condição de cada forma pode ser composta, como no exemplo `maximo3`, onde a condição para a resposta ser `a`{.python} era `a >= b and a >= c`{.python} (a condição é composta por duas partes). \pause

Nesses casos, podemos verificar cada parte da condição de forma separada. A cada verificação, dividimos as formas de resposta em dois grupos, as que precisam que a condição seja verdadeira e as que precisam que a condição seja falsa. Usando verificação subsequentes, vamos restringindo as formas de resposta até chegar em apenas uma forma. \pause

Vamos tentar utilizar essa abordagem para fazer um implementação alternativa da função `maximo3`.


# Exemplo - máximo de 3

Se `a >= b`{.python} é `True`{.python}, quais valores podem ser o máximo? \pause Os valores de `a` e `c`. \pause E como descobrimos quem é o máximo entre `a` e `c`? \pause Fazendo outra seleção. \pause

Se `a >= b`{.python} é `False`{.python}, quais valores podem ser o máximo? \pause Os valores de `b` e `c`. \pause E como descobrimos quem é o máximo entre `b` e `c`? \pause Fazendo outra seleção.


\small

\pause

```
          a >= b
         /      \
      True     False
       /          \
    a >= c      b >= c
    /   \        /   \
 True  False  True  Flase
  /       \    /       \
  a       c    b       c
```


# Exemplo - máximo de 3

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


# Exemplo - máximo de 3

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


# Exemplo - máximo de 3

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


# Exemplo - máximo de 3

\small

```python
def maximo3(a: int, b: int, c: int) -> int:
    return maximo(maximo(a, b), c)
```

\pause

\normalsize

Poderíamos ter chegado nessa implementação na primeira vez? \pause

Sim, mas nesse caso, deveríamos ter visto que as três formas de resposta distintas poderiam ter sido generalizadas em uma única forma, que é `maximo(maximo(a, b), c)`{.python}. Essa generalização direta requer prática, por enquanto, podemos fazer os casos distintos e tentar, durante a revisão, simplificar o código.


# Exemplo - máximo de 3


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

11, 9, 2, 3, 6, 9, 2, 5, 6, 9, 11. \pause

Confira o [processo](https://pythontutor.com/render.html#code=def%20maximo%28a%3A%20int,%20b%3A%20int%29%20-%3E%20int%3A%0A%20%20%20%20if%20a%20%3E%20b%3A%0A%20%20%20%20%20%20%20%20m%20%3D%20a%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20m%20%3D%20b%0A%20%20%20%20return%20a%0A%0Adef%20maximo3%28a%3A%20int,%20b%3A%20int,%20c%3A%20int%29%20-%3E%20int%3A%0A%20%20%20%20return%20maximo%28maximo%28a,%20b%29,%20c%29%0A%0Amaximo3%2810,%202,%2015%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false) de execução desse código no Python Tutor.

</div>
</div>


# Exemplo - ponto final

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
    assert texto != '', "texto não pode ser ''"
    if texto[len(texto) - 1] == '.':
        com_ponto = texto
    else:
        com_ponto = texto + '.'
    return com_ponto
```
</div>
</div>


# Assert

Usamos o `assert`{.python} quando queremos expressar uma condição que precisa ser verdadeira para que o código continue executando. Caso a condição não seja verdadeira, o programa é interrompido (falha) com uma mensagem de erro. \pause

O que acontece na função `ponto_final` se não utilizarmos o `assert`{.python} e a função for chamada com o argumento `''`{.python}? \pause

Vai falhar na expressão `texto[len(texto) - 1]`{.python}, pois estamos querendo acessar o último caractere de uma string vazia. \pause

Se usando ou não o `assert`{.python} o programa falha, porque utilizar o `assert`{.python}? \pause Para que a falha tenha uma causa mais precisa, facilitando a depuração do programa.


# Assert

<div class="columns">
<div class="column" width="48%">
\footnotesize

```
>>> # sem assert
>>> ponto_final('')
Traceback (most recent call last):
    ...
    if texto[len(texto) - 1] == '.':
       ~~~~~^^^^^^^^^^^^^^^^
IndexError: string index out of range
>>> # Reação do usuário da função:
>>> # Que erro é esse?
```

</div>
<div class="column" width="48%">

\footnotesize

```
>>> # com assert
>>> ponot_final('')
Traceback (most recent call last):
    ...
    ...
    ...
AssertionError: texto não pode ser ''
>>> # Reação do usuário da função:
>>> # Entendi.
```

</div>
</div>


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


# Exemplo - centralizar string

Em uma determinada aplicação as strings precisam ser exibidas com pelo menos $n$ caracteres, onde $n$ pode variar dependendo da situação. Se uma string não tem $n$ caracteres, é necessário adicionar espaços em branco no início e fim da string, deixando ela centralizada entre os espaços, para que ela seja exibida corretamente. Projete uma função que ajuste uma string dessa forma. Assuma que a string de entrada não tenha espaços o início e no final.


# Exemplo - centralizar string

Análise

- Deixar uma string que não tem $n$ caracteres com $n$ caracteres adicionando espaços no início e no final da string.

\pause

Especificação

- A seguir


# Exemplo - centralizar string

<div class="columns">
<div class="column" width="48%">
\footnotesize

```python
def centraliza(s: str, n: int) -> str:
    '''
    Produz uma string adicionando espaços
    no início e fim de *s*, se necessário,
    de modo que ela fique com *n*
    caracteres.

    Se *s* tem mais que *n* caracteres,
    devolve *s*.

    Exemplos
    >>> centraliza('casa', 3)
    'casa'
    >>> centraliza('', 0)
    ''
    '''
```

</div>
<div class="column" width="48%">
\pause

Qual deve ser a resposta para `centraliza('casa', 5)`{.python}? \pause `' casa'`{.python} ou `'casa '`{.python}? \pause

Não está claro no propósito da função, então vamos voltar e esclarecer esse ponto.

</div>
</div>


# Exemplo - centralizar string

<div class="columns">
<div class="column" width="48%">
\footnotesize

```python
def centraliza(s: str, n: int) -> str:
    '''
    Produz uma string adicionando espaços
    no início e fim de *s*, se necessário,
    de modo que ela fique com *n*
    caracteres.

    Se *s* tem mais que *n* caracteres,
    devolve *s*.

    A quantidade de espaços adicionado no
    início é igual ou um a mais do que a
    quantidade adicionada no fim.
    '''
```


</div>
<div class="column" width="48%">
\pause

\footnotesize

```python
    >>> centraliza('casa', 3)
    'casa'
    >>> centraliza('', 0)
    ''
    >>> centraliza('casa', 10)
    '   casa   '
    >>> centraliza('casa', 9)
    '   casa  '
    >>> centraliza('apenas', 10)
    '  apenas  '
    >>> centraliza('apenas', 9)
    '  apenas '
```

</div>
</div>


# Exemplo - centralizar string

<div class="columns">
<div class="column" width="48%">
Temos dois casos: adiciona ou não os espaços. \pause

Qual é a condição para não adicionar espaços? \pause `len(s) >= n`{.python}. \pause

Qual é o processo para adicionar os espaços?

\pause Descobrir a quantidade de espaços, dividir em duas quantidades, a do início e a do fim, adicionar os espaços.

</div>
<div class="column" width="48%">
\pause

\footnotesize

```python
def centraliza(s: str, n: int) -> str:
    if len(s) >= n:
        r = s
    else:
        faltando = n - len(s)
        fim = faltando // 2
        inicio = faltando - fim
        r = ' ' * inicio + s + ' ' * fim
    return r
```

</div>
</div>


# Exemplo - álcool ou gasolina

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


# Exemplo - álcool ou gasolina - especificação

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


# Exemplo - álcool ou gasolina - implementação

Quantas formas para a resposta existem? \pause Duas: `'alcool'`{.python} e `'gasolina'`{.python}. \pause Então precisamos usar seleção. \pause Qual é a condição para que a resposta seja `'alcool'`{.python}? \pause `preco_alcool <= 0.7 * preco_gasolina`{.python} \pause

\small

```python
def indica_combustivel(preco_alcool: float, preco_gasolina: float) -> str:
    if preco_alcool <= 0.7 * preco_gasolina:
        combustivel = 'alcool'
    else:
        combustivel = 'gasolina'
    return combustivel
```


# Exemplo - álcool ou gasolina - verificação e revisão

Verificação: \pause ok. \pause

Revisão: \pause string não parece ser um tipo de dado apropriado... \pause

Vamos continuar na próxima aula...
