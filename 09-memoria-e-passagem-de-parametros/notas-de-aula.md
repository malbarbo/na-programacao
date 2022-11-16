---
# vim: set spell spelllang=pt_br:
# TODO: modificação no for each
title: Memória e passagem de parâmetros
---

# Introdução

Até o momento, quais eram as nossas preocupações no projeto de programas? \pause

- Identificar o problema \pause
- Resolver o problema \pause
- Escrever bom código \pause

Agora vamos discutir outro aspecto importante no projeto de programas: \pause o uso de recursos, especificamente o uso de memória.


# Memória

A memória é um recurso compartilhado entre os diversos programas que estão em execução em um computador. \pause O sistema operacional faz a gerência de memória entre os diversos processos e garante que cada processo só tenha acesso a memória destinada a ele. \pause

Cada processo também precisa gerenciar a sua própria memória. \pause

Algumas linguagens como Python, Java e Go, fazem a gerência automática da memória. \pause A parte do C++ que vimos até agora também faz a gerência automática da memória. \pause Algumas outras linguagens, como C, requerem que o programador faça a gerência da memória de forma manual (explícita).


# Memória

Cada forma de fazer a gerência de memória tem diversas vantagens e desvantagem, mas o ponto principal é a facilidade de programação vs o controle. \pause Vocês vão aprender mais sobre isso ao longo do curso! \pause

A gerência de memória requer basicamente duas operações: a alocação e a desalocação de memória. \pause

O que significa alocar memória? \pause É reservar um espaço de memória para ser usada de uma determinada forma. \pause

O que significa desalocar memória? \pause É devolver para o sistema um espaço de memória que havia sido alocada previamente para que ela possa ser usada de outra forma.


# Desafio

Considere um caderno com 100 linhas, onde as linhas estão enumeradas em sequência de 0 a 99, e cada linha representa uma célula de memória. \pause Simule no caderno como a memória é usada durante a execução do seguinte programa \pause

\scriptsize

```cpp
int i = 10;
vector<int> v = {1, 2, 3};
if (i > 4) {
    int j = i + 1;
    v.push_back(j);
}
vector<int> w = {10};
for (int t : v) {
    w.push_back(t);
}
```

\pause

\normalsize

Que conclusão podemos tirar dessa atividade? \pause A gerência de memória **pode** ser complicada!


# Gerência de memória em C++

Para facilitar a gerência de memória o compilador do C++ (os compiladores em geral), costumam dividir a memória em duas regiões: a pilha e o heap. \pause

A pilha é geralmente utilizada para alocar as variáveis de tamanho fixo e o heap é usado para alocar as variáveis de tamanho dinâmico. \pause

A pilha é gerenciada com uma estratégia simples: \pause

- A memória é sempre alocada após a última memória alocada ainda em uso \pause
- A memória é desalocada sempre na ordem inversa da alocação \pause

O heap é gerenciado com estratégias mais elaboradas e permite a desalocação em qualquer ordem.


# Gerência de memória em C++

No modelo de execução linha a linha, quando uma linha que contém uma declaração de variável é executada, o C++ reserva automaticamente uma memória para aquela variável. \pause

Quando uma variável sai do escopo, o C++ desaloca automaticamente a memória daquela variável.

\scriptsize


# Gerência de memória em C++

E as atribuições de variáveis? \pause

Quando as variáveis tem tamanho fixo, o valor que está sendo atribuído é armazenado diretamente na memória da variável. \pause

Quando as variáveis tem tamanho dinâmico, a memória alocada para a variável de destino é desalocada e uma nova memória de tamanho adequado é alocada, então o valor que está sendo atribuído é armazenado nessa nova memória.

# Gerência de memória em C++

\scriptsize

```cpp
int a = 10;
int x = 123;
// Armazena 20 e depos 123 na memória previamente alocada para a
a = 20;
a = x;
vector<int> v = {1, 6, 10};
vector<int> w = {10, 1, 7, 5};
// Explicação simplificada
// - Desaloca a memória de v
// - Aloca uma outra porção de memória suficiente para armazenar os valores de w
// - Copia os valores de w para a nova memória de v
v = w;
// Mesma coisa que antes, mas o vetor que está sendo copiado é criado implicitamente
v = {1, 3, 1};
```


