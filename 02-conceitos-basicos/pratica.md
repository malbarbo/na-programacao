---
title: Conceitos básicos - Prática
urlcolor: Blue
# TODO: adicionar avaliação de expressões relacionais e booleanas
---

@) Indique o valor de cada resultado oculto nessa seção de interações. Use a janela de interações após calcular as respostas manualmente para conferir se elas estão corretas.

    ```python
    >>> 2 * 19 // 3
    ?
    >>> 64 ** 1 / 4
    ?
    >>> 15 % 6 * 8 / 4
    ?
    >>> a: int = len('palavra') + 11
    >>> a // 2 * 2
    ?
    >>> b: int = a + a // 3
    >>> a = 12
    >>> b
    ?
    >>> b = 2 * b
    >>> b
    ?
    >>> nome: str = 'José da Silva'
    >>> nome[:4].upper()
    ?
    >>> nome[5:].lower()
    ?
    >>> nome[3:7]
    ?
    >>> nome[3:7][1]
    ?
    >>> str(len(nome))
    ?
    >>> int('1' * len(nome)) % 100
    ?
    >>> nome = nome + ' e Almeida'
    >>> nome
    ?
    ```


@) Faça uma função chamada `area_retangulo` que recebe dois argumentos, a `largura` e a `altura` de um retângulo, e calcula a sua área. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> area_retangulo(3.0, 5.0)
    15.0
    >>> area_retangulo(2.0, 2.5)
    5.0
    ```


@) Faça uma função chamada `produto_anterior_posterior` que recebe um número inteiro `n` e calcula o produto de `n`, `n + 1` e `n - 1`. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> produto_anterior_posterior(3)
    24
    >>> produto_anterior_posterior(1)
    0
    >>> produto_anterior_posterior(-2)
    -6
    ```


@) Faça uma função chamada `aumenta` que recebe dois número positivos, um `valor` e uma `porcentagem`, e calcula o resultado de aumentar a `porcetagem` ao `valor`. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> aumenta(100.0, 3.0)
    103.0
    >>> aumenta(20.0, 50.0)
    30.0
    >>> aumenta(10.0, 80.0)
    18.0
    ```


@) Faça uma função chamada `zera_dezena_e_unidade` que recebe um número natural `n` e devolve um novo número que é como `n` mas tem o valor da dezena e unidade zero. Dica: use piso da divisão. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> zera_dezena_e_unidade(19)
    0
    >>> zera_dezena_e_unidade(341)
    300
    >>> zera_dezena_e_unidade(5251)
    5200
    ```


@) Faça uma função chamada `exclamacao` que recebe dois argumento, uma string `frase` e um número natural `n`, e produz a mesma frase adicionando `n` pontos de exclamação no final da frase. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> exclamacao('Nossa', 3)
    'Nossa!!!'
    >>> exclamacao('Que legal', 1)
    'Que legal!'
    >>> exclamacao('Nada', 0)
    'Nada'
    ```


@) Faça uma função chamada `primeira_maiuscula` que recebe uma string `frase` e produz a mesma frase mas com a primeira letra em maiúscula. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> primeira_maiuscula('joao venceu.')
    'Joao venceu.'
    >>> primeira_maiuscula('A Paula é um sucesso.')
    'A paula é um sucesso.'
    ```


@) Faça uma função chamada `censura` que recebe dois argumento, uma string `frase` e um número natural `n`, e produz uma nova frase trocando as as primeiras `n` letras da frase de entrada por `n` `'x'`. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> censura('droga de lanche!', 5)
    'xxxxx de lanche!'
    >>> censura('ferrou geral!', 6)
    'xxxxxx geral!'
    ```


@) Faça uma função chamada `par` que recebe um número natural `n` e indica se `n` é par. Um número é par se o resto da divisão dele por 2 é igual a zero. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> par(3)
    False
    >>> par(6)
    True
    ```


@) Faça uma função chamada `tres_digitos` que recebe um número natural `n` e verifica se `n` tem exatamente 3 dígitos. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```scheme
    >>> tres_digitos(99)
    False
    >>> tres_digitos(100)
    False
    >>> tres_digitos(999)
    True
    >>> tres_digitos(1000)
    False
    ```


@) Faça uma função chamada `termina_z` que recebe uma string `s` e indica se `s` termina com a letra `'z'`. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> termina_z('arroz')
    True
    >>> termina_z('')
    False
    >>> termina_z('Z')
    True
    >>> termina_z('casa')
    False
    ```


