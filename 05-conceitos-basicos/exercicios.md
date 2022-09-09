---
# vim: set spell spelllang=pt_br sw=4:
title: Conceitos básicos
---

Algumas observações:

- Nós vimos de maneira informal na última aula sobre "conceitos básicos" uma sequência de passos para projetar uma função. Este vai ser o processo que vamos utilizar durante toda a disciplina. Mesmo tendo apenas uma noção do processo, é importante que você tente segui-lo para resolver esses exercícios. Se você tiver dificuldades, não se preocupe, na próxima aula vamos fazer muitos exemplos, mas é importante você tentar e observar as suas dificuldades. Com o tempo, as coisas vão ficar mais claras.

- Em geral, quando temos que projetar uma função que verifica algo, podemos escolher booleano como tipo de retorno. Por exemplo, se tivéssemos que projetar uma função que verifica se um número inteiro é positivo, teríamos algo como

    ```cpp
    // Devolve true se n é um número positivo, isto é, maior que zero,
    // false caso contrário.
    // Exemplos:
    // positivo(3) -> true
    // positivo(0) -> false
    // positivo(-1) -> false
    bool positivo(int n)
    {
        return n > 0;
    }
    ```

#. O governo federal aumentou o valor da pensão do INSS em 5% e agora precisa atualizar a pensão de todos os pensionistas. Ajude o governo e projete uma função que calcule o novo valor de uma dada pensão.

#. De acordo com a Wikipédia, um supercentenário é uma pessoa que atinge a idade de 110 anos. Projete uma função que verifique, a partir da idade, se uma pessoa é supercentenário.

#. Uma polegada é um medida de comprimento utilizado no sistema imperial e corresponde a 2,54cm.

    a. Projete uma função que converta uma medida em centímetros para polegadas.

    b. Projete uma função que converta uma medida em polegadas para centímetros.

#. Quando escrevemos uma data no Brasil em geral usamos a ordem dia/mês/ano. Já em outros países a ordem usada é mês/dia/ano. Uma outra forma mais recente de escrever a data é ano/mês/dia. Projete uma função que receba como entra o dia o mês e o ano e gere uma string representando a data na forma ano/mês/dia.

#. Dizemos que o nome de uma pessoal é curto se tem no máximo três letras e longo se tem mais que 8 letras. Um nome que não é nem curto e nem longo é mediano. Projete uma função que verifique se um dado nome é mediano.

#. A operação de módulo é bastante comum na computação, mas muitos ainda não estão acostumados com essa operação, por isso é importante fazermos alguns exemplos para nos familiarizarmos com ela.

    a. Projete uma função que calcule a unidade de um número inteiro positivo, por exemplo, para o número 152, a unidade é 2.

    b. Projete uma função que calcule a dezena de um número inteiro positivo, por exemplo, para o número 152, a dezena é 5.

    c. Projete uma função que verifique se um dado número inteiro positivo é par.

    d. Projete uma função que verifique se os dois últimos dígitos de um número são 00.

#. Projete uma função que verifique se o primeiro nome de uma pessoa é "Paula". (Dica: `substr`)

#. Projete uma função que verifique se o sobrenome de uma pessoa é "Silva".

#. Projete uma função que calcule o valor da hipotenusa a partir dos valores dos catetos.

#. Resolva o problema do André, ele está esperando!

   O André viaja muito. Sempre antes de fazer uma viagem ele calcula o quanto ele irá gastar com combustível. Ele determina a distância que ele irá percorrer na viagem, o preço do litro do combustível e consulta as suas anotações para ver o consumo do carro, isto é, a quantidade de quilômetros que o carro anda com um litro de combustível e então faz o cálculo do custo. O André acha um pouco chato fazer os cálculos na mão, então ele pediu para você escrever um programa que faça os cálculos para ele.

#. Um construtor precisa calcular a quantidade de azulejos necessários pra azulejar uma determinada parede. Cada azulejo é quadrado e tem 20cm de lado. Ajude o construtor e defina uma função que receba como entrada o comprimento e a altura em metros de uma parede e calcule a quantidade de azulejos inteiros necessários para azulejar a parede. Considere que o construtor nunca perde um azulejo e que recortes de azulejos não são reaproveitados.

#. (Desafio) Projete uma função que encontre o maior valor entre dois números dados.
