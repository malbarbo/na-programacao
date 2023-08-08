---
# vim: set spell spelllang=pt_br:
title: Seleção, enumerações e estruturas
# TODO: deixar claro que cada bloco pode ter mais que uma instrução
# TODO: dar nome ao processo de criar a implementação analisando as formas de resposta
# TODO: falar do contrato de função, entre o fornecedor e o usuário da função
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

A forma geral do `if else`{.python} é:

```cpp
if condição:
    instruções então
else:
    instruções senão
```

\pause

Como a instrução `if else`{.python} é executada? \pause O Python avalia a condição e verifica o resultado \pause

- Se o resultado for `True`{.python}, então as instruções do bloco "instruções então" são executadas; \pause
- Senão (o resultado é `False`{.python}), as instruções do bloco "instruções senão" são executadas;


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

Se temos respostas diferentes, então a resposta depende de uma ou mais condições. \pause Então, usamos instruções de seleção. \pause

Qual é a condição para a resposta ser `a`? \pause `a >= b and a >= c`{.python} \pause

Qual é a condição para a resposta ser `b`? \pause `b >= a and b >= c`{.python} \pause

Qual é a condição para a resposta ser `c`? \pause `c >= a and c >= b`{.python}

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

</div>
<div class="column" width="45%">
Qual é a ordem que as linhas são executadas para o exemplo a seguir:

`maximo(10, 6, 8)`{.python}? \pause 6, \pause 7, \pause 13 \pause

`maximo(10, 15, 8)`{.python}? \pause 6, \pause 9, \pause 10, \pause 13 \pause

`maximo(10, 15, 20)`{.python}? \pause 6, \pause 9, \pause 12, \pause 13
</div>
</div>


# Verificação e revisão

<div class="columns">
<div class="column" width="65%">
\small

