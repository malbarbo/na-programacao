---
title: Conceitos básicos - Prática
urlcolor: Blue
---

#. Reveja o material de [conceitos básicos](https://malbarbo.pro.br/arquivos/2023/6879/05-conceitos-basicos-notas-de-aula.pdf) e responda [esse](https://forms.gle/Hrnhg5oCinaAhydn7) quiz (não vale nota).

#. Faça uma função chamada `area_retangulo` que recebe dois argumentos, a `largura` e a `altura` de um retângulo, e calcula a sua área. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> area_retangulo(3.0, 5.0)
    15.0
    >>> area_retangulo(2.0, 2.5)
    5.0
    ```


#. Faça uma função chamada `produto_anterior_posterior` que recebe um número inteiro `n` e calcula o produto de `n`, `n + 1` e `n - 1`. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> produto_anterior_posterior(3)
    24
    >>> produto_anterior_posterior(1)
    0
    >>> produto_anterior_posterior(-2)
    -6
    ```


#. Faça uma função chamada `aumenta` que recebe dois número positivos, um `valor` e uma `porcentagem`, e calcula o resultado de aumentar a `porcetagem` ao `valor`. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> aumenta(100.0, 3.0)
    103.0
    >>> aumenta(20.0, 50.0)
    30.0
    >>> aumenta(10.0, 80.0)
    18.0
    ```


#. Faça uma função chamada `zera_dezena_e_unidade` que recebe um número natural `n` e devolve um novo número que é como `n` mas tem o valor da dezena e unidade zero. Dica: use piso da divisão. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> zera_dezena_e_unidade(19)
    0
    >>> zera_dezena_e_unidade(341)
    300
    >>> zera_dezena_e_unidade(5251)
    5200
    ```


#. Faça uma função chamada `exclamacao` que recebe dois argumento, uma string `frase` e um número natural `n`, e produz a mesma frase adicionando `n` pontos de exclamação no final da frase. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> exclamacao('Nossa', 3)
    'Nossa!!!'
    >>> exclamacao('Que legal', 1)
    'Que legal!'
    >>> exclamacao('Nada', 0)
    'Nada'
    ```


#. Faça uma função chamada `primeira_maiuscula` que recebe uma string `frase` e produz a mesma frase mas com a primeira letra em maiúscula. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> primeira_maiuscula('joao venceu.')
    'Joao venceu.'
    >>> primeira_maiuscula('A Paula é um sucesso.')
    'A paula é um sucesso.'
    ```


#. Faça uma função chamada `censura` que recebe dois argumento, uma string `frase` e um número natural `n`, e produz uma nova frase trocando as as primeiras `n` letras da frase de entrada por `n` `'x'`. Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

    ```python
    >>> censura('droga de lanche!', 5)
    'xxxxx de lanche!'
    >>> censura('ferrou geral!', 6)
    'xxxxxx geral!'
    ```

#. Para cada exercício anterior, faça um programa com uma função `main` com entrada, processamento e saída.
