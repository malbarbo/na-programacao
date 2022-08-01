---
# vim: set spell spelllang=pt_br:
# TODO: separar em diversos arquivos
title: Repetição, arranjos e conjuntos
---

# Introdução

Vimos anteriormente que devemos definir uma estrutura para representar uma informação quando ela consiste de dois ou mais itens que juntos descrevem uma entidade. \pause

- No problema da conversão de segundos para horas, minutos e segundos, definimos a estrutura `Tempo`. \pause

- No problema da loteria, definimos a estrutura `SeisNumeros`.


# Introdução

O `Tempo` era composto de três "itens", que foram representados pelos campos horas, minutos e segundos. \pause

Já para `SeisNúmeros` cada item não tinha uma interpretação particular, então não usamos nomes significativos, tivemos que "inventar" os nomes de `a`, ..., `f`. \pause

Como faríamos se ao invés de 6 itens tivéssemos 20? \pause E 1.000? E 1.000.000? \pause Ou ainda, uma quantidade indefinida? \pause E como escrever o código para processar esse tipo de dado? \pause

Vamos ver como fazer essas!


# Arranjos de tamanho fixo

Quando precisamos representar uma coleção com um número fixo de valores de mesma natureza (todos os itens são notas, nomes, pontos, janelas, etc), utilizamos arranjos de tamanho fixo. \pause

Os arranjos em C++ são definidos na biblioteca `array`. Quando declaramos uma variável do tipo arranjo, precisamos especificar o tipo e a quantidade de elementos. A inicialização é feita de forma semelhante a valores do tipo estrutura.


# Arranjos de tamanho fixo

\scriptsize

```cpp

#include <array>
...

examples
{
    array<int, 4> valores = {10, 4, 9, -1};
    array<string, 3> nomes = {"joao", "jose", "maria"};
```

\pause

\normalsize

Para ler ou modificar um valor específico do arranjo, especificamos o seu índice entre colchetes \pause

\scriptsize

```cpp
    check_expect(valores[0], 10);
    check_expect(nomes[2], "maria");

    check_expect(valores[1], 4);
    valores[1] = 25;
    check_expect(valores[1], 25);
}
```

\pause

\normalsize

Observe que o primeiro elemento de um arranjo tem índice 0.


# Arranjos de tamanho fixo

O valor do índice deve estar no intervalo válido para o arranjo, caso contrário, o programa pode não funcionar corretamente. \pause Por padrão, os índices dos arranjos não são verificados antes de serem acessados. \pause Caso seja necessário fazer a verificação, deve-se usar o método `at`.

\scriptsize

```cpp
array<int, 4> valores = {10, 4, 9, -1};
check_expec(valores.at(1), 4);
valores.at(1) = 12;
check_expec(valores.at(1), 12);
```

\pause

No caso de

```cpp
valores.at(4);
```

o seguinte erro é gerado

```
terminate called after throwing an instance of 'std::out_of_range'
  what():  array::at: __n (which is 4) >= _Nm (which is 4)
Abortado
```


# Estruturas vs Arranjos

Tanto as estruturas quanto os arranjos são utilizados para representar informações com dois ou mais itens.

- Usamos estruturas quando cada item da informação tem uma interpretação particular (estrutura Tempo, Janela, etc)

- Usamos arranjos quando os itens da informação são da mesma natureza (todos são nomes, notas, etc)

\pause

No exemplo da loteria, os itens da aposta e do resultados têm a mesma natureza, são todos números, então devemos utilizar arranjos ao invés de estruturas. \pause Vamos altera o código!


# Loteria

<div class="columns">
<div class="column" width="48%">
\tiny

```cpp
// Produz true se n é um dos números
// em sorteados, false caso contrário.
bool sorteado(int n, SeisNumeros sorteados)
{
    bool sorteado = false;
    if (n == sorteados.a) {
        sorteado = true;
    }
    if (n == sorteados.b) {
        sorteado = true;
    }
    if (n == sorteados.c) {
        sorteado = true;
    }
    if (n == sorteados.d) {
        sorteado = true;
    }
    if (n == sorteados.e) {
        sorteado = true;
    }
    if (n == sorteados.f) {
        sorteado = true;
    }
    return sorteado;
}
```
</div>
<div class="column" width="48%">
\tiny

```cpp
// Produz true se n é um dos números
// em sorteados, false caso contrário.
bool sorteado(int n, array<int, 6> sorteados)
{
    bool sorteado = false;
    if (n == sorteados[0]) {
        sorteado = true;
    }
    if (n == sorteados[1]) {
        sorteado = true;
    }
    if (n == sorteados[2]) {
        sorteado = true;
    }
    if (n == sorteados[3]) {
        sorteado = true;
    }
    if (n == sorteados[4]) {
        sorteado = true;
    }
    if (n == sorteados[5]) {
        sorteado = true;
    }
    return sorteado;
}
```
</div>
</div>


# Loteria

<div class="columns">
<div class="column" width="48%">
\tiny

```cpp
// Calcula quantos números da aposta estão em sorteados.
int numero_acertos(SeisNumeros aposta, SeisNumeros sorteados)
{
    int acertos = 0;
    if (sorteado(aposta.a, sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta.b, sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta.c, sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta.d, sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta.e, sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta.f, sorteados)) {
        acertos = acertos + 1;
    }
    return acertos;
}
```
</div>
<div class="column" width="48%">
\tiny

```cpp
// Calcula quantos números da aposta estão em sorteados.
int numero_acertos(array<int, 6> aposta, array<int, 6> sorteados)
{
    int acertos = 0;
    if (sorteado(aposta[0], sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta[1], sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta[2], sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta[3], sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta[4], sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta[5], sorteados)) {
        acertos = acertos + 1;
    }
    return acertos;
}
```
</div>
</div>


# Loteria

E então, o código melhorou? \pause Ainda não! \pause

Agora vamos eliminar a repetição física do código por uma repetição lógica, usando uma nova estrutura de controle. Isso é possível porque os elementos de um arranjo têm a mesma natureza.


# Para cada

Em C++, uma das construções de repetição é o "para cada", que tem a seguinte forma geral \pause

\scriptsize

```cpp
for (Tipo var : arranjo) {
    instruções;
}
```

\pause

\normalsize

O funcionamento do "para cada" é a seguinte \pause

- O primeiro valor de `arranjo` é atribuído para `var` e as `instruções` são executadas; \pause
- O segundo valor de `arranjo` é atribuído para `var` e as `instruções` são executadas; \pause
- ... \pause
- E as sim por diante até que todos os valores de `arranjo` tenham sidos atribuídos para `nome`. \pause

Ou seja, o "para cada" executa as mesmas instruções atribuindo cada valor de `arranjo` para `nome`, por isso ele chama "para cada"!


# Para cada

