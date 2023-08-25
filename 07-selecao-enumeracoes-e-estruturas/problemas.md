---
# vim: set spell spelllang=pt_br sw=4:
title: Seleção, enumerações e estruturas - Problemas
---

<!-- Seleção -->

@. Cada cidadão de um país, cuja moeda chama dinheiro, tem que pagar imposto sobre a sua renda. Cidadãos que recebem até 1000 dinheiros pagam 5% de imposto. Cidadãos que recebem entre 1000 e 5000 dinheiros pagam 5% de imposto sobre 1000 dinheiros e 10% sobre o que passar de 1000. Cidadãos que recebem mais do 5000 dinheiros pagam 5% de imposto sobre 1000 dinheiros, 10% de imposto sobre 4000 dinheiros e 20% sobre o que passar de 5000. Projete uma função que calcule o imposto que um cidadão deve pagar dado a sua renda.

@. Um banco emprega diferentes taxas de correção anual para um investimento dependendo do valor aplicado no início de cada ano. Para valores até R$ 2000 a taxa de correção é de 10%, para valores entre R$ 2000 e R$ 5000 a taxa de correção é de 12%, para valores maiores que R$ 5000 a taxa de correção é de 13%.

    a) Projete uma função que calcule quanto um investimento realizado no início do ano irá render após um ano aplicado no banco.

    b) Projete uma função que calcule quanto um investimento realizado no início do ano irá render após dois anos aplicado no banco. Dica: use a função do item a para fazer a implementação.

@. Em um determinado jogo os jogadores são classificados em níveis de 0 a 25 e este nível é atualizado semanalmente baseado na quantidade de horas que o jogador jogou o jogo. Os jogadores que jogaram entre 4 e 5 horas permanecem no mesmo nível. Os jogadores que jogaram menos que 4 horas diminuem um nível a cada 1 hora que faltou para alcançar as 4 horas. Os jogadores que jogaram mais de 5 horas aumentam um nível a cada hora jogada além das 5 horas respeitando o limite máximo de 7 níveis. Projete uma função que recebe o nível atual do jogador e a quantidade de horas jogadas em uma semana e calcule o novo nível do jogador.

<!-- TODO: não precisa de seleção? -->

@. Muitos letreiros exibem mensagens que tem mais caracteres do que eles podem exibir, para isso, eles exibem apenas uma porção da mensagem que é alterada com o passar do tempo. Por exemplo, em um letreiro de 20 caracteres, a mensagem `'Promocao de sorvetes, pague 2 leve 3!'` é exibida como `Promocao de sorvetes` no momento 0, como `'romocao de sorvetes,'` no momento 1, `'omocao de sorvetes, '`, no momento 3, e assim por diante até que no momento 17 é exibido `'tes, pague 2 leve 3!'`. O momento sempre aumenta, e após chegar no final da mensagem ela começa a ser exibida novamente, nesse caso, no momento 18 é exibido `'es, pague 2 leve 3! '` e no momento 19 é exibido `'s, pague 2 leve 3! P'`, onde o `P` é o início da mensagem. Projete uma função que determine os caracteres de uma mensagem que devem ser exibidos em um determinado momento em um letreiro que pode exibir um determinado número de caracteres. Você pode assumir que o número de caracteres da mensagem é maior do que o do letreiro.

<!--
@. Escreva a especificação para a seguinte implementação de função. Observe que a especificação sozinha deve ser suficiente para um desenvolvedor fazer uma implementação. Faça a revisão do código.

    ```python
    def qualificacao(num_questoes: int, num_acertos: int, faltas: float) -> str:
        aproveitamento = num_acertos / num_questoes
        if aproveitamento < 0.3 or faltas > 0.25:
            resultado = 'reprovado'
        elif aproveitamento < 0.6:
            resultado = 'nova-tentativa'
        else:
            resultado = 'aprovado'
        return resultado
    ```
-->

<!-- Enumerações -->

@. Dizemos que o nome de uma pessoal é curto se tem no máximo quatro letras e longo se tem mais que 8 letras. Um nome que não é nem curto e nem longo é mediano. Projete uma função que classifique um nome de acordo com seu número de letras.

@. O Brasil institui há algum tempo um sistema de bandeira tarifária para sinalizar ao consumidores os custos reais de geração de energia. Nesse sistema, a bandeira verde indica condições favoráveis de geração de energia e a tarifa não sofre acréscimo. Já a bandeira amarela indica condições menor favoráveis e por isso a tarifa sofre um acréscimo de R$ 0,01874 para cada quilowatt-hora. A bandeira vermelha - patamar 1 indica condições mais custosas de geração e o acréscimo na tarifa é de R$ 0,03971 para cada quilowatt-hora consumido. Por fim, a bandeira vermelha - patamar 2 indica condições ainda mais custosas e o acréscimo na tarifa é de R$ 0,09492 para cada quilowatt-hora consumido. Projete uma função que determine o valor final que o consumidor tem que pagar dado o seu consumo em quilowatt-hora, a tarifa básica do quilowatt-hora e a bandeira tarifária.

