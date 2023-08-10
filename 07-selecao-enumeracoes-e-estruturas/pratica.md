---
# vim: set spell spelllang=pt_br sw=4:
title: Seleção, enumerações e estruturas - Prática
---

#. Escreva a especificação para a seguinte implementação de função. Observe que a especificação sozinha deve ser suficiente para um desenvolvedor fazer uma implementação. Faça a revisão do código.

    ```python
    def qualificacao(num_questoes: int, num_acertos: int, num_faltas: float) -> str:
        aproveitamento = num_acertos / num_questoes
        if aproveitamento < 0.3 or faltas > 0.25:
            resultado = 'reprovado'
        elif aproveitamento < 0.6:
            resultado = 'nova-tentativa'
        else:
            resultado = 'aprovado'
        return resultado
    ```

#. De um determinado ponto de vista, um número inteiro tem duas características, a sua magnitude, isto é, o valor absoluto, e o sinal. Em Python podemos utilizar a função `abs`{.python} para obter o valor absoluto de um número, mas não existe uma função pré-definida para determinar o sinal de um número. Projete uma função que determine o sinal de um número, produzindo `-1`{.python} para valores negativos, `0`{.python} para o `0`{.python} e `+1`{.python} para valores positivos.

#. Um banco emprega diferentes taxas de correção anual para um investimento dependendo do valor aplicado no início de cada ano. Para valores até R$ 2000 a taxa de correção é de 10%, para valores entre R$ 2000 e R$ 5000 a taxa de correção é de 12%, para valores maiores que R$ 5000 a taxa de correção é de 13%.

    a) Projete uma função que calcule quanto um investimento realizado no início do ano irá render após um ano aplicado no banco.

    b) Projete uma função que calcule quanto um investimento realizado no início do ano irá render após dois anos aplicado no banco.

#. Dizemos que o nome de uma pessoal é curto se tem no máximo quatro letras e longo se tem mais que 8 letras. Um nome que não é nem curto e nem longo é mediano. Projete uma função que classifique um nome de acordo com seu número de letras.