<div class="columns">
<div class="column" width="48%">
\tiny

```cpp
// Produz true se n é um dos números
// em sorteados, false caso contrário.
bool sorteado(int n, array<int, 6> sorteados)
{
    bool sorteado = false;
    if (n == sorteados[0]) {
        sorteado = true;
    }
    if (n == sorteados[1]) {
        sorteado = true;
    }
    if (n == sorteados[2]) {
        sorteado = true;
    }
    if (n == sorteados[3]) {
        sorteado = true;
    }
    if (n == sorteados[4]) {
        sorteado = true;
    }
    if (n == sorteados[5]) {
        sorteado = true;
    }
    return sorteado;
}
```
</div>
<div class="column" width="48%">

\pause

Nesse código, queremos executar as mesmas instruções, uma vez para cada valor de `sorteados`, então, podemos utilizar o "para cada".

\pause

\scriptsize

```cpp
// Produz true se n é um dos números em sorteados,
// false caso contrário.
bool sorteado(int n, array<int, 6> sorteados)
{
    bool sorteado = false;
    for (int s : sorteados) {
        if (n == s) {
            sorteado = true;
        }
    }
    return sorteado;
}
```
</div>
</div>


# Para cada

<div class="columns">
<div class="column" width="48%">
\tiny

```cpp
// Calcula quantos números da aposta estão em sorteados.
int numero_acertos(array<int, 6> aposta, array<int, 6> sorteados)
{
    int acertos = 0;
    if (sorteado(aposta[0], sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta[1], sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta[2], sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta[3], sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta[4], sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta[5], sorteados)) {
        acertos = acertos + 1;
    }
    return acertos;
}
```
</div>
<div class="column" width="48%">
\pause

Nesse código, queremos executar as mesmas instruções, uma vez para cada valor de `aposta`, então, podemos utilizar o "para cada".

\pause

\tiny

```cpp
// Calcula quantos números da aposta estão em sorteados.
int numero_acertos(array<int, 6> aposta, array<int, 6> sorteados)
{
    int acertos = 0;
    for (int num : aposta) {
        if (sorteado(num, sorteados)) {
            acertos = acertos + 1;
        }
    }
    return acertos;
}
```
</div>
</div>


# Com projetar funções que processam arranjos usando o "para cada"

No exemplo da loteria, vimos como uma repetição física de código pode ser substituída por uma repetição lógica. \pause

Em geral, não precisamos ter uma repetição física de código para depois trocar por uma repetição lógica, podemos projetar a função usando uma repetição lógica diretamente. \pause

Vamos ver como fazer isso!


# Com projetar funções que processam arranjos usando o "para cada"

Quando precisamos processar um arranjo, geralmente queremos calcular valores de forma incremental, analisando um por um os elementos do arranjo. \pause

Esse valores podem ser o resultado final da função ou podem ser usados em outras instruções para determinar o resultado final da função. \pause

Então, para escrever o código que processa os elementos de um arranjo com o "para cada" precisamos responder três perguntas \pause

1) Quais variáveis (valores) queremos calcular? \pause
2) Como as variáveis são inicializados? \pause
3) Como as variáveis são atualizados? \pause

Para responder cada pergunta, usamos os exemplos e perguntas auxiliares.


# Com projetar funções que processam arranjos usando o "para cada"

a) Quais variáveis (valores) queremos calcular? \pause

   Podemos calcular o resultado final da função apenas analisando os elementos do arranjo, sem precisar fazer nada depois? \pause

   Se sim, então esse é o valor que queremos calcular. \pause

   Se não, temos que pensar em valores que podem nos ajudar com a resposta da função e esses são os valores que queremos calcular. \pause

   Em ambos os casos, criamos variáveis para armazenar esses valores.


# Com projetar funções que processam arranjos usando o "para cada"

b) Como as variáveis são inicializados? \pause

   Se o arranjo não tivesse nenhum elemento, qual seria o valor esperado para as variáveis? \pause

   Use esses valores para inicializar as variáveis.


# Com projetar funções que processam arranjos usando o "para cada"

c) Como as variáveis são atualizadas? \pause

   Pegue alguns exemplos e suponha que o "para cada" já tenha processado de forma correta todos os elementos do arranjo, exceto o último, e determine os valores que as variáveis deveriam ter. \pause

   Agora considere que o último elemento está sendo processado e determine quais operações são necessárias para modificar os valores das variáveis para que elas fiquem com o valor final esperado. \pause

   Generalize e escreva o código para fazer essas operações.


# Soma

Projete uma função que some todos os valores de um arranjo de 7 números.


# Soma

<div class="columns">
<div class="column" width="58%">
\scriptsize

```cpp
// Soma os valores de numeros.
int soma(array<int, 7> numeros)
{
    return 0;
}

examples
{
    check_expect(soma({1, 0, 1, 0, 5, 0, -7}), 0);
    check_expect(soma({1, 0, 1, 0, 5, 0, 10}), 17);
    check_expect(soma({0, -4, 1, 0, -5, -10, 0}), -18);
}
```

\small

\pause

1) Quais variáveis (valores) queremos calcular? \pause A soma. \pause
2) Como as variáveis são inicializados? \pause A soma é inicializada com 0. \pause
3) Como as variáveis são atualizados? \pause A soma é atualizada somando elemento atual. \pause

</div>
<div class="column" width="38%">
\scriptsize

```cpp
// Soma os valores de numeros.
int soma(array<int, 7> numeros)
{
    int soma = 0;
    for (int num : numeros) {
        soma = soma + num;
    }
    return soma;
}
```
</div>
</div>


# Máximo

Projete uma função que encontre o valor máximo de um arranjo com 5 números.


# Máximo

<div class="columns">
<div class="column" width="58%">
\scriptsize

```cpp
// Encontra o valor máximo de numeros.
int maximo(array<int, 5> numeros)
{
    return 0;
}

examples
{
    check_expect(maximo({5, 4, 1, 0, 7}), 7);
    check_expect(maximo({1, -5, 8, 1, 2}), 8);
    check_expect(maximo({-4, -6, -1, -1, -3}), -1);
}
```

\small

\pause

1) Quais variáveis (valores) queremos calcular? \pause O maximo. \pause
2) Como as variáveis são inicializados? \pause O máximo é inicializado com o primeiro elemento. \pause
3) Como as variáveis são atualizados? \pause Se o elemento atual é maior que o máximo, ele passa a ser o máximo.

</div>
<div class="column" width="38%">
\scriptsize

```cpp
// Encontra o valor máximo de numeros.
int maximo(array<int, 5> numeros)
{
    int max = numeros[0];
    for (int n : numeros) {
        if (n > max) {
            max = n;
        }
    }
    return max;
}
```
</div>
</div>


# Concatenação

Projete uma função que junte todas as string de um arranjo de 5 strings.


# Concatenação