# Gerência de memória em C++

E a passagem de parâmetros? \pause

Por padrão, o C++ usa a mesma estratégia de atribuição de variáveis, a cópia dos valores. \pause

Em algumas situações essa estratégia pode ser inconveniente.


# Palíndromo

\scriptsize

```cpp
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

\pause
\normalsize

O que acontece na chamada a seguir? \pause

\scriptsize

```cpp
vector<int> v = {};
for (int i = 0; i < 1000000; i = i + 1) {
    v.push_back(123);
}
palindromo(v);
```


# Palíndromo

Uma memória para 1000000 de elementos é alocada para `valores` e `v` é copiado para essa memória. A após a execução de palíndromo a memória de `valores` é desalocada. \pause

Parece um desperdício! \pause E é! \pause Podemo melhorar? \pause Sim! \pause

Ao invés de copiar os valores de `v` para `valores` podemos instruir o C++ a compartilhar esses valores. \pause Fazemos isso especificando que `valores` é uma referência constante com `const &`{.cpp}.


# Palíndromo

\scriptsize

```cpp
bool palindromo(const vector<int> &valores)
{
    bool palindromo = true;
    for (int i = 0, j = valores.size() - 1; i < j && palindromo; i = i + 1, j = j - 1) {
        if (valores[i] != valores[j]) {
            palindromo = false;
        }
    }
    return palindromo;
}

palindromo(v);
```

\pause

\normalsize

Quando `palindromo` é chamado, o valor de `v` é compartilhado com `valores`, isto é, tanto a variável `v` quanto a variável `valores` referenciam a mesma memória (são **apelidos** para a mesma memória). \pause Como a referência é `const`{.cpp}, então não é possível alterar `valores` (ex: `valores.push_back(1)`{.cpp} gera um erro de compilação).


# Referências constantes

Quando devemos usar referências constantes? \pause

Quando vamos apenas ler os valores de uma variável e queremos evitar que o seu conteúdo seja copiado. \pause

Note que evitar que o conteúdo seja copiado é uma preocupação apenas para variáveis que ocupam muita memória (arranjos, conjuntos e strings com muitos elementos).


# Referências

Existem referências que não são constantes? \pause Sim! \pause

Uma variável que é uma referência constante não pode ser modificada, já uma variável que é apenas uma referência, pode ser modificada. \pause

Como uma referência é um apelido para a memória de outra variável, então quando uma memória é modificada através de uma referência, de fato, a memória da outra variável é que é modificada.


# Referências

\scriptsize

```cpp
void soma_1_no_primeiro(vector<int> &v)
{
    v[0] = v[0] + 1;
}

examples
{
    vector<int> x = {5, 1, 8};
    soma_1_no_primeiro(x);
    check_expect(x, (vector<int> {6, 1, 8}));
}
```

\pause

\normalsize

O que está acontecendo aqui? \pause

Quando `soma_1_no_primeiro` é chamada, `v` passa a referenciar a mesma memória de `x`, então, quando `v` é alterado, de fato é `x` que está sendo alterado.


# Referências

\scriptsize

```cpp
void soma_1_no_primeiro(vector<int> &v)
{
    v[0] = v[0] + 1;
}

examples
{
    vector<int> x = {5, 1, 8};
    soma_1_no_primeiro(x);
    check_expect(x, (vector<int> {6, 1, 8}));
}
```

\normalsize

Lendo o código do exemplo com cuidado, podemos entender a intenção do código, sem se preocupar com como ele funciona. \pause Cria um arranjo `x` com os elementos `{5, 1, 8}`{.cpp}, \pause soma 1 no primeiro elemento de `x`, \pause verifica que a soma foi feita corretamente.


# Referências

\scriptsize

```cpp
void soma_1_no_primeiro(vector<int> &v)
{
    v[0] = v[0] + 1;
}

