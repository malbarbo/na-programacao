---
# vim: set spell spelllang=pt_br sw=4:
title: Conceitos básicos
---

Algumas observações:

- Nós vimos de maneira informal na última aula sobre "conceitos básicos" uma sequência de passos para projetar uma função. Este vai ser o processo que vamos utilizar durante toda a disciplina. Mesmo tendo apenas uma noção do processo, é importante que você tente segui-lo para resolver esses exercícios. Se você tiver dificuldades, não se preocupe, na próxima aula vamos fazer muitos exemplos, mas é importante você tentar e observar as suas dificuldades. Com o tempo, as coisas vão ficar mais claras.

- Em geral, quando temos que projetar uma função que verifica algo, podemos escolher booleano como tipo de retorno. Por exemplo, se tivéssemos que projetar uma função que verifica se um número inteiro é positivo, teríamos algo como

    ```cpp
    // Devolve true se n é um número positivo, isto é, maior que zero, false caso constrário.
    // Exemplos:
    // positivo(3) -> true
    // positivo(0) -> false
    // positivo(-1) -> false
    bool positivo(int n)
    {
        return n > 0;
    }
    ```


#. Projete uma função que calcule o valor da hipotenusa a partir dos valores dos catetos.

#. Projete uma função que calcule a unidade de um número inteiro positivo, por exemplo, para o número 152, a unidade é 2. Dica: operação de módulo.

#. Projete uma função que verifique se o primeiro nome de uma pessoa é "Paula".

#. Projete uma função que verifique se o sobrenome de uma pessoa é "Silva".

#. Projete uma função que calcule a dezena de um número inteiro positivo, por exemplo, para o número 152, a dezena é 5. Dica: divisão inteira e módulo

#. Projete uma função que calcule a centena de um número inteiro positivo, por exemplo, para o número 152, a centena é 1. Dica: divisão inteira e módulo.

#. Projete uma função que verifique se um dado número inteiro positivo é par.

#. Resolva o problema do André, ele está esperando!

   O André viaja muito. Sempre antes de fazer uma viagem ele calcula o quanto ele irá gastar com combustível. Ele determina a distância que ele irá percorrer na viagem, o preço do litro do combustível e consulta as suas anotações para ver o consumo do carro, isto é, a quantidade de quilômetros que o carro anda com um litro de combustível e então faz o cálculo do custo. O André acha um pouco chato fazer os cálculos na mão, então ele pediu para você escrever um programa que faça os cálculos para ele.

#. Um construtor precisa calcular a quantidade de azulejos necessários pra azulejar uma determinada parede. Cada azulejo é quadrado e tem 20cm de lado. Ajude o construtor e defina uma função que receba como entrada o comprimento e a altura em metros de uma parede e calcule a quantidade de azulejos inteiros necessários para azulejar a parede. Considere que o construtor nunca perde um azulejo e que recortes de azulejos não são reaproveitados.

#. (Desafio) Projete uma função que encontre o maior valor entre dois números dados.