\scriptsize

```cpp
// Concatena as strings de strs uma após a outra.
string concatena(array<string, 5> strs)
{
    return "";
}

examples
{
    check_expect(concatena({"Ola", " ", "mundo", "", "!"}), "Ola mundo!");
    check_expect(concatena({"ab", "c", "de", "", "fgh"}), "abcdefgh");
}
```

\pause

\small

1) Quais variáveis (valores) queremos calcular? \pause A concatenação das strings. \pause
2) Como as variáveis são inicializados? \pause A concatenação é inicializada com vazio. \pause
3) Como as variáveis são atualizados? \pause A concatenação é atualizada concatenando o elemento atual.


# Concatenação

\scriptsize

```cpp
// Concatena as strings de strs uma após a outra.
string concatena(array<string, 5> strs)
{
    string concatenacao = "";
    for (string str : strs) {
        concatenacao = concatenacao + str;
    }
    return concatenacao;
}
```


# Positivos ou negativos

Projete uma função que verifique se um arranjo com 5 números inteiros positivos tem mais números pares ou ímpares.


# Positivos ou negativos

Definição dos tipos de dados

\scriptsize

```cpp
// O tipo de um número.
enum Tipo {
    Positivo,
    Negativo,
    Nenhum,
}
```


# Positivos ou negativos

\scriptsize

```cpp
// Verifica se existem mais números positivos ou negativos no arranjo numeros.
// Devolve Positivo se existem mais positivos do que negativos.
// Devolve Negativo se existem mais negativos do que positivos.
// Devolve Nenhum se a quantidade de positivos é igual a de negativos.
Tipo mais_positivos_ou_negativos(array<int, 5> numeros) {
    return Nenhum;
}

examples {
    check_expect(mais_positivos_ou_negativos({1, 2, 3, -1, 0}), Positivo);
    check_expect(mais_positivos_ou_negativos({1, 2, 3, -1, -2}), Positivo);
    check_expect(mais_positivos_ou_negativos({-4, 2, 3, -1, -2}), Negativo);
    check_expect(mais_positivos_ou_negativos({-4, 2, 3, 0, -2}), Nenhum);
}
```

\pause

\small

1) Quais variáveis (valores) queremos calcular? \pause A quantidade de positivos e negativos. \pause
2) Como as variáveis são inicializados? \pause Com zero. \pause
3) Como as variáveis são atualizados? \pause Se o elemento atual é positivo, incrementa o número de positivos, se o elemento atual é negativo, incrementa o número de negativos.


# Positivos ou negativos

\scriptsize

```cpp
Tipo mais_positivos_ou_negativos(array<int, 5> numeros)
{
    int num_positivos = 0;
    int num_negativos = 0;
    for (int num : numeros) {
        if (num > 0) {
            num_positivos = num_positivos + 1;
        } else if (num < 0) {
            num_negativos = num_negativos + 1;
        }
    }
    Tipo tipo = Nenhum;
    if (num_positivos > num_negativos) {
        tipo = Positivo;
    } else if (num_negativos > num_positivos) {
        tipo = Negativo;
    }
    return tipo;
}
```


# Arranjos dinâmicos

O exemplo da loteria requeria arranjos com 6 elementos. \pause

Já para os demais exemplos, o tamanho fixo do arranjo parece uma imposição artificial. \pause

De fato, o mais comum é problemas que precisam de arranjos de tamanho dinâmico. \pause

Em C++ tipo arranjo de tamanho dinâmico (ou arranjos dinâmicos, ou vetores, ou listas, ou ...) é chamado de `vector` e está disponível através da biblioteca `vector`. \pause

Vamos ver as operações básicas com arranjos dinâmicos.


# Arranjos dinâmicos

\small

A forma de inicializar arranjos dinâmicos é similar a forma de inicializar arranjos de tamanho fixo, com exceção de que não precisamos especificar a quantidade de elementos.

\scriptsize

```cpp
#include <vector>
...
examples {
    vector<int> valores = {10, 4, 9, -1};
    vector<string> nomes = {"joao", "jose", "maria"};
```

\pause

\small

Assim com para `array`, também acessamos e modificamos os elementos de um `vector` com índices e/ou com o método `at`

\scriptsize

```cpp
    check_expect(valores[0], 10);
    check_expect(nomes[2], "maria");

    check_expect(valores.at(1), 4);
    valores.at(1) = 25;
    check_expect(valores[1], 25);
}
```


# Tamanho e adição no final

Como `vector` tem tamanho dinâmico, podemos consultar o tamanho (quantidade de elementos) atual com o método `size`

\small

```cpp
vector<int> idades = {2, 7, 1, 9};

check_expect(idades.size(), 4);
```

\pause

\normalsize

Para adicionar um novo elemento no final do arranjo, utilizamos o método `push_back`

\small

```cpp
idades.push_back(4);

check_expect(idades.size(), 5);
check_expect(idades, (vector<int> {2, 7, 1, 9, 4}));
```


# {.plain}

\Large
**ATENÇÃO**: quando queremos utilizar um `vector`, um `array` ou uma estrutura como **resultado esperado** em um `checke_expect` precisamos colocar o resultado todo entre parênteses e nome do tipo antes de `{`

```cpp
check_expect(..., (array<string, 2> {"casa", "agua"}));
check_expect(..., (vector<int> {4, 10}));
check_expect(..., (Janela {10, 40, 100, 200}));
```


# Soma

Utilizamos o mesmo processo para escrever a implementação de funções que processam arranjos de tamanho fixo e arranjos de tamanho dinâmico.

\scriptsize

```cpp
// Soma os elementos de valores.
int soma(vector<int> valores)
{
    int soma = 0;
    for (int num : valores) {
        soma = soma + num;
    }
    return soma;
}

examples
{
    check_expect(soma({}), 0);
    check_expect(soma({3, 1}), 4);
    check_expect(soma({4, 6, -2, 0, 1}), 9);
}
```


# Eleições

Uma eleição é realizada com apenas dois candidatos. Cada eleitor pode votar ou no primeiro candidato, ou no segundo candidato ou ainda, votar em branco. O candidato que tiver mais votos ganha a eleição. Se os votos em branco forem mais do que 50% do total de votos, novas eleições devem ser convocadas. Projete uma função que receba como entrada uma lista não vazia de votos e determine qual foi o resultado da eleição. Dica: deseje uma função auxilar!


# Análise

Determinar o resultado de uma eleição. \pause

- O voto pode ser em um de dois candidatos ou em braco; \pause
- Se mais que 50% dos votos forem brancos ou se os candidatos tiverem o mesmo número de votos, é necessário uma nova eleição. \pause
- Se não for necessário uma nova eleição, ganha quem tiver mais votos.


# Definição dos tipos de dados

\footnotesize

