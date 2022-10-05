---
title: Resumo
---

# Compilação

Criar executável `ola` a partir do arquivo `ola.cpp`

```
g++ -o ola ola.cpp
```

# Linguagem

## Notação

`[]`: opcional.

`...`: o padrão se repete.

## Declaração de variáveis

_Forma geral_

```cpp
Tipo nome_variavel [= expressão valor inicial];
```

_Forma de execução_

O computador aloca uma célula de memória e associa o nome `nome_varial` com a célula. Se "expressão valor inicial" existir, a expressão é avaliada e  o valor resultante é armazenado na célula `nome_varial`. Note que se um valor inicial não for fornecido, o valor armazenado na na célula de memória é indefinido.

_Exemplos_

```cpp
int a = 10;
// aloca uma célula de memória e associa com o nome b e armazena o valor 22 nessa célula
int b = a * a + 2;
double x;
```

Note que as instruções são executadas sequencialmente, uma após a outra.

## Funções

_Forma geral_

```cpp
TipoSaida nome_da_funcao(TipoEntrada1 e1, ...)
{
    [instruções; ...]
    return expressão resultado;
}
```

_Forma de execução_

Na chamada de uma função o fluxo de execução é desviado para a primeira instrução dentro da função e volta para o local do desvio quando a instrução `return` é executada.

_Exemplos_

```{.cpp .number-lines}
// inverte_unidade_dezena(4367) -> 4376
bool inverte_unidade_dezena(int num)
{
    int u = num % 10;
    int d = (num / 10) % 10;
    int restante = num / 100;
    return restante * 100 + u * 10 + d;
}

int main() {
    int x = inverte_unidade_dezena(4367); // 4376
    cout << x << endl;
}
```

Nesse exemplo as linhas são executadas na ordem 11, 4, 5, 6, 7, 11, 12.

## Instrução `if/else`{.cpp}

_Forma geral_

```cpp
if (condição) {
    instruções então;
} [else {
    instruções senão;
}]
```

_Forma de execução_

O computador avalia a "condição" e verifica o resultado. Se o resultado for `true`{.cpp}, então as instruções do bloco "instruções então" são executadas, senão (o resultado é `false`{.cpp}), as instruções do bloco "instruções senão" são executadas.

__Exemplos__

```{.cpp .number-lines}
int main() {
    int a = 10;
    int b = 20;
    int m;
    if (a > b) {
        m = a;
    } else {
        m = b;
    }
    cout << m << endl;
}
```

O valor exibido por esse programa é 20 e as linhas são executadas na ordem 2, 3, 4, 5, 8, 10.

## Tipo enumerado

_Forma geral_

```cpp
enum Nome {
    Enum1,
    Enum2,
    ...
};
```

_Quando utilizar?_

Quando todos os valores válidos para o tipo podem ser nomeados.

_Exemplos_

A cor de um semáforo só pode assumir 3 valores: vermelho, amarelo ou verde, então criamos um tipo enumerado.

```
enum Cor {
  Vermelho,
  Amarelo,
  Verde
};
```


## Instrução `switch/case`{.cpp}

```cpp
switch (expressão) {
    case caso:
        instruções;
        break;
    [case caso:
        instruções;
        break;
     ...
    ]
    [default:
        instruções;
        break;]
}
```


# Tipos primitivos e pré-definidos

## Números

`int`{.cpp}: números inteiros no intervalo $-2^{32}$ a $2^{32} - 1$.

`double`{.cpp}: aproximação de número decimais com até 15 casas decimais.

Operações que misturam `double`{.cpp} e `int`{.cpp} produzem `double`{.cpp} como resposta.

```cpp
// Operações com int
23 + 12; // 35
23 - 12; // 11
3 * 6 ; // 18
// Divisão inteira
15 / 5; // 3
15 / 7; // 2
// Módulo
15 % 5; // 0
15 % 7; // 1
18 % 7; // 3
```

```cpp
// Operações com double
1.2 + 2.5; // 3.7
4.2 - 8.0; // -3.8
4.1 * 2.0; // 8.2
4.75 / 0.5; // 9.5
```

Função da biblioteca `cmath`.

```cpp
// Produz o maior inteiro menor ou igual a (piso).
double floor(double n);
floor(1.0); // 1.0
floor(1.3); // 1.0
floor(1.5); // 1.0
floor(1.7); // 1.0
```

