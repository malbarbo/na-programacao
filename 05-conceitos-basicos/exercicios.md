---
# vim: set spell spelllang=pt_br sw=4:
title: Conceitos básicos - Exercícios
# TODO: Pensar com mais cuidados na questões para que elas atigam todo o conteúdo
# TODO: Fazer outro quiz
---

Observações:

- Deixe anotado com comentários os exemplos que você utilizou para testar a função.

- A funções que verificam algo devem ter como saída um `bool`{.python}.

\ 

#) Leia o material de conceitos básicos.

#) Indique o valor de cada resultado oculto nessa seção de interações. Use a janela de interações após calcular as respostas manualmente para conferir se elas estão corretas.

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
    >>> nome[:4].to_upper()
    ?
    >>> nome[5:].to_lower()
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

#) Projete uma função que calcule o valor da hipotenusa a partir dos valores dos catetos.

#) Uma polegada é um medida de comprimento utilizado no sistema imperial e corresponde a 2,54cm.

    a. Projete uma função que converta uma medida em centímetros para polegadas.

    b. Projete uma função que converta uma medida em polegadas para centímetros.

#) Quando escrevemos uma data no Brasil em geral usamos a ordem dia/mês/ano. Já em outros países a ordem usada é mês/dia/ano. Uma outra forma mais recente de escrever a data é ano/mês/dia. Projete uma função que receba como entrada o dia o mês e o ano e gere uma string representando a data na forma ano/mês/dia.

#) Dizemos que o nome de uma pessoal é curto se tem no máximo três letras e longo se tem mais que 8 letras. Um nome que não é nem curto e nem longo é mediano. Projete uma função que verifique se um dado nome é mediano.

#) A operação de resto da divisão é bastante comum na computação, mas muitos ainda não estão acostumados com essa operação, por isso é importante fazermos alguns exemplos para nos familiarizarmos com ela.

    a. Projete uma função que calcule a unidade de um número inteiro positivo, por exemplo, para o número 152, a unidade é 2.

    b. Projete uma função que calcule a dezena de um número inteiro positivo, por exemplo, para o número 152, a dezena é 5.

    c. Projete uma função que calcule a centena de um número inteiro positivo, por exemplo, para o número 152, a centena é 1.

    d. Projete uma função que verifique se os dois últimos dígitos de um número são 00.

#) Projete uma função que verifique se o primeiro nome de uma pessoa é "Paula". Você pode assumir que a string de entrada não tem espaços no início e no final e que contém pelo menos um espaço em branco.

#) Projete uma função que verifique se o último nome (sobrenome) de uma pessoa é "Silva". Você pode assumir que a string de entrada não tem espaços no início e no final e que contém pelo menos um espaço em branco.

#) Para cada exercícios de projeto de função, faça um programa com a função `main` com entrada, processamento e saída.

#) (Desafio) Projete uma função que encontre o maior valor entre dois números dados.