```cpp

// Os votos serão representados por vector<Voto>.

// Um voto em uma eleição.
enum Voto {
    Candidato1,
    Candidato2,
    Branco,
};

// O resultado de uma eleição.
enum ResultadoEleicao {
    Venceu1,
    Venceu2,
    NovasEleicoes,
};
```


# Especificação

\scriptsize

```cpp
// Apura o resultado da eleicao considerando os votos no arranjo votos.
// - Produz NovasEleicoes se mais do que 50% do total de votos for branco ou a
// quantidade de votos do Candidato1 for igual ao do Candidato2.
// - Senão, produz Venceu1 se o Candidato1 teve mais votos ou Venceu2 se o
// Candidato2 teve mais votos.
ResultadoEleicao apura_eleicao(vector<Voto> votos)
{
    return NovasEleicoes;
}

examples
{
    check_expect(apura_eleicao({Candidato1, Candidato2, Candidato1, Branco}), Venceu1);
    check_expect(apura_eleicao({Candidato2, Candidato2, Candidato1, Branco}), Venceu2);
    check_expect(apura_eleicao({Candidato2, Candidato1, Candidato1, Candidato2}), NovasEleicoes);
    check_expect(apura_eleicao({Candidato1, Candidato1, Branco, Branco}), Venceu1);
    check_expect(apura_eleicao({Candidato2, Candidato2, Branco, Branco}), Venceu2);
    check_expect(apura_eleicao({Candidato1, Candidato2, Branco, Branco}), NovasEleicoes);
    check_expect(apura_eleicao({Candidato2, Candidato2, Branco, Branco, Branco}), NovasEleicoes);
}
```


# Implementação

Vamos seguir a dica do enunciado e desejar a função `conta_votos`, que conta um determinado tipo de voto.

\scriptsize

```cpp
ResultadoEleicao apura_eleicao(vector<Voto> votos) {
    int num_votos1 = conta_votos(votos, Candidato1);
    int num_votos2 = conta_votos(votos, Candidato2);
    int num_brancos = conta_votos(votos, Branco);

    ResultadoEleicao resultado;
    if (num_brancos > votos.size() / 2) {
        resultado = NovasEleicoes;
    } else if (num_votos1 > num_votos2) {
        resultado = Venceu1;
    } else if (num_votos2 > num_votos1) {
        resultado = Venceu2;
    } else {
        resultado = NovasEleicoes;
    }
    return resultado;
}
```


# Lista de pendências

Adicionamos `conta_votos` na lista de pendências e fazemos o projeto da função.

\pause

\scriptsize

```cpp
// Conta quantos votos no arranjo votos é igual ao alvo.
int conta_votos(vector<Voto> votos, Voto alvo)
{
    return 0;
}

examples
{
    vector<Voto> votos = {Candidato2, Candidato1, Branco, Candidato1, Candidato2, Candidato1};
    check_expect(conta_votos(votos, Candidato1), 3);
    check_expect(conta_votos(votos, Candidato2), 2);
    check_expect(conta_votos(votos, Branco), 1);
}
```


# Implementação

<div class="columns">
<div class="column" width="48%">
1) Quais variáveis (valores) queremos calcular? \pause A quantidade de votos iguais ao alvo. \pause
2) Como as variáveis são inicializados? \pause A quantidade é inicializada com 0. \pause
3) Como as variáveis são atualizados? \pause A quantidade é atualizada em 1 quanto o elemento atual for igual ao alvo. \pause
</div>
<div class="column" width="48%">
\scriptsize
```cpp
int conta_votos(vector<Voto> votos, Voto alvo)
{
    int num = 0;
    for (Voto voto : votos) {
        if (voto == alvo) {
            num = num + 1;
        }
    }
    return num;
}
```
</div>
</div>

\pause

Verificação: \pause Ok. \pause

Revisão: \pause Ok.


# Índice do máximo

Projete uma função que encontre o índice (posição) da primeira ocorrência do valor máximo de um arranjo dinâmico não vazio.


# Especificação

\small

```cpp
// Encontra o índice da primeira ocorrência do valor máximo de valores.
int indice_maximo(vector<int> valores)
{
    return 0;
}

examples
{
    check_expect(indice_maximo({5}), 0);
    check_expect(indice_maximo({5, 5}), 0);
    check_expect(indice_maximo({5, 7, 5}), 1);
    check_expect(indice_maximo({5, 7, 5, 8}), 3);
}
```


# Implementação

1) Quais variáveis (valores) queremos calcular? \pause O índice da primeira ocorrência do máximo (`imax`) e o índice o elemento atual (`i`). \pause
2) Como as variáveis são inicializados? \pause Os dois valores são inicializados com 0. \pause
3) Como as variáveis são atualizados? \pause `imax` é atualizado para `i` se o elemento atual for maior que o elemento na posição `imax`. `i` é incrementado com 1.


# Implementação

\scriptsize

```cpp
int indice_maximo(vector<int> valores)
{
    int i = 0;
    int imax = 0;
    for (int valor : valores) {
        if (valor > valores[imax]) {
            imax = i;
        }
        i = i + 1;
    }
    return imax;
}
```

\pause

\normalsize

Verificação: \pause Ok.

Revisão: \pause Não está claro a relação de `i` com `valor`... \pause podemos mudar `valor` para `valores[i]`.


# Implementação

\scriptsize

```cpp
int indice_maximo(vector<int> valores)
{
    int i = 0;
    int imax = 0;
    for (int valor : valores) {
        if (valores[i] > valores[imax]) {
            imax = i;
        }
        i = i + 1;
    }
    return imax;
}
```


\pause

\normalsize

E agora? \pause `valor` não é mais utilizado. \pause

A questão é que não queremos mais acessar os elementos do arranjo diretamente, queremos usar um índice para acessar os elementos. \pause Vamos utilizar o laço "para", que é mais apropriado para essa situação.


# Laço "para"

O laço "para" tem a seguinte forma geral

\small

```c++
for(inicialização; condição; atualização) {
   instruções;
}
```

O funcionamento do "para" é o seguinte \pause

- A inicialização é executada \pause
- Em seguida a condição é verificada, se ela for `true`{.cpp} as instruções são executadas, senão o laço termina \pause
- Depois a atualização é executada e a condição é verificada novamente, se ele for `true`{.cpp}...


# Exemplo - soma

<div class="columns">
<div class="column" width="48%">

\scriptsize

```cpp
// Soma os elementos de valores.
int soma(vector<int> valores)
{
    int soma = 0;
    for (int num : valores) {
        soma = soma + num;
    }
    return soma;
}
```
</div>
<div class="column" width="48%">

\pause

\scriptsize

```cpp
// Soma os elementos de valores.
int soma(vector<int> valores)
{
    int soma = 0;
    for (int i = 0; i < valores.size(); i = i + 1) {
        soma = soma + valores[i];
    }
    return soma;
}
```
</div>
</div>