```python
def maximo3(a: int, b: int, c: int) -> int:
    '''
    Encontra o valor máximo entre *a*, *b* e *c*.
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
<div class="column" width="35%">

\small

\pause

Verificação: \pause ok. \pause

Revisão \pause

Podemos modificar o código para torná-lo mais fácil de ler e entender? \pause

O Python permite "juntar" um `else`{.python} seguido de um `if`{.python} em um `elif`{.python}. Isto ajuda a diminuir os níveis de indentação, facilitando a escrita e leitura do código.
</div>
</div>


# Revisão

\small

```python
def maximo3(a: int, b: int, c: int) -> int:
    '''
    Encontra o valor máximo entre *a*, *b* e *c*.
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

\small

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
Qual o propósito do bloco das linhas 3 a 6? \pause Encontrar o máximo entre `a` e `c`. \pause

Qual o propósito do bloco das linhas 8 a 11? \pause Encontrar o máximo entre `b` e `c`. \pause

Já temos uma função para encontrar o máximo entre dois números? \pause Sim! \pause A função `maximo` que fizemos anteriormente.
</div>
</div>


# Revisão

<div class="columns">
<div class="column" width="60%">

\small

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

Poderíamos ter chegado nessa implementação na primeira vez? \pause

Sim, mas nesse caso, deveríamos ter visto que as três formas de resposta distintas poderiam ter sido generalizadas em uma única forma, que é `maximo(maximo(a, b), c)`{.python}. Essa generalização direta requer prática, por enquanto, podemos fazer os casos distintos e tentar durante a revisão simplificar o código.


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

Se as duas formas o programa crasha, porque utilizar o `assert`{.python}? \pause Para que a falha tenha uma causa mais precisa, facilitando a depuração do programa.


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


# Álcool ou Gasolina?

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

Quantas formas para a resposta existem? \pause 2, `'alcool'`{.python} e `'gasolina'`{.python}. \pause Então precisamos usar seleção. \pause Qual é a condição para a resposta `'alcool'`{.python}? \pause `preco_alcool <= 0.7 * preco_gasolina`{.python} \pause

\small

```python
def indica_combustivel(preco_alcool: float, preco_gasolina: float) -> str:
    if preco_alcool <= 0.7 * preco_gasolina:
        combustivel = "alcool"
    else:
        combustivel = "gasolina"
    return combustivel
}
```


# Verificação e revisão

Verificação: \pause ok. \pause

Revisão: \pause string não parece ser o tipo apropriado. \pause Pela assinatura da função, "qualquer" string pode ser dada como resposta, mas de fato apenas dois valores são possível: `'alcool'`{.python} e `'gasolina'`{.python}. \pause Podemos melhorar? \pause Sim.


<!--

# Tipos enumerados

Em um **tipo enumerado** todos os valores válidos para o tipo são enumerados explicitamente. \pause

A forma geral para definir tipos enumerados é

```cpp
enum NomeDoTipo {
    Valor1,
    Valor2,
    ...,
};
```


# Tipos enumerados

```cpp
// O tipo do combustível utilizado no abastecimento.
enum Combustivel {
    Alcool,
    Gasolina,
};
```

\pause

\normalsize

Observações \pause

- Sempre vamos adicionar um comentário sobre o propósito do tipo; \pause
- É necessário finalizar a declaração com um ponto e vírgula;


# Tipos enumerados

Uma variável do tipo `Combustivel` só pode armazenar o valor `Alcool` ou `Gasolina`, se tentarmos atribuir um valor diferente, o compilador indicará um erro. \pause

\small

```cpp
Combustivel c = "Alcool";
```

\pause

Erro

\footnotesize

```
x.cpp:13:21: error: cannot convert ‘const char*’ to ‘Combustivel’ in initialization
   13 |     Combustivel c = "Alcool";
      |                     ^~~~~~~~
```


# Tipos enumerados

Quando usar tipos enumerados? \pause

Quando todos os valores válidos para o tipo podem ser nomeados. \pause

Por que utilizar tipos enumerados? \pause

Para expressar mais claramente o propósito do código e evitar a utilização de valores inválidos (como `"alcoo"`{.cpp} em uma variável string que representa o tipo do combustível).


# Revisão do exemplo

\footnotesize

```cpp
Combustivel indica_combustivel(double preco_alcool, double preco_gasolina)
{
    Combustivel combustivel;
    if (preco_alcool <= 0.7 * preco_gasolina) {
        combustivel = Alcool;
    } else {
        combustivel = Gasolina;
    }
    return combustivel;
}
examples
{
    check_expect(indica_combustivel(4.000, 5.000), Gasolina);
    check_expect(indica_combustivel(4.000, 6.000), Alcool);
    check_expect(indica_combustivel(3.500, 5.000), Alcool);
}
```


# Exemplo

Projete uma função que receba como entrada a cor atual de um semáforo de trânsito e devolva a próxima cor que será ativada (considere um semáforo com três cores: verde, amarelo e vermelho). \pause

Fizemos o projeto desse programa durante a aula obtivemos o seguinte resultado:


# Semáforo

<div class="columns">
<div class="column" width="48%">
\scriptsize

```cpp
// Representa a cor de um semáforo.
enum Cor {
    Verde,
    Vermelho,
    Amarelo,
};
// Produz a próximo cor de um semáforo
// que está com a cor c.
Cor proxima_cor(Cor c) {
    Cor proxima;
    if (c == Verde) {
        proxima = Amarelo;
    } else if (c == Vermelho) {
        proxima = Verde;
    } else { // c == Amarelo
        proxima = Vermelho;
    }
    return proxima;
}
```
</div>
<div class="column" width="48%">

\scriptsize

```cpp
examples
{
    check_expect(proxima_cor(Verde), Amarelo);
    check_expect(proxima_cor(Vermelho), Verde);
    check_expect(proxima_cor(Amarelo), Vermelho);
}
```

\pause

\small

Verificação: \pause Ok. \pause

Revisão: \pause vamos usar uma construção nova, o `switch/case`{.cpp}.

</div>
</div>


# `switch/case`{.cpp}

<div class="columns">
<div class="column" width="48%">
A sintaxe simplificada do `switch/case`{.cpp} é

\scriptsize

```cpp
switch (expressão) {
    // zero ou mais casos
    case caso1:
        instruções;
        break;
    // ...
    case cason:
        instruções;
        break;
    // opcional
    default:
        instruções;
        break;
}
```

\small

Onde `expressão` precisa gerar um valor do tipo inteiro ou enumerado.
</div>
<div class="column" width="48%">
\small
\pause
A instrução `switch/case`{.cpp} funciona da seguinte forma: \pause

A `expressão` é avaliada e seu valor é comparado com cada caso na sequência. \pause

Quando um caso que tem o mesmo valor do resultado da expressão é encontrado, as `instruções` daquele caso são executadas até encontrar um `break`, quando então a instrução `switch/case`{.cpp} termina e o programa continua a execução com a próxima instrução após o `switch/case`{.cpp}. \pause

Se o valor da expressão não é igual a nenhum caso, então as instruções da cláusula `default`{.cpp} são executadas.

</div>
</div>


# `switch/case`{.cpp}

Quando utilizar o `switch/case`{.cpp}? \pause

Quando precisamos analisar o valor de um tipo enumerado ou quando precisamos analisar um conjunto de valores inteiros específicos (ex 1, 3, 4, 5). \pause

Qual é a vantagem de utilizar `switch/case`{.cpp} ao invés de uma sequência de `if`{.cpp}s? \pause

O código fica mais fácil de ler. \pause

O compilador (usando a opção `-Wall`) gera um aviso se esquecermos de algum valor na análise de valores enumerados.



# Semáforo

Escrevendo a função `proxima_cor` para utilizar o `switch/case`{.cpp} obtemos \pause

\footnotesize

```cpp
Cor proxima_cor(Cor c) {
    Cor proxima;
    switch (c) {
        case Verde:
            proxima = Amarelo;
            break;
        case Vermelho:
            proxima = Verde;
            break;
        case Amarelo:
            proxima = Vermelho;
            break;
    }
    return proxima;
}
```


# Exemplo

Em um determinado programa é necessário exibir para o usuário o tempo que uma operação demorou. Esse tempo está disponível em segundos, mas exibir essa informação em segundos para o usuário pode não ser interessante, afinal, ter uma noção razoável de tempo para 14678 segundos é difícil! \pause

a) Projete uma função que converta uma quantidade de segundos para uma quantidade de horas, minutos e segundos equivalentes. \pause

b) Projete uma função que converta uma quantidade de horas, minutos e segundos em uma string amigável para o usuário. A string não deve conter informações sobre tempo que são zeros (por exemplo, não deve informar 0 minutos).


# Exemplo

Análise

- Converter uma quantidade de segundos em horas, minutos e segundos. \pause

Definição de tipos de dados

- Os segundos da entrada serão representados com números inteiros positivos \pause

- A saída são três números inteiros positivos... \pause As funções em C++ só podem produzir um valor de saída, como proceder? \pause Vamos criar um novo tipo de dado que agrupa esses três valores.



# Tipos de dados

Vamos relembrar alguns tipos de dados que utilizamos até agora:

- Tipos atômicos pré-definidos (primitivos) na linguagem: `int, double, bool`{.cpp}
- Tipos atômicos definidos em bibliotecas: `string`{.cpp}
- Tipos atômicos enumerados definidos pelo usuário: `enum`{.cpp}

\pause

Esses tipos são chamados atômicos porque não são compostos por partes. \pause

Podemos criar novos tipos de dados a partir de tipos existentes. \pause

Uma forma de fazer isso é através de tipos estruturas.


# Tipos estruturas

Um **tipo estrutura** é um tipo de dado composto por um conjunto fixo de campos com nome e tipo.

\pause

A forma geral para definir um tipo estrutura é

```cpp
struct NomeDoTipo {
    Tipo1 campo1;
    Tipo2 campo2;
    ...
};
```


# Tipos estruturas

\small

Podemos definir um novo tipo para representar um tempo da seguinte forma

```cpp
// Representa o tempo de duração de um evento.
// horas, minutos e segundos devem ser positivos.
// minutos e segundos devem ser menores que 60.
struct Tempo {
    int horas;
    int minutos;
    int segundos;
};
```

\pause

Observações

- Assim como para definição de tipos enumerados, sempre vamos adicionar um comentário sobre o propósito do tipo; \pause
- É necessário finalizar a declaração com um ponto e vírgula.


# Tipos estruturas

Para inicializar uma variável de um tipo estrutura, especificamos os valores dos campos (na ordem que eles foram declarados) entre chaves e separados por vírgula \pause

```cpp
Tempo t1 = {0, 20, 10};
Tempo t2 = {4, 0, 20};
```

\pause

Para exibir um valor de um tipo estrutura podemos utilizar a função `repr` da biblioteca `bscpp`

```cpp
cout << repr(t1) << endl; // Tempo {0, 20, 10}
```


# Tipos estruturas

Como valores do tipo `Tempo` são compostos de outros valores (partes), podemos acessar e alterar cada valor de forma separada. \pause

```cpp
Tempo t1 = {0, 20, 10};

cout << t1.minutos << endl; // exibe 20

t1.horas = 3; // muda a quantidade de horas para 3
```

\pause

Agora podemos voltar para o nosso problema.


# Especificação e implementação

<div class="columns">
<div class="column" width="65%">
Especificação

\scriptsize

```cpp
// Converte a quantidade segundos para o tempo equivalente em
// horas, minutos e segundos. A quantidade de segundos e
// minutos da resposta é sempre menor que 60.
Tempo segundos_para_tempo(int segundos) {
    return Tempo {0, 0, 0};
}

examples {
    // 160 / 60 -> 2
    // 160 % 60 -> 40
    check_expect(segundos_para_tempo(160), (Tempo {0, 2, 40}));
    // 3760 / 3600 -> 1
    // 3760 % 3600 -> 160 segundos que sobraram
    // 160 / 60 -> 2
    // 160 % 60 -> 40
    check_expect(segundos_para_tempo(3760), (Tempo {1, 2, 40}));
}
```

\pause
</div>
<div class="column" width="33%">
Implementação

\scriptsize

```cpp
Tempo segundos_para_tempo(int segundos)
{
    int h = segundos / 3600;
    // segundos que não foram
    // convertidos para hora
    int restantes = segundos % 3600;
    int m = restantes / 60;
    int s = restantes % 60;
    return Tempo {h, m, s};
}
```

\pause

Verificação: ok \pause

Revisão: ok
</div>
</div>


# Estruturas

Quando utilizamos estruturas? \pause

Quando a informação consiste de dois ou mais itens que juntos descrevem uma entidade.


# Exemplo

O novo problema inicial era:

Em um determinado programa é necessário exibir para o usuário o tempo que uma operação demorou. Esse tempo está disponível em segundos, mas exibir essa informação em segundos para o usuário pode não ser interessante, afinal, ter uma noção razoável de tempo para 14678 segundos é difícil!

a) Projete uma função que converta uma quantidade de segundos para uma quantidade de horas, minutos e segundos equivalentes.

b) Projete uma função que converta uma quantidade de horas, minutos e segundos em uma string amigável para o usuário. A string não deve conter informações sobre o tempo que são zeros (por exemplo, não deve informar 0 minutos).

\pause

Agora vamos fazer o item b. (Projeto desenvolvido em aula.)


# Especificação

\scriptsize

```cpp
// Converte t em uma mensagem para o usuário. Cada componente de t aparece
// com a sua unidade, mas se o valor do componente for 0, ele não aparece na
// mensagem. Os componentes são separados com " e " ou ", " respeitando as
// regras do Português. Se t for {0, 0, 0}, devolve "0 segundo(s)".
string tempo_para_string(Tempo t)
{
   return "";
}
```

# Especificação

\scriptsize

```cpp
examples {
    // horas == 0 && minutos == 0
    check_expect(tempo_para_string(Tempo {0, 0, 0}), "0 segundo(s)");
    check_expect(tempo_para_string(Tempo {0, 0, 1}), "1 segundo(s)");
    check_expect(tempo_para_string(Tempo {0, 0, 10}), "10 segundo(s)");
    // horas == 0 && minutos != 0 && segundos != 0
    check_expect(tempo_para_string(Tempo {0, 1, 20}), "1 minuto(s) e 20 segundo(s)");
    // horas == 0 && minutos != 0 && segundos == 0
    check_expect(tempo_para_string(Tempo {0, 2, 0}), "2 minuto(s)");
    // horas != 0 && minutos != 0 && segundos != 0
    check_expect(tempo_para_string(Tempo {1, 2, 1}), "1 hora(s), 2 minuto(s) e 1 segundo(s)");
    // horas != 0 && minutos == 0 && segundos != 0
    check_expect(tempo_para_string(Tempo {4, 0, 25}), "4 hora(s) e 25 segundo(s)");
    // horas != 0 && minutos != 0 && segundos == 0
    check_expect(tempo_para_string(Tempo {2, 4, 0}), "2 hora(s) e 4 minuto(s)");
    // horas != 0 && minutos == 0 && segundos == 0
    check_expect(tempo_para_string(Tempo {3, 0, 0}), "3 hora(s)");
}
```

# Implementação

A implementação direta usando as condições combinadas fica com exercício. \pause

A implementação a seguir usando condições aninhadas foi desenvolvida em sala.

#

<div class="columns">
<div class="column" width="48%">
Implementação

\tiny

```cpp
string tempo_para_string(Tempo t) {
    string h = to_string(t.horas) + " hora(s)";
    string m = to_string(t.minutos) + " minuto(s)";
    string s = to_string(t.segundos) + " segundo(s)";
    string msg = "";
    // nos exemplos são 7 casos distintos
    if (t.horas > 0) {
        if (t.minutos > 0) {
            if (t.segundos > 0) {
                msg = h + ", " + m + " e " + s;
            } else {
                msg = h + " e " + m;
            }
        } else if (t.segundos > 0) {
            msg = h + " e " + s;
        } else {
            msg = h;
        }
    } else if (t.minutos > 0) {
        if (t.segundos > 0) {
            msg = m + " e " + s;
        } else {
            msg = m;
        }
    } else {
        msg = s;
    };
    return msg; }
```

</div>
<div class="column" width="48%">
\pause

Implementação alternativa

\tiny

```cpp
string tempo_para_string(Tempo t) {
    // usado para separar cada componente de t
    string sep = "";
    string msg = "";
    if (t.segundos > 0) {
        sep = " e ";
        msg = to_string(t.segundos) + " segundo(s)";
    }

    if (t.minutos > 0) {
        msg = to_string(t.minutos) + " minuto(s)" + sep + msg;
        if (t.segundos > 0) {
            sep = ", ";
        } else {
            sep = " e ";
        }
    }

    if (t.horas > 0) {
        msg = to_string(t.horas) + " hora(s)" + sep + msg;
    }

    if (msg == "") {
        msg = "0 segundo(s)";
    }

    return msg;
}
```
</div>
</div>


# Exercício

Modifique a especificação e implementação da função anterior para que o plural dos componentes fique de acordo com o Português.


# Exemplo

\small

Segundo a Wikipédia, um pixel é o menor elemento de um dispositivo de exibição, como por exemplo, um monitor, ao qual é possível atribuir uma cor. Nos monitores atuais, os pixels são organizados em linhas e colunas, de maneira a formar a imagem exibida. Cada pixel pode ser referenciado por uma coordenada, que é o número da linha e coluna que ele aparece. Por exemplo, em um monitor de 1080 linhas e 1920 colunas, o pixel no canto superior esquerdo está na posição (0, 0), enquanto o pixel no canto inferior direito está na posição (1079, 1919). \pause

Em um ambiente gráfico com janelas, quando um usuário faz um clique com o mouse é necessário identificar em qual janela ocorreu o clique. Considerando que o espaço que uma janela ocupa pode ser representada pela coordenada do canto superior esquerdo e pela quantidade de pixels da largura e da altura da janela \pause

a) Projete uma função que receba como parâmetros as informações sobre uma janela e um clique do mouse e determine se o clique aconteceu sobre a janela. \pause

b) Projete uma função que verifique se os espaços de duas janelas se sobrepõem.


# Definição de tipos de dados

Projeto desenvolvido em aula.


# Definição de tipos de dados

\scriptsize

```cpp
// Representa o espaço que uma janela ocupa em um ambiente gráfico.
//
// A coordenada (x, y) descreve a posição do canto superior esquerdo.
// A largura representa a quantidade de pixels à direita de (x, y)
// e a altura representa a quantidade de pixels abaixo de (x, y).
//
// Os valores da largura e altura devem ser maiores que zero.
struct Janela {
    int x;
    int y;
    int largura;
    int altura;
};
```

\pause

```cpp
// Representa a posição de um clique em um ambiente gráfico.
// Os valores de x e y devem ser maiores que 0 e menores do que as dimensões do
// ambiente.
struct Clique {
    int x;
    int y;
};
```


# Especificação

\scriptsize

```cpp
// Devolve true se o clique c está dentro do espaço da janela j, false contrário.
bool dentro_janela(Janela j, Clique c)
{
   return false;
}
```

# Especificação

\scriptsize

```cpp
examples {
    //  x = 100, y = 100, largura = 300, altura = 200
    //
    //        p5
    //      +-----------+
    //  p4  | p1        | p2
    //      |           |
    //      +-----------+
    //        p3
    Janela janela = { 100, 100, 300, 200 };
    // p1 - dentro da janela
    check_expect(dentro_janela(janela, { 150, 150 }), true);
    // p2 - dentro do espaço da altura e depois do espaço da largura
    check_expect(dentro_janela(janela, { 600, 150 }), false);
    // p3 - depois do espaço da altura e dentro do espaço da largura
    check_expect(dentro_janela(janela, { 150, 300 }), false);
    // p4 - dentro do espaço da altura e antes do espaço da largura
    check_expect(dentro_janela(janela, { 150, 50 }), false);
    // p5 - antes do espaço da altura e dentro do espaço da largura
    check_expect(dentro_janela(janela, { 150, 50 }), false);
```


# Especificação

\scriptsize

```cpp
    // canto superior esquerdo
    check_expect(dentro_janela(janela, { 100, 100 }), true);
    // canto superior direito
    check_expect(dentro_janela(janela, { 399, 100 }), true);
    check_expect(dentro_janela(janela, { 400, 100 }), false);
    // canto inferior direito
    check_expect(dentro_janela(janela, { 399, 299 }), true);
    check_expect(dentro_janela(janela, { 400, 299 }), false);
    check_expect(dentro_janela(janela, { 399, 300 }), false);
    check_expect(dentro_janela(janela, { 400, 300 }), false);
    // canto inferior esquerdo
    check_expect(dentro_janela(janela, { 100, 299 }), true);
    check_expect(dentro_janela(janela, { 100, 300 }), false);
}
```

# Implementação

\scriptsize

```cpp
// Devolve true se o clique c está dentro do espaço da janela j, false contrário.
bool dentro_janela(Janela j, Clique c)
{
    // c.x está dentro do espaço da largura e c.y dentro do espaço da altura
    return j.x <= c.x && c.x < (j.x + j.largura) && j.y <= c.y && c.y < (j.y + j.altura);
}
```

\pause

\normalsize

Verificação: ok \pause

Revisão: ok


# Especificação

\scriptsize

```cpp
// Produz true se o espaço das janelas a e b se soprepõem, false caso contrário.
bool janelas_soprepoem(Janela a, Janela b)
{
    return false;
}

examples
{
    // fixa (eixo y): a janela a vem antes da janela b
    // variável: posição da borda direita de a
    check_expect(janelas_soprepoem({  10, 20, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 210, 20, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 310, 20, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 410, 20, 100, 200 }, { 300, 400, 50, 100 }), false);
    // fixa: (eixo y) interseção da parte de baixo de a com a parte de cima de b
    // variável: posição da borda direita de a
    check_expect(janelas_soprepoem({  10, 250, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 210, 250, 100, 200 }, { 300, 400, 50, 100 }), true);
    check_expect(janelas_soprepoem({ 310, 250, 100, 200 }, { 300, 400, 50, 100 }), true);
    check_expect(janelas_soprepoem({ 410, 250, 100, 200 }, { 300, 400, 50, 100 }), false);
```

# Especificação

\scriptsize

```cpp
    // fixa: (eixo y) interseção da parte de cima de a com a parte de baixo de b
    // variável: posição da borda direita de a
    check_expect(janelas_soprepoem({  10, 450, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 210, 450, 100, 200 }, { 300, 400, 50, 100 }), true);
    check_expect(janelas_soprepoem({ 310, 450, 100, 200 }, { 300, 400, 50, 100 }), true);
    check_expect(janelas_soprepoem({ 410, 450, 100, 200 }, { 300, 400, 50, 100 }), false);
    // fixa: (eixo y) a janela a vem depois da janela b
    // variável: posição da borda direita de a
    check_expect(janelas_soprepoem({  10, 550, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 210, 550, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 310, 550, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 410, 550, 100, 200 }, { 300, 400, 50, 100 }), false);
}
```


# Implementação

\scriptsize

```cpp
// Produz true se o espaço das janelas a e b se soprepõem, false caso contrário.
bool janelas_soprepoem(Janela a, Janela b)
{
    return a.x < (b.x + b.largura) &&
           // borda direta de a vem antes da borda esquerda de b
           b.x < (a.x + a.largura) &&
           // borda direta de b vem antes da borda esquerda de a
           a.y < (b.y + b.altura) &&
           // borda superior de a vem antes da borda inferior de b
           b.y < (a.y + a.altura);
           // borda superior de b vem antes da borda inferior de a
}
```


# Exemplo

\small

Em um jogo de loteria os apostadores fazem apostas escolhendo 6 números distintos entre 1 e 60. No sorteio são sorteados 6 números de forma aleatória. Os apostadores que acertam 4, 5 ou 6 números são contemplados com prêmios. Projete uma função que conte quantos números uma determinada aposta acertou.

\pause

Projeto desenvolvido em sala.

# Definição de tipos de dados

\scriptsize

```cpp
// Coleção de 6 números distintos entre 1 e 60.
struct SeisNumeros {
    int a;
    int b;
    int c;
    int d;
    int e;
    int f;
};
```

\pause

\normalsize

As apostas e os números sorteados serão representados pela estrutura `SeisNumeros`.


# Especificação

\scriptsize

```cpp
// Calcula quantos números da aposta estão em sorteados.
int numero_acertos(SeisNumeros aposta, SeisNumeros sorteados)
{
    return 0;
}

examples
{
    check_expect(numero_acertos({1, 2, 3, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 0);
    check_expect(numero_acertos({8, 2, 3, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 1);
    check_expect(numero_acertos({8, 12, 3, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 2);
    check_expect(numero_acertos({8, 12, 20, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 3);
    check_expect(numero_acertos({8, 12, 20, 41, 5, 6}, {8, 12, 20, 41, 52, 57}), 4);
    check_expect(numero_acertos({8, 12, 20, 41, 52, 6}, {8, 12, 20, 41, 52, 57}), 5);
    check_expect(numero_acertos({8, 12, 20, 41, 52, 57}, {8, 12, 20, 41, 52, 57}), 6);
}
```

\normalsize

\pause

Qual o processo que utilizamos para determinar as respostas?


# Especificação

Começamos o número de acertos com zero. \pause

Depois verificamos se o primeiro número está entre os sorteados, se sim, aumentamentos os acertos em 1. \pause

Depois verificamos se o segundo número está entre os sorteados, se sim, aumentamentos os acertos em 1. \pause

E assim com o restante dos números. No final, temos a quantidade de acertos. \pause

Este processo não parece muito detalhado... \pause como verificamos se um número está entre os sorteados? \pause Vamos deixar esse problema para depois. \pause

Como expressar esse processo em C++? \pause Com uma sequência de etapas, como em muitos exercícios anteriores.


# Implementação

<div class="columns">
<div class="column" width="48%">
\scriptsize

```cpp
int acertos = 0;
if (sorteado(aposta.a, sorteados)) {
    acertos = acertos + 1;
}
if (sorteado(aposta.b, sorteados)) {
    acertos = acertos + 1;
}
if (sorteado(aposta.c, sorteados)) {
    acertos = acertos + 1;
}
if (sorteado(aposta.d, sorteados)) {
    acertos = acertos + 1;
}
if (sorteado(aposta.e, sorteados)) {
    acertos = acertos + 1;
}
if (sorteado(aposta.f, sorteados)) {
    acertos = acertos + 1;
}
return acertos;
```
</div>
<div class="column" width="48%">
\pause

\small

Aqui utilizamos o pensamento desejoso e desejamos que a função `sorteado`{.cpp} exista e funcione de acordo com a seguinte especificação:

\scriptsize

```cpp
// Produz true se n é um dos números em sorteados,
// false caso contrário.
bool sorteado(int n, SeisNumeros sorteados);
```

\small

\pause

Todas as funções que desejamos durante o projeto de outra função são colocas em uma lista de pendência. Após o término da implementação da função em questão, precisamos implementar as funções da lista de pendências.

\pause

Agora precisamos terminar o projeto da função `sorteado`{.cpp}.

</div>
</div>


# Lista de pendências

\scriptsize

```cpp
// Produz true se n é um dos números em sorteados, false caso contrário.
bool sorteado(int n, SeisNumeros sorteados)
{
    return false;
}

examples {
    SeisNumeros sorteados = {1, 7, 10, 40, 41, 60};
    check_expect(sorteado(1, sorteados), true);
    check_expect(sorteado(7, sorteados), true);
    check_expect(sorteado(10, sorteados), true);
    check_expect(sorteado(40, sorteados), true);
    check_expect(sorteado(41, sorteados), true);
    check_expect(sorteado(60, sorteados), true);
    check_expect(sorteado(2, sorteados), false);
    check_expect(sorteado(15, sorteados), false);
    check_expect(sorteado(49, sorteados), false);
}
```

\pause

\normalsize

Qual o processo que utilizamos para determinar as respostas?


# Implementação

Verificamos se `n` é igual ao primeiro valor sorteado, se sim, guardamos a resposta `true`{.cpp}. \pause

Senão, verificamos se `n` é igual ao segundo valor sorteado, se sim, guardamos a resposta `true`{.cpp}. \pause

Senão, verificamos se `n` é igual ao terceiro valor... Senão guardamos a resposta `false`{.cpp}. \pause

Como expressar esse processo em C++? \pause Com uma sequência de etapas! \pause Aqui vamos fazer uma simplificação para evitar o aninhamento demasiado de ifs. \pause Vamos colocar um if após o outro (você consegue ver que este processo alternativo continua correto?)



# Implementação

<div class="columns">
<div class="column" width="48%">
\tiny

```cpp
// Produz true se n é um dos números
// em sorteados, false caso contrário.
bool sorteado(int n, SeisNumeros sorteados)
{
    bool sorteado = false;
    if (n == sorteados.a) {
        sorteado = true;
    }
    if (n == sorteados.b) {
        sorteado = true;
    }
    if (n == sorteados.c) {
        sorteado = true;
    }
    if (n == sorteados.d) {
        sorteado = true;
    }
    if (n == sorteados.e) {
        sorteado = true;
    }
    if (n == sorteados.f) {
        sorteado = true;
    }
    return sorteado;
}
```
</div>
<div class="column" width="48%">

\pause

Implementação alternativa.

\tiny

```cpp
// Produz true se n é um dos números
// em sorteados, false caso contrário.
bool sorteado(int n, SeisNumeros sorteados)
{
    return n == sorteados.a ||
        n == sorteados.b ||
        n == sorteados.c ||
        n == sorteados.d ||
        n == sorteados.e ||
        n == sorteados.f;
}
```

</div>
</div>


# Verificação e Revisão

Verificação: \pause ok \pause

Revisão: \pause o código parece repetitivo... \pause Vamos ver novas construções!

-->