examples
{
    vector<int> x = {5, 1, 8};
    soma_1_no_primeiro(x);
    check_expect(x, (vector<int> {6, 1, 8}));
}
```

\normalsize

Note que a função `soma_1_no_primeiro` não tem retorno. \pause

Como uma função sem retorno produz algo de útil? \pause Através de **efeitos colaterais**, no caso de `soma_1_no_primeiro`, o efeito colateral é alterar o valor do parâmetro `v`. \pause

Como a função não tem retorno, temos que testá-la em três etapas, inicializar as variáveis, chamar a função e verificar se as variáveis foram alteradas corretamente.


# Referências

Quando usar referências? \pause

Quando queremos alterar variáveis e não precisamos manter os seus valores antigos. \pause

Quando não usar referências? \pause

Quando precisamos dos valores atuais e dos novos valores das variáveis.


# Projeto de funções

Como projetar funções que modificam os seu argumentos? \pause

Generalizando exemplos concretos.


# Exemplo

Dado um arranjo ordenado em ordem não decrescente e um valor `v`, projete uma função que modifique o arranjo inserindo o valor `v` de maneira que o arranjo continue em ordem.


# Especificação

\scriptsize

```cpp
// Insere v em valores de maneira que valores continue em ordem.
// Requer que valores esteja ordenado em ordem não decrescente.
void insere_ordenado(vector<int> &valores, int v) { }

examples {
    vector<int> valores = {};
    insere_ordenado(valores, 10);
    check_expect(valores, (vector<int> {10}));

    insere_ordenado(valores, 1);
    check_expect(valores, (vector<int> {1, 10}));

    insere_ordenado(valores, 2);
    check_expect(valores, (vector<int> {1, 2, 10}));

    insere_ordenado(valores, 12);
    check_expect(valores, (vector<int> {1, 2, 10, 12}));

    insere_ordenado(valores, 10);
    check_expect(valores, (vector<int> {1, 2, 10, 10, 12})); }
```


# Exemplo

<div class="columns">
<div class="column" width="48%">
\scriptsize

```cpp
vector<int> valores = {1, 2, 10, 12};
int v = 9;

valores.push_back(v);
// valores = {1, 2, 10, 12, 9}
```

\pause

```cpp
int t = valores[4];
valores[4] = valores[3];
valores[3] = t;
// valores = {1, 2, 10, 9, 12}
```

\pause

```cpp
int t = valores[3];
valores[3] = valores[2];
valores[2] = t;
// valores = {1, 2, 9, 10, 12}
```
</div>
<div class="column" width="48%">
\pause
Quais variáveis vamos precisar para o laço? \pause O índice `i`{.cpp} do elemento que está fora de ordem. \pause

Como as variáveis são inicializadas? \pause `i = valores.size() - 1`{.cpp}. \pause

Qual a condição para o laço continuar a execução? \pause `i > 0`{.cpp} e `valores[i - 1] > valores[i]`{.cpp}. \pause

O que é feito a cada iteração? O elemento na posição `i`{.cpp} é trocado de lugar com o elemento na posição `i - 1`{.cpp} e `i`{.cpp} é decrementado.
</div>
</div>


# Implementação

\scriptsize

```cpp
void insere_ordenado(vector<int> &valores, int v) {
    valores.push_back(v);
    int i = valores.size() - 1;
    while (i > 0 && valores[i - 1] > valores[i]) {
        int t = valores[i];
        valores[i] = valores[i - 1];
        valores[i - 1] = t;
        i = i - 1;
    }
}
```

\pause

Podemos melhorar? \pause

```cpp
void insere_ordenado(vector<int> &valores, int v) {
    valores.push_back(v);
    for (int i = valores.size() - 1; i > 0 && valores[i - 1] > valores[i]; i = i - 1) {
        int t = valores[i];
        valores[i] = valores[i - 1];
        valores[i - 1] = t;
    }
}
```