\pause

Qual das duas implementações é mais simples? \pause A que usa o "para cada"! \pause Por quê? \pause

Porque a variável do laço (`num`) é controlada implicitamente, já no caso do "para" a variável do laço (`i`) é controlado explicitamente.


# "para" vs "para cada"

Mas então, quando usamos o "para" ao invés do "para cada"? \pause Quando queremos mais controle sobre o laço! \pause

Abrimos mão da simplicidade pela flexibilidade. \pause

"para cada": quando queremos analisar os elementos na sequência. \pause

"para": para os demais casos (queremos os índices, queremos analisar mais que um elemento de uma vez, não precisamos analisar todos os elementos, etc).


# Como projetar funções que processam arranjos usando o "para"

Assim como no "para cada", precisamos responder as três perguntas \pause

1) Quais variáveis (valores) queremos calcular?
2) Como as variáveis são inicializados?
3) Como as variáveis são atualizados?

\pause

Mais alguma coisa? \pause Sim! \pause Também precisamos definir os itens do laço \pause

1) Quais são as variáveis do laço e como elas são inicializadas? \pause
2) Qual a condição do laço? \pause
3) Como as variáveis do laço são atualizadas?

\pause

Note em que algumas situações as variáveis do laço são o que queremos calcular.


# Índice do máximo

<div class="columns">
<div class="column" width="48%">
\scriptsize

```cpp
int indice_maximo(vector<int> valores)
{
    int i = 0;
    int imax = 0;
    for (int valor : valores) {
        if (valores[i] > valores[imax]) {
            imax = i;
        }
        i = i + 1;
    }
    return imax;
}
```
</div>

<div class="column" width="48%">

\pause

Fazendo uma "tradução" direta obtemos \pause

\scriptsize

```cpp
int indice_maximo(vector<int> valores)
{
    int imax = 0;
    for (int i = 0; i < valores.size(); i = i + 1) {
        if (valores[i] > valores[imax]) {
            imax = i;
        }
    }
    return imax;
}
```
</div>
</div>

Qual é mais adequada? \pause A que usa o "para". \pause

Podemos melhorar? \pause Sim, `i` pode começar com `1`, dessa forma não comparamos `valores[0]` com ele mesmo na primeira iteração.


# Inserção

Projete uma função que receba como entrada um arranjo dinâmico de números, uma posição $i$ e um número $n$ e devolva um novo arranjo com $n$ adicionado na posição $i$ do arranjo de entrada.


# Especificação

\scriptsize

```cpp
// Cria um nova arranjo inserindo o valor no índice pos de valores.
// Requer que 0 <= pos <= valores.size().
vector<int> insere_posicao(vector<int> valores, int pos, int valor)
{
    return {};
}

examples {
    check_expect(insere_posicao({}, 0, 10), (vector<int> {10}));
    check_expect(insere_posicao({8}, 0, 10), (vector<int> {10, 8}));
    check_expect(insere_posicao({8}, 1, 10), (vector<int> {8, 10}));
    check_expect(insere_posicao({2, 8}, 0, 3), (vector<int> {3, 2, 8}));
    check_expect(insere_posicao({2, 8}, 1, 3), (vector<int> {2, 3, 8}));
    check_expect(insere_posicao({2, 8}, 2, 3), (vector<int> {2, 8, 3}));
}
```


# Implementação

<div class="columns">
<div class="column" width="48%">
\scriptsize

```cpp
vector<int> insere_posicao(
     vector<int> valores,
     int pos,
     int valor)
{
    vector<int> resultado = {};
    for (int i = 0; i < valores.size(); i = i + 1) {
        if (i == pos) {
            resultado.push_back(valor);
        }
        resultado.push_back(valores[i]);
    }

    return resultado;
}
```
</div>
<div class="column" width="48%">
\pause

Verificação \pause

\scriptsize

```
Ran 6 tests.
3 of the 6 tests passed.
Failures
  insere_posicao.cpp at line 35:
    left : std::vector<int> {}
    right: std::vector<int> {10}

  insere_posicao.cpp at line 37:
    left : std::vector<int> {8}
    right: std::vector<int> {8, 10}

  insere_posicao.cpp at line 40:
    left : std::vector<int> {2, 8}
    right: std::vector<int> {2, 8, 3}
```
</div>
</div>


# Implementação

\scriptsize

```cpp
vector<int> insere_posicao(vector<int> valores, int pos, int valor) {
    vector<int> resultado = {};
    for (int i = 0; i < valores.size(); i = i + 1) {
        if (i == pos) {
            resultado.push_back(valor);
        }
        resultado.push_back(valores[i]);
    }
    if (pos == valores.size()) {
        resultado.push_back(valor);
    }
    return resultado;
}
```

\pause

\normalsize

Verificação: \pause Ok. \pause

Revisão: o código tem um caso especial... \pause O que podemos fazer? \pause Separar em três etapas, inserir os elementos antes de `pos`, inserir o `valor`, inserir os elementos de `pos` até o final.


# Implementação

\scriptsize

```cpp
vector<int> insere_posicao(vector<int> valores, int pos, int valor)
{
    vector<int> resultado = {};

    for (int i = 0; i < pos; i = i + 1) {
        resultado.push_back(valores[i]);
    }

    resultado.push_back(valor);

    for (int i = pos; i < valores.size(); i = i + 1) {
        resultado.push_back(valores[i]);
    }

    return resultado;
}
```


# Remoção

Projete uma função que receba como entrada um arranjo dinâmico de números e uma posição e devolva um novo arranjo sem o elemento da posição especificada.


# Especificação

\scriptsize

```cpp
// Cria um nova arranjo removendo o elemento da posição pos de valores.
// Requer que 0 <= pos < valores.size().
vector<int> remove_posicao(vector<int> valores, int pos)
{
    return {};
}

examples {
    check_expect(remove_posicao({8}, 0), (vector<int> {}));
    check_expect(remove_posicao({2, 8}, 0), (vector<int> {8}));
    check_expect(remove_posicao({2, 8}, 1), (vector<int> {2}));
    check_expect(remove_posicao({7, 2, 8}, 0), (vector<int> {2, 8}));
    check_expect(remove_posicao({7, 2, 8}, 1), (vector<int> {7, 8}));
    check_expect(remove_posicao({7, 2, 8}, 2), (vector<int> {7, 2}));
}
```


# Implementação

\scriptsize

```cpp
// Cria um nova arranjo removendo o elemento da posição pos de valores.
// Requer que 0 <= pos < valores.size().
vector<int> remove_posicao(vector<int> valores, int pos)
{
    vector<int> resultado = {};

    for (int i = 0; i < pos; i = i + 1) {
        resultado.push_back(valores[i]);
    }

    for (int i = pos + 1; i < valores.size(); i = i + 1) {
        resultado.push_back(valores[i]);
    }

    return resultado;
}
```