```cpp
Produz o menor inteiro menor ou igual a n (teto).
double ceil(double n);
ceil(1.3); // 2.0
ceil(1.5); // 2.0
ceil(1.7); // 2.0
ceil(2.0); // 2.0
```

```cpp
// Produz o inteiro mais próximo de n (arredondamento).
double round(double n);
round(1.3); // 1.0
round(1.5); // 2.0
round(1.7); // 2.0
```

```cpp
// Calcula o seno de x (dado em radianos).
double sin(double x);
sin(3.14); // 0.00159265
```

```cpp
// Calcula a raiz quadrada de x.
double sqrt(double x);
sqrt(2.0); // 1.41421
```

```cpp
// Calcular x elevado a potência y.
double pow(double x, double y);
pow(2.0, 4.0); // 16
```

## Booleano

```cpp
// Negação
// Produz true se x é false e produz false se x é true.
bool operator!(bool x);
!(4 == 2 + 2); // false
!false; // true
```

```cpp
// Conjunção (e)
// Produz true se a e b são true, false caso contrário.
bool operator&&(bool a, bool b);
// par e maior que 12
int n = 14;
n % 2 == 0 && n > 12; // false

// Disjunção (ou)
// Produz true se a ou b é true, false caso contrário.
bool operator||(bool a, bool b);
// menor de idade ou idoso
int idade = 72;
idade < 18 || idade >= 60; // true
```

## String

Necessário incluir a biblioteca `string`.

```cpp
// Concatenação
// Produz uma nova string juntado a string b no final da string a.
string operator+(string a, string b);

string s = "Jorge";
"Ola " + s + "!"; // "Ola Jorge!"
```

```cpp
// Substring
// Produz uma substring de this que começa na posição start e termina na
// posição start + len - 1. Requer que 0 <= start < this.length().
string string::substr(int start, int len);

string s = "jorge";
s.substr(1, 3); // "org"
```

```cpp
// Número de bytes
// Produz o número de bytes de this.
int string::length();

string s = "jorge";
s.length(); // 5
```


# Projeto de programas

Para projetar um programa seguimos os passos:

1. Análise
2. Definição dos tipos de dados
3. Especificação
4. Implementação
5. Verificação
6. Revisão

## Análise

Determinar o problema que deve ser resolvido e as informações relevantes.

## Definição dos tipos de dados

Identificar as informações e determinar como elas serão representadas.

## Especificação

Escrever com mais precisão e com exemplos o que a função faz. Inclui

- Assinatura (nome da função, entradas e saída)
- Propósito
- Exemplos

## Implementação

Escrever o corpo da função para que ela faça o que está na especificação.

## Verificação

Compilar e executar o programa para verificar se a implementação está de acordo com a especificação.

## Revisão

Alterar a organização do programa para que fique mais fácil de ser lido, entendido e alterado.

## Exemplos

_Problema_

O André viaja muito. Sempre antes de fazer uma viagem ele calcula o quanto ele irá gastar com             combustível. Ele determina a distância que ele irá percorrer na viagem, o preço do litro do combustível e consulta as suas anotações para ver o consumo do carro, isto é, a quantidade de quilômetros que o carro   anda com um litro de combustível e então faz o cálculo do custo. O André acha um pouco chato fazer os     cálculos na mão, então ele pediu para você escrever um programa que faça os cálculos para ele.

_Projeto_

```cpp
#include "bscpp.hpp"

// Análise
// - Calcular o custo em reais para percorrer uma determinada distância levando
//   em consideração o desempenho   do carro e o preço do litro do combustível.
//
// Definição de tipos de dados
//
// - A distância em Km, rendimento em Km/l, preço em R$/l e o custo da viagem
//   em R$ serão representados por número positivos (double).

// Calcula o custo em reais para percorrer a distancia especificada
// considerando o rendimento do carro e o preco do litro do combustível.
double custo_viagem(double distancia, double rendimento, double preco) {
    return (distancia / rendimento) * preco;
}

examples {
    check_expect(custo_viagem(120.0, 10.0, 5.0), 60.0); // (120.0 / 10.0) * 5.0
    check_expect(custo_viagem(300.0, 15.0, 6.0), 120.0); // (300.0 / 15.0) * 6.0
}

int main() {
    run_tests();
}
```
