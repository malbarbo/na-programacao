---
title: Projeto de programas - Prática
urlcolor: Blue
# TODO: refazer a lista com exercícios mais objetivos
# TODO: fazer exercícios sobre cada etapa individual
---

#. Faça o download dos exemplos de projeto de programas na página da disciplina.

    a) Abra o diretório com o código no vscode.

    a) Faça a verificação de tipos com o `mypy`.

    a) Faça a verificação dos exemplos com o `doctest`.

    a) Adicione algum erro no código e use o `mypy` para identificá-lo.

    a) Adicione algum erro no código e use o `doctest` para identificá-lo.


#. Faça o download e leia as soluções da prática de conceitos básicos na página da disciplina.

    a) Observe a forma como os propósitos foram escritos.

    a) Observe a forma como os exemplos foram escritos.

    a) Observe como as implementações foram feitas.

    a) Faça a verificação de tipos com o `mypy`

    a) Faça a verificação dos exemplos com o `doctest`


#. Faça o download e leia as soluções dos exercícios de conceitos básicos na página da disciplina.

    a) Leia com cuidado o código observando como a especificação e a implementação foram feitas.

    a) Escreva a especificação para os demais exercícios (no seu código) de conceitos básicos e faça a verificação de tipos com o `mypy` e a verificação dos exemplos com o `doctest`.

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