# Verificação de ordem

Projete uma função que verifique se um arranjo de valores está em ordem não decrescente.


# Especificação

\scriptsize

```cpp
// Produz true se os elementos de valores estão em ordem não decrescente, false
// caso contrário.
bool ordem_nao_decrescente(vector<int> valores)
{
    return false;
}

examples {
    check_expect(ordem_nao_decrescente({}), true);
    check_expect(ordem_nao_decrescente({3}), true);
    check_expect(ordem_nao_decrescente({1, 3}), true);
    check_expect(ordem_nao_decrescente({3, 1}), false);
    check_expect(ordem_nao_decrescente({1, 3, 3}), true);
    check_expect(ordem_nao_decrescente({3, 3, 3}), true);
    check_expect(ordem_nao_decrescente({3, 2, 3}), false);
    check_expect(ordem_nao_decrescente({3, 4, 2}), false);
    check_expect(ordem_nao_decrescente({1, 2, 3, 4, 5, 6}), true);
    check_expect(ordem_nao_decrescente({1, 2, 3, 2, 5, 6}), false);
}
```


# Implementação

A implementação desse função parece ser diferente das anteriores. \pause

Antes só precisávamos analisar um único elemento do arranjo a cada iteração, agora temos que analisar dois elementos. \pause

Como podemos proceder nesse caso? \pause

Vamos resolver o problema para arranjos com 5 elementos usando repetição física de código e depois vamos tentar transformação essa repetição física em uma repetição lógica.


# Implementação

<div class="columns">
<div class="column" width="48%">
\scriptsize

```cpp
bool ordem_nao_decrescente(array<int, 5> valores)
{
    bool em_ordem = true;
    if (valores[0] > valores[1]) {
        em_ordem = false;
    }
    if (valores[1] > valores[2]) {
        em_ordem = false;
    }
    if (valores[2] > valores[3]) {
        em_ordem = false;
    }
    if (valores[3] > valores[4]) {
        em_ordem = false;
    }
    return em_ordem;
}
```
</div>
<div class="column" width="48%">
\pause

1) Quais são as variáveis do laço e como elas são inicializadas? \pause `int i = 1`{.cpp} \pause
2) Qual a condição do laço? \pause `i < valores.size()`{.cpp} \pause
3) Como as variáveis do laço são atualizadas? \pause `i = i + 1`{.cpp}
</div>
</div>


# Implementação

\scriptsize

```cpp
// Produz true se os elementos de valores estão em ordem não decrescente, false
// caso contrário.
bool ordem_nao_decrescente(vector<int> valores)
{
    bool em_ordem = true;
    for (int i = 1; i < valores.size(); i = i + 1) {
        if (valores[i - 1] > valores[i]) {
            em_ordem = false;
        }
    }
    return em_ordem;
}
```

\pause

\normalsize

Verificação: \pause Ok. \pause

Revisão: \pause mesmo encontrando valores "fora de ordem" a repetição continua e analisa todos os elementos de `valores`... \pause A repetição só precisa continuar enquanto `em_ordem` for `true`{.cpp}.


# Implementação

\scriptsize

```cpp
// Produz true se os elementos de valores estão em ordem não decrescente, false
// caso contrário.
bool ordem_nao_decrescente(vector<int> valores)
{
    bool em_ordem = true;
    for (int i = 1; i < valores.size() && em_ordem; i = i + 1) {
        if (valores[i - 1] > valores[i]) {
            em_ordem = false;
        }
    }
    return em_ordem;
}
```


# Verificação de palíndromo

Projete uma função que verifique se um arranjo de valores é palíndromo.


# Especificação

\scriptsize

```cpp
// Produz true se valores é palíndromo, isto é, os elementos de valores vistos
// da esquerda para direita e da direita para esquerda são os mesmos. Produz
// false se valores não é palíndromo.
bool palindromo(vector<int> valores)
{
    return false;
}

examples {
    check_expect(palindromo({}), true);
    check_expect(palindromo({1}), true);
    check_expect(palindromo({2, 1}), false);
    check_expect(palindromo({1, 2}), false);
    check_expect(palindromo({2, 2}), true);
    check_expect(palindromo({2, 1, 2}), true);
    check_expect(palindromo({4, 4, 2}), false);
    check_expect(palindromo({2, 1, 1, 2}), true);
    check_expect(palindromo({2, 0, 1, 2}), false);
    check_expect(palindromo({2, 0, 1, 0, 2}), true);
}
```


# Implementação

Assim como para a função `ordem_nao_decrescente`, vamos resolver o problema para 5 elementos usando repetição física de código.


# Implementação

<div class="columns">
<div class="column" width="40%">
\scriptsize

```cpp
bool palindromo(array<int, 5> valores)
{
    bool palindromo = true;
    if (valores[0] != valores[4]) {
        palindromo = false;
    }
    if (valores[1] > valores[3]) {
        palindromo = false;
    }
    return palindromo;
}
```
</div>
<div class="column" width="55%">
\pause

1) Quais são as variáveis do laço e como elas são inicializadas? \pause

   `int i = 0, j = valores.size() - 1`{.cpp} \pause
2) Qual a condição do laço? \pause

   `i < j`{.cpp} \pause
3) Como as variáveis do laço são atualizadas? \pause

   `i = i + 1, j = j - 1`{.cpp}
</div>
</div>


# Implementação

\scriptsize

```cpp
// Produz true se valores é palíndromo, isto é, os elementos de valores vistos
// da esquerda para direita e da direita para esquerda são os mesmos. Produz
// false se valores não é palíndromo.
bool palindromo(vector<int> valores)
{
    bool palindromo = true;
    for (int i = 0, j = valores.size() - 1; i < j && palindromo; i = i + 1, j = j - 1) {
        if (valores[i] != valores[j]) {
            palindromo = false;
        }
    }
    return palindromo;
}
```


# Exercício

A escola do seu irmão mais novo está fazendo um coletânea de ditos populares. Cada aluno da escola escolheu um dito popular e a escola agregou todos eles em um arquivo texto (um dito por linha). Agora a escola precisa eliminar os ditos repetidos e classificá-los em ordem, mas ela não sabe como fazer isso. Você pode ajudar?


# Análise

Classificar uma coleção de ditos em ordem e eliminar ditos repetidos. \pause

- Os ditos devem ser obtidos de um arquivo texto onde cada linha tem um dito.

\pause

Devemos fazer um programa completo e não apenas uma função!

\pause

Por onde começamos?

\pause

Assumimos que temos os dados de entrada e prosseguimos com o projeto de uma função! \pause Depois fazemos a parte de entrada e saída dos dados. \pause

Mas antes, vamos ver um tipo que irá nos ajudar a resolver o problema: conjuntos.


# Conjuntos

