---
# vim: set spell spelllang=pt_br sw=4:
title: |
       | Fundamentos de Algoritmos
       | Projeto de funções
urlcolor: Blue
# TODO: fazer mais exercícios sobre cada etapa individual
# TODO: melhorar os exercícios de avançando (remover do paralelepipido)
---

**\color{red}Lembre-se** de seguir o processo de projeto de funções e de usar o `mypy` e o `doctest` na etapa de verificação.

# Começando

@) Leia o material de projeto de funções e responda:

    a) Quais são as etapas do processo de projeto de funções?

    a) Qual é o propósito da análise?

    a) Qual é o propósito da definição dos tipos de dados?

    a) Quais são as partes que compõem a especificação de uma função?

    a) Qual é a principal propriedade que uma especificação deve ter para ser considerada adequada?

    a) O que é a assinatura de uma função?

    a) Qual é o objetivo inicial dos exemplos no projeto de uma função? E os demais objetivos?

    a) Se não forem encontrados erros na verificação para os exemplos da especificação, é possível afirma que a função está isenta de erros? Explique.

    a) A implementação é a fase mais importante do projeto de funções, verdadeiro ou falso? Explique.

    a) Como proceder quando um teste falha?

    a) Qual é o objetivo da revisão?

    a) Qual é a diferença do resultado da análise e a descrição do propósito da função?

@) Faça a instalação do `mypy` com o comando `pip install mypy`.

@) Faça o download dos exemplos de projeto de programas na página da disciplina e para cada arquivo

    a) Observe a forma como os propósitos foram escritos.

    a) Observe a forma como os exemplos foram escritos.

    a) Observe como as implementações foram feitas.

    a) Faça a verificação de tipos com o `mypy` usando o comando `mypy arquivo.py`.

    a) Faça a verificação dos exemplos com o `doctest` usando o comando `python -m doctest -v arquivo.py`.


# Praticando

@) Implemente a função de acordo com a especificação a seguir. Corrija a especificação se necessário.

    ```python
    def isento_tarifa(idade: int) -> bool:
        '''
        Produz True se uma pessoa de *idade* anos é isento da tarifa
        de transporte público, isto é, tem menos que 18 anos ou 65
        ou mais. Produz False caso contrário.

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

@) Escreva os exemplos e implemente a função de acordo com a assinatura e o propósito a seguir.

    ```python
    def dma_para_amd(data: str) -> str:
        '''
        Transforma *data*, que deve estar no formato "dia/mes/ano",
        onde dia e mes tem dois dígitos e ano tem quatro dígitos,
        para o formato "ano/mes/dia".
        '''
        return ''
    ```

@) Escreva a especificação para a seguinte implementação de função. Observe que a especificação sozinha   deve ser suficiente para um desenvolvedor fazer uma nova implementação.

    ```python
    def numero_digitos(n: int) -> int:
        return len(str(abs(n)))
    ```

@) Para cada função da lista de exercícios de conceitos básicos que você implementou, complete o projeto da função adicionando a especificação (propósito e exemplos). Faça a verificação com o `mypy` e com o `doctest`.


# Avançando

@) Você está fazendo um programa e precisa verificar se um texto digitado pelo usuário está de acordo com algumas regras. A regra “sem espaços extras” requer que o texto não comece e não termine com espaços. Projete uma função que verifique se um texto qualquer está de acordo com a regra “sem espaços extras”.

@) Pablo é um artesão e precisa pintar uma série de paralelepípedos. Antes de começar a pintura, ele fez um teste inicial e descobriu que ele demora 30 segundos para pintar uma área de 8 cm por 8 cm. Projete uma função que determine quanto tempo Pablo irá demorar para pintar um paralelepípedo.

@) Rotacionar uma string `n` posições a direita significa mover os últimos `n` caracteres da string para as primeiras `n` posições da string. Por exemplo, rotacionar a string `"marcelio"` 5 posições a direita produz a string `"celiomar"`. Projete uma função que receba como entrada uma string e um número `n` e produza uma nova string rotacionando a string de entrada `n` posições a direita.