@. A nota final em um disciplina é calculada pela média simples de 4 avaliações que valem de 0 a 10. A partir da nota final os alunos ficam em um de três situações: Aprovado, alunos com nota final maior ou igual a 7. Reprovado, alunos com nota menor que 4. Exame, alunos com nota maior igual a 4 e menores que 7. Projete uma função que indique a situação de um aluno dado as 4 notas das suas avaliações.

@. Beatriz gosta muito de jogar cartas com as amigas. Para treinar memória e raciocínio lógico, ela inventou um pequeno passatempo com cartas enumeradas de 1 a 13. Ela retira as três primeiras cartas do topo de um baralho bem embaralhado, e as coloca em sequência, da esquerda para a direita, na mesa, com as faces voltadas para cima. Então ela olha, por um breve instante, cada uma das cartas da sequência e logo as recoloca na mesa, com a face para baixo. Usando apenas a sua memória, Beatriz deve agora dizer se a sequência de cartas está ordenada crescentemente, decrescentemente, ou não está ordenada. De tanto jogar, ela está ficando cansada e não confia em seu próprio julgamento para saber se acertou ou errou. Por isso, ela pediu para você fazer um programa que, dada uma sequência de três cartas, determine se a sequência dada está ordenada crescentemente, decrescentemente, ou não está ordenada.

@. Jokenpô é um jogo recreativo bastante conhecido no Brasil. Nele dois participantes esticam a mão simultaneamente e formam um símbolo, que pode ser pedra, papel ou tesoura. A decisão de quem ganha é feita da seguinte forma: a pedra ganha da tesoura, a tesoura ganha do papel, e o papel ganha da pedra. Projete uma função que determine a partir do nome e símbolo feito por dois jogadores, quem ganhou no jogo.


<!-- Estruturas -->

@. Em um concurso público a classificação dos candidatos é feita pelos pontos (0 a 100) obtidos em um prova, no caso de empate, o candidato com o menor número de inscrição é classificado primeiro. Dado as informações de dois candidatos do concurso, projete uma função que determine o candidato melhor classificado.

@. Considere um jogo onde o personagem está em um tabuleiro (semelhante a um tabuleiro de jogo de xadrez). As linhas e colunas do tabuleiro são enumeradas de 1 a 10, dessa forma, é possível representar a posição (casa) do personagem pelo número da linha e da coluna que ele se encontra. O personagem fica virado para uma das direções: norte, sul, leste ou oeste. O jogador pode avançar o seu personagem qualquer número de casas na direção que ele está virado, mas é claro, não pode sair do tabuleiro. Projete uma função que indique a partir das informações do personagem, qual é o número máximo de casas que ele pode avançar na direção que ele está virado.

@. Uma determinada sala de reunião pode ser usada das 8:00h às 18:00h. Cada interessado em utilizar a sala faz uma reserva indicando o intervalo de tempo que gostaria de utilizar a sala. Como parte de um sistema de reservas, você deve projetar uma função que verifique se duas reservas podem ser atendidas, ou seja, não têm conflito de horário.

@. O desempenho de um time de futebol em um determinado campeonato é dado pelo número de pontos, número   de vitórias e saldo de gols (diferenças entre todos os gols marcados e sofridos), nessa ordem. Caso dois times empatem nesse critérios, a ordem alfabética dos nomes é usado para desempate.

    a) Projete uma função que determine qual de dois times tem o melhor desempenho.

    b) Considerando que cada jogo ganho pelo time dá 3 pontos e empate 1 ponto, projete uma função que atualize o desempenho de um time dado o resultado de um jogo.

@. Segundo a Wikipédia, um pixel é o menor elemento de um dispositivo de exibição, como por exemplo, um monitor, ao qual é possível atribuir uma cor. Nos monitores atuais, os pixels são organizados em linhas e colunas, de maneira a formar a imagem exibida. Cada pixel pode ser referenciado por uma coordenada, que é o número da linha e coluna que ele aparece. Por exemplo, em um monitor de 1920 colunas por 1080 linhas, o pixel no canto superior esquerdo está na posição (0, 0), enquanto o pixel no canto inferior direito está na posição (1919, 1079).

    Em um ambiente gráfico com janelas, quando o usuário faz um clique com o mouse é necessário identificar em qual janela ocorreu o clique.

    a) Projete uma função que receba como parâmetros as informações sobre uma janela e um clique do mouse e determine se o clique aconteceu sobre a janela.

    b) (Desafio) Projete uma função que verifique se os espaços de duas janelas se sobrepõem.