Um conjunto em C++ podem ser representado pelo tipo `set`, definido na biblioteca `set`.

\pause

Um conjunto é semelhante a um arranjo dinâmico, mas não contém elementos repetidos, os elementos são mantidos em ordem e não são indexados.


# Conjuntos

<div class="columns">
<div class="column" width="48%">
\scriptsize

```cpp
set<int> s = {3, 1, 4};

check_expect(s, (set<int> {1, 4, 3}));

s.insert(5);
s.insert(4);
s.insert(1);

check_expect(s.size(), 4);
check_expect(s, (set<int> {1, 5, 4, 3}));

s.erase(10);
s.erase(1);
s.erase(3);

check_expect(s, (set<int> {4, 5}));

check_expect(s.count(4), 1);
check_expect(s.count(3), 0);
```

</div>
<div class="column" width="48%">

\pause

Inserir um elemento existente ou remover um elemento inexistente não altera o conjunto.

\pause

Podemos verificar se um conjunto contém um elemento utilizando o método `count`.

</div>
</div>


# Conjuntos

Para analisar todos os elementos de um conjunto, usamos o "para cada" \pause

\footnotesize

```cpp
set<int> valores = {7, 10, 2};

int soma = 0;

for (int valor : valores) {
    soma = soma + valor;
}

check_expect(soma, 19);
```

\pause

\normalsize

É isso! \pause Agora vamos voltar para o problema dos ditos.


# Definição dos tipos de dados

Os ditos de entrada serão representados por um arranjo de strings. \pause

Vamos usar um conjunto na implementação...


# Especificação

\scriptsize

```cpp
// Seleciona uma ocorrência de cada dito do arranjo ditos e classifica o
// resultado em ordem alfabética.
vector<string> classifica_ditos_unicos_em_ordem(vector<string> ditos) {
    return {};
}

examples
{
    string dito1 = "Esmola demais até santo desconfia";
    string dito2 = "Diga com quem anda que lhe direi quem és";
    string dito3 = "Saco vazio não para em pé";
    check_expect(classifica_ditos_unicos_em_ordem({}),
                 (vector<string> {}));

    check_expect(classifica_ditos_unicos_em_ordem({dito1, dito2, dito1}),
                 (vector<string> {dito2, dito1}));

    check_expect(classifica_ditos_unicos_em_ordem({dito3, dito1, dito2, dito1, dito3, dito2}),
                 (vector<string> {dito2, dito1, dito3}));
}
```


# Implementação

Precisamos analisar todos os elementos da entrada e podemos fazer isso na ordem que eles aparecem, então pode usar o "para cada". \pause

O que queremos calcular com o "para cada"? \pause

Calcular a resposta diretamente parece complicado pois teríamos que evitar as repetições de ditos e ainda classificar o arranjo de saída. \pause

Podemos computar um resultado intermediário mais facilmente que nos ajude a computar o resultado da função? \pause Sim! \pause Vamos criar um conjunto com os ditos, eles serão únicos e estarão em ordem! \pause E depois? \pause

Criamos o arranjo de resposta com os elementos do conjunto.


# Implementação

\scriptsize

```cpp
// Seleciona uma ocorrência de cada dito do arranjo ditos e classifica o
// resultado em ordem alfabética.
vector<string> classifica_ditos_unicos_em_ordem(vector<string> ditos)
{
    // Usamos um conjunto para selecionar apenas uma ocorrência de cada dito e
    // também classificá-los em ordem.
    set<string> unicos = {};
    for (string dito : ditos) {
        unicos.insert(dito);
    }

    vector<string> result = {};

    for (string dito : unicos) {
        result.push_back(dito);
    }

    return result;
}
```


# Programa

Temos a função que calcula o que queremos, e agora, o que precisamo fazer para ter um programa? \pause

Escrever o código que faz a entrada e saída. \pause Vamos desejar por funções auxiliares e escrever a função principal. \pause

\scriptsize

```cpp
int main()
{
    // Entrada
    vector<string> ditos = le_ditos();

    // Processamento
    vector<string> ditos_unicos = classifica_ditos_unicos_em_ordem(ditos);

    // Saída
    escreve_ditos(ditos_unicos);
}
```


# Pendências

\scriptsize

```cpp
// Produz um arranjo de ditos lendo um dito por linha da entrada padrão.
vector<string> le_ditos()
{
    return {};
}

// Escreve na saída padrão os ditos.
void escreve_ditos(vector<string> ditos)
{
}
```

\pause

\normalsize

O que essas funções têm de diferente das funções que temos escrito até agora? \pause

A função `le_ditos` não tem argumentos de entrada e a função `escreve_ditos` não tem resposta (usamos o tipo `void`{.cpp} para representar isso). \pause

Por isso não temos come escrever os exemplos para essas funções! Veja o vídeo da aula para mais informações.


# Implementação

A implementação da função `escreve_ditos` é direta: \pause

\scriptsize

```cpp
// Escreve na saída padrão os ditos.
void escreve_ditos(vector<string> ditos)
{
    for (string dito: ditos) {
        cout << dito << endl;
    }
}
```


# Implementação

Mas e a implementação da função `le_ditos`? \pause Ler um dito para simples \pause

\scriptsize

```cpp
vector<string> le_ditos()
{
    vector<string> ditos = {};
    string dito;

    getline(cin, dito);
    ditos.push_back(dito);

    return ditos;
}
```

\pause

\normalsize

Mas como ler uma quantidade indeterminada de ditos? \pause Precisamos de uma nova forma de repetição!


# Enquanto

A forma geral do "enquanto" é:

\scriptsize

```cpp
while (condição) {
    instruções;
}
```

\pause

\normalsize

O funcionamento do "enquanto" é a seguinte \pause

- A condição é verificada; \pause
- Se a condição for `true`{.cpp}, as instruções são executadas e processo começa novamente.\pause
- Se a condição for `false`{.cpp}, o laço é finalizado. \pause

Ou seja, o "enquanto" executa as mesmas instruções enquanto a condição for verdadeira.


# Exemplo

\scriptsize

```cpp
vector<int> valores = {1, 2, 4};

int i = 0;
int soma = 0;
while (i < valores.size()) {
    soma = soma + valores[i];
}

check_expect(soma, 7).
```


# Quando usar o "enquanto"?

Claro, não precisamos do "enquanto" para fazer a soma dos valores de um arranjo, podemos usar o "para cada". \pause

Então, quando usamos o "enquanto"? \pause

Em geral, quando precisamos de uma repetição que não dependa de uma coleção de valores. \pause Mas também podemos usar o "enquanto" quando precisamos analisar os elementos de um arranjo e o "para" e o "para cada" não são adequados (deixa o código mais complicado).


# Implementação

Agora podemos voltar para a implementação do `le_ditos`. \pause

