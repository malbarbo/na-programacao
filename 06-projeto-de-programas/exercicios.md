---
# vim: set spell spelllang=pt_br sw=4:
title: Projeto de programas - Exercícios
# TODO: mais exercícios?
---


#. Implemente a função de acordo com a especificação a seguir. Corrija a especificação se necessário.

    ```python
    def isento_tarifa(idade: int) -> bool:
        '''
        Produz True se uma pessoa de *idade* anos é isento da tarifa de transporte
        público, isto é, tem menos que 18 anos ou 65 ou mais. Produz False caso
        contrário.

        Exemplos
        >>> isento_tarifa(17)
        True
        >>> isento_tarifa(18)
        True
        >>> isento_tarifa(50)
        False
        >>> isento_tarifa(65)
        True
        >>> isento_tarifa(70)
        True
        '''
        return False
    ```

#. Escreva os exemplos e implemente a função de acordo com a assinatura e o propósito a seguir.

    ```python
    def dma_para_amd(data: str) -> str:
        '''
        Transforma *data*, que deve estar no formato "dia/mes/ano",
        onde dia e mes tem dois dígitos e ano tem quatro dígitos,
        para o formato "ano/mes/dia".
        '''
        return ''
    ```

#. Escreva a especificação para a seguinte implementação de função. Observe que a especificação sozinha   deve ser suficiente para um desenvolvedor fazer uma nova implementação.

    ```python
    def numero_digitos(n: int) -> int:
        return len(str(abs(n)))
    ```

#. Pablo é um artesão e precisa pintar uma série de paralelepípedos. Antes de começar a pintura, ele fez um teste inicial e descobriu que ele demora 30 segundos para pintar uma área de 8 cm por 8 cm. Projete uma função que determine quanto tempo Pablo irá demorar para pintar um paralelepípedo.

#. Rotacionar uma string `n` posições a direita significa mover os últimos `n` caracteres da string para as primeiras `n` posições da string. Por exemplo, rotacionar a string `"marcelio"`{.scheme} 5 posições a direita produz a string `"celiomar"`{.scheme}. Projete uma função que receba como entrada uma string e um número `n` e produza uma nova string rotacionando a string de entrada `n` posições a direita.

#. Você está fazendo um programa e precisa verificar se um texto digitado pelo usuário está de acordo com algumas regras. A regra “sem espaços extras” requer que o texto não comece e não termine com espaços. Projete uma função que verifique se um texto qualquer está de acordo com a regra “sem espaços extras”.