A função `getline` produz um valor que pode ser usado com uma condição. Se `getline` conseguir ler uma linha da entrada, o valor produzido corresponde a `true`{.cpp}, caso contrário, o valores corresponde a `false`{.cpp}. \pause

Então, a ideia para implementar a função `le_ditos` é: \pause

- Enquanto conseguiu ler uma linha, adiciona a linha em um arranjo.


# Implementação

\scriptsize

```cpp
// Produz um arranjo de ditos lendo um dito por linha da entrada padrão.
vector<string> le_ditos()
{
    vector<string> ditos = {};
    string dito;

    while (getline(cin, dito)) {
        ditos.push_back(dito);
    }

    return ditos;
}
```


# Execução do programa

O programa está pronto! Agora podemos executar e testar o programa. \pause

Veja o vídeo da aula para informações sobre redirecionamento de entrada e saída.


# Exercício

Projete uma função que separe as "partes" de uma string usando um espaço como delimitador.


# Especificação

\scriptsize

```cpp
// Produz uma lista das "partes" de s usando espaços como delimitador.
vector<string> separa(string s)
{
    return {};
}

examples
{
    check_expect(separa(""), (vector<string> {}));
    check_expect(separa("casa"), (vector<string> {"casa"}));
    check_expect(separa("Seu Jorge cantou a musica."),
                 (vector<string> {"Seu", "Jorge", "cantou", "a", "musica."}));
}
```


# Implementação

Como fazer a implementação? \pause Vamos precisar de uma repetição, \pause mas qual tipo? \pause Diferente das repetições que fizemos anteriormente, esta não depende de uma "coleção" de valores, então vamos usar o "enquanto". \pause

E como fazer a repetição? \pause Vamos tentar generalizar a solução de alguns exemplos específicos.


# Implementação

\scriptsize

```cpp
string s = "Seu Jorge cantou a musica.";
vector<string> palavras = {};
```

\pause

```cpp
s.find(" ", 0); // a partir do indice 0 ("S"), encontra o indice do primeiro " ", que é 3
palavras.push_back(s.substr(0, 3 - 0)); // "Seu"
```

\pause

```cpp
s.find(" ", 3 + 1); // a partir do indice 4 ("J"), encontra o indice do primeiro " ", que é 9
palavras.push_back(s.substr(4, 9 - 4)); // "Jorge"
```

\pause

```cpp
s.find(" ", 9 + 1); // a partir do indice 10 ("c"), encontra o indice do primeiro " ", que é 16
palavras.push_back(s.substr(10, 16 - 10)); // "cantou"
```

\pause

```cpp
s.find(" ", 16 + 1); // a partir do indice 17 ("a"), encontra o indice do primeiro " ", que é 18
palavras.push_back(s.substr(17, 18 - 17)); // "a"
```

\pause

```cpp
s.find(" ", 18 + 1); // a partir do indice 18 ("m"), não tem mais " ", produz -1.
palavras.push_back(s.substr(17, 26 - 19)); // "musica." 26 é o tamanho de s
```


# Implementação

Quais informações (variáveis) são necessárias a cada iteração? \pause O índice de início (`inicio`{.cpp}) e o valor produzido pela busca do espaço (`fim`{.cpp}). \pause

Como as variáveis são inicializadas? \pause `inicio = 0`{.cpp}. \pause

O que precisa ser feito a cada iteração? \pause Calcular `fim`, extrair e adicionar a substring em `palavras`. \pause O que mais? \pause Atualizar o `inicio` para a próxima iteração! \pause

Todas as iterações são iguais? \pause Não, a última interação é diferente. \pause Como identificar se estamos na última iteração? \pause `find` produz `-1`{.cpp}. \pause

Como o `inicio` é atualizado? \pause No caso geral, `inicio = fim + 1`{.cpp}. \pause E no último caso? \pause `inicio = s.length()`{.cpp}. \pause

Qual a condição para o laço continuar a execução? \pause `inicio < s.length()`{.cpp}


# Implementação

\scriptsize

```cpp
// Separa uma string usando um espaço como delimitador.
vector<string> separa(string s)
{
    vector<string> palavras = {};
    int inicio = 0;
    int fim;
    while (inicio < s.length()) {
        fim = s.find(" ", inicio);
        if (fim != -1) {
            palavras.push_back(s.substr(inicio, fim - inicio));
            inicio = fim + 1;
        } else {
            palavras.push_back(s.substr(inicio, s.length() - inicio));
            inicio = s.length();
        }
    }
    return palavras;
}
```

\pause

Podemos melhorar? \pause Sim! \pause `fim` é usado apenas dentro do laço, então podemo mover a declaração.


# Exercício

Um número inteiro positivo $n$ é primo se ele tem exatamente dois divisores distintos, $1$ e $n$. Projete uma função que verifique se um número inteiro positivo é primo. Dica: Faça exemplos de código (sem repetição lógica) para verificar se alguns números específicos (5, 8, 11) são primos e tente generalizar o código com repetição lógica usando o "enquanto". Leia com cuidado a definição e faça o código mais simples e direto possível!


# Especificação

\scriptsize

```cpp
// Produz true se n é um número primo, isto é, se n tem exatamente dois
// divisores distintos, 1 e ele mesmo. Produz false se n não é primo.
//
// Requer que n seja maior que 0.
bool primo(int n)
{
    return false;
}

examples
{
    check_expect(primo(1), false);
    check_expect(primo(2), true);
    check_expect(primo(3), true);
    check_expect(primo(4), false);
    check_expect(primo(5), true);
    check_expect(primo(8), false);
    check_expect(primo(11), true);
}
```


# Implementação

Como fazer a implementação? \pause Generalizando soluções específicas!


# Implementação

\scriptsize

```cpp
int n = 5;
int num_divisores = 0;

if (n % 1 == 0) {
    num_divisores = num_divisores + 1;
}
if (n % 2 == 0) {
    num_divisores = num_divisores + 1;

}
if (n % 3 == 0) {
    num_divisores = num_divisores + 1;
}
if (n % 4 == 0) {
    num_divisores = num_divisores + 1;
}
if (n % 5 == 0) {
    num_divisores = num_divisores + 1;
}
return num_divisores == 2; // 2 == 2 -> true
```


# Implementação

\scriptsize

```cpp
bool primo(int n)
{
    int num_divisores = 0;
    int i = 1;
    while (i <= n) {
        if (n % i == 0) {
            num_divisores = num_divisores + 1;
        }
        i += 1;
    }
    return num_divisores == 2;
}
```

\pause

\normalsize

Podemos melhorar! \pause Sim! \pause Veja o vídeo da aula para a discussão.


# Implementação

\scriptsize

```cpp
bool primo(int n)
{
    bool primo = n > 1;
    for (int i = 2; i <= n / 2 && primo; i = i + 1) {
        if (n % i == 0) {
            primo = false;
        }
    }
    return primo;
}
```