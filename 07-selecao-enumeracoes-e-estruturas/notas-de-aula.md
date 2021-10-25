---
# vim: set spell spelllang=pt_br:
title: Seleção, enumerações e estruturas
---

# Introdução

Antes de estudarmos instruções de seleção, vamos analisar como um computador "executa" um programa.


# Sequenciação

```{.cpp .number-lines}
int n = 10;
int a = n + 2;
cout << a;
```

\pause

Qual o valor exibido pelo programa? \pause 12. \pause

Nesse exemplo, o computador executa uma linha após a outra, por isso chamamos essa "estrutura" de código de sequencial (sequenciação). \pause

Qual é a ordem que as linhas serão executadas? \pause 1, 2, 3.


# Mudança de variável

<div class="columns">
<div class="column" width="48%">

```{.cpp .number-lines}
int n;
int a = 10;
n = a;
cout << n;
```

Qual o valor exibido pelo programa? \pause 10. \pause

```{.cpp .number-lines}
int n = 5;
int a = 10;
n = a;
cout << n;
```

\pause

Qual o valor exibido pelo programa? \pause 10. \pause
</div>
<div class="column" width="48%">
No primeiro caso, a variável `n` é declarada mas não é inicializada na linha 1. Quando a linha 3 é executada, o `n` é inicializado com o valor que está armazenado em `a`, que é 10. Na linha 4 o valor de `n` é exibido. \pause

Já no segundo caso, a variável `n` é declarada e inicializada na linha 1 com o valor 5. Na linha 3 o valor de `a` é copiado para `n` (célula de memória com o nome `n`), substituindo o valor 5 por 10. Na linha 4 o valor de `n` é exibido.
</div>
</div>


# Mudança de variável

```{.cpp .number-lines}
int n = 1;
int a = n + 1;
n = a + 3;
cout << n;
```

Qual o valor exibido pelo programa? \pause 5. \pause

Para entender esse resultado devemos executar o programa como um computador! \pause

- Na linha 1 alocamos uma célula de memória e nomeamos ela de `n` e armazenamos o valor 1 nessa célula; \pause
- Na linha 2 alocamos uma célula de memória e nomeamos ela de `a`. Lemos o valor de `n`, somamos 1 e armazenamos o resultado (2) em `a`; \pause
- Na linha 3 lemos o valor de `a` e somamos com 3, depois armazenamos o resultado (5) em `n`; \pause
- Na linha 4 lemos e exibimos o valor de `n`.


# Mudança de variável

```{.cpp .number-lines}
int n = 1;
n = n + 2;
n = n + 5;
cout << n;
```

Qual o valor exibido pelo programa? \pause 8. \pause

Executando com um computador: \pause

- Na linha 1 alocamos uma célula de memória e nomeamos ela de `n` e armazenamos o valor 1 nessa célula; \pause
- Na linha 2 lemos o valor de `n` e somamos com 2, depois armazenamos o resultado (3) em `n`; \pause
- Na linha 3 lemos o valor de `n` e somamos com 5, depois armazenamos o resultado (8) em `n`; \pause
- Na linha 4 lemos e exibimos o valor de `n`.


# Pergunta

Em todos os programas que escrevemos até agora as linhas são sempre executadas na sequência? \pause Não! \pause

Quando chamamos uma função, o fluxo de execução é desviado para o início do corpo da função. Quando uma função executa uma instrução `return`{.cpp}, o fluxo de execução volta para onde ele estava antes da chamada da função.


# Execução de funções

<div class="columns">
<div class="column" width="48%">

```{.cpp .number-lines}
int dobro_mais_um(int n) {
    int a = 2 * n;
    return a + 1;
}

int main() {
   int b = 5;
   int c = dobro_mais_um(b + 4) + 1;
   cout << c;
}
```
</div>
<div class="column" width="48%">
\pause
Qual o valor exibido pelo programa? \pause 20. \pause

Qual é a ordem que as linhas são executadas? (veja o vídeo da aula para entender como o programa é executado) \pause

- 7 \pause
- 8 (`b + 4`) \pause
- 2 \pause
- 3 \pause
- 8 (soma do resultado da função (19) com 1 e atribuição do valor a `c`) \pause
- 9
</div>
</div>


# Escopo, nomes e chamadas de funções

<div class="columns">
<div class="column" width="48%">

```{.cpp .number-lines}
int soma_1(int n) {
    int a = n + 1;
    return a;
}

int main() {
   int n = 2;
   int a = 3;
   n = soma_1(a);
   cout << n << " " << a;
}
```
</div>
<div class="column" width="48%">
\pause
Qual o valor exibido pelo programa? \pause

Não tente "executar" a chamada da função, pense apenas no seu propósito, sem olhar para o seu corpo. \pause

Então, qual o valor exibido pelo programa? \pause 4 e 3.
</div>
</div>


# Seleção

Além das chamadas de funções, temos outras instruções que alteram o fluxo de execução do programa. \pause

Uma dessas instruções é o `if else`{.cpp} (se e senão em inglês).


# Seleção

O `if else`{.cpp} é uma instrução de seleção e sua forma geral é: \pause

```cpp
if (condição) {
    intruções então;
} else {
    intruções senão;
}
```

\pause

Como a instrução `if else`{.cpp} é executada? \pause O computador avaliação a condição e verifica o resultado. Se o resultado for `true`{.cpp}, então as instruções do bloco "instruções então" são executadas, senão (o resultado é `false`{.cpp}), as instruções do bloco "instruções senão" são executadas.


# Exemplo

<div class="columns">
<div class="column" width="48%">

```{.cpp .number-lines}
int a = 10;
int b = 20;
int m;
if (a > b) {
    m = a;
} else {
    m = b;
}
cout << m;
```

\pause

Qual o valor exibido pelo programa? \pause 20. \pause

Em que ordem as linhas são executas para gerar esse resultado? \pause 1, 2, 3, 4, 7, 9. \pause
</div>
<div class="column" width="48%">

```{.cpp .number-lines}
int a = 15;
int b = 8;
int m;
if (a > b) {
    m = a;
} else {
    m = b;
}
cout << m;
```

\pause

Qual o valor exibido pelo programa? \pause 15. \pause

Em que ordem as linhas são executas para gerar esse resultado? \pause 1, 2, 3, 4, 5, 9.
</div>
</div>


# Valor máximo

Vamos voltar ao exemplo do valor máximo. \pause

Projete uma função que encontre o maior valor entre dois números dados.

# Especificação e implementação

<div class="columns">
<div class="column" width="48%">
\small
Especificação \pause

```cpp
// Encontra o valor máximo entre a e b.
int maximo(int a, int b)
{
    return 0;
}

examples
{
    check_expect(maximo(20, 10), 20);
    check_expect(maximo(5, 10), 10);
    check_expect(maximo(5, 5), 5);
}
```

\pause
</div>
<div class="column" width="48%">

Implementação \pause

A resposta da função `maximo` dependente de alguma condição? \pause Sim. \pause

Se o valor de `a` for maior do que o valor de `b`, então a resposta é o valor de `a`, senão a resposta é o valor de `b`. \pause

Quando a resposta depende de uma condição, usamos uma sentença de seleção!
</div>
</div>


# Implementação

<div class="columns">
<div class="column" width="48%">
\small

```{.cpp .number-lines}
int maximo(int a, int b) {
    int m;
    if (a > b) {
        m = a;
    } else {
        m = b;
    }
    return m;
}

int main() {
    int a = maximo(10, 8);
    int b = maximo(14, 20);
    cout << a << " " << b;
}
```
</div>
<div class="column" width="48%">
\pause
Qual é a saída exibido pelo programa? \pause 10 e 20. \pause

Em que ordem as linhas são executas para gerar esse resultado? \pause

12, \pause 2, \pause 3, \pause 4, \pause 8, \pause 12, \pause

13, \pause 2, \pause 3, \pause 6, \pause 8, \pause 13, \pause

14
</div>
</div>


# Máximo 3

Projete uma função que encontre o valor máximo entre três números.


# Análise e definição de tipos de dados

Análise \pause

- Encontrar o valor máximo entre três número dados \pause

Tipos de dados \pause

- Os valores serão números inteiros


# Especificação

<div class="columns">
<div class="column" width="48%">
Especificação \pause

\scriptsize
```cpp
// Encontra o valor máximo entre a, b e c.
int maximo3(int a, int b, int c) {
   return 0;
}
examples {
    // a é máximo
    check_expect(maximo3(20, 10, 12), 20);
    check_expect(maximo3(20, 12, 10), 20);
    check_expect(maximo3(20, 12, 12), 20);
    // b é máximo
    check_expect(maximo3(5, 12, 3), 12);
    check_expect(maximo3(3, 12, 5), 12);
    check_expect(maximo3(5, 12, 5), 12);
    // c é máximo
    check_expect(maximo3(4, 8, 18), 18);
    check_expect(maximo3(8, 4, 18), 18);
    check_expect(maximo3(8, 8, 18), 18);
}
```

\pause
</div>
<div class="column" width="48%">
Implementação \pause

\scriptsize
Encontrar o máximo entre a e b e depois o máximo entre o resultado e c. \pause

```cpp
int maximo3(int a, int b, int c) {
    int max;
    if (a >= b) {
        if (a >= c) {
            max = a;
        } else {
            max = c;
        }
    } else {
        if (b >= c) {
            max = b;
        } else {
            max = c;
        }
    }
    return max; }
```
</div>
</div>


# Verificação e revisão

Verificação: \pause ok. \pause

Revisão: \pause muitas possibilidades!


# Revisão

<div class="columns">
<div class="column" width="48%">

\scriptsize

```{.cpp .number-lines}
int maximo3(int a, int b, int c) {
    int max;
    if (a >= b) {
        if (a >= c) {
            max = a;
        } else {
            max = c;
        }
    } else {
        if (b >= c) {
            max = b;
        } else {
            max = c;
        }
    }
    return max;
}
```
</div>
<div class="column" width="48%">
\pause
Qual o propósito do bloco das linhas 4 a 8? \pause Encontrar o máximo entre `a` e `c`. \pause

Qual o propósito do bloco das linhas 10 a 14? \pause Encontrar o máximo entre `b` e `c`. \pause

Já temos uma função para encontrar o máximo entre dois números? \pause Sim! \pause A função `maximo` que fizemos anteriormente.
</div>
</div>


# Revisão

<div class="columns">
<div class="column" width="48%">

\small

```{.cpp .number-lines}
int maximo3(int a, int b, int c) {
    int max;
    if (a >= b) {
        max = maximo(a, c);
    } else {
        max = maximo(b, c);
    }
    return max;
}
```
</div>
<div class="column" width="48%">
\pause
Qual o propósito da estrutura de seleção da linha 3? \pause Encontrar o máximo entre `a` e `b`... \pause Nós já temos uma função para fazer isso!
</div>
</div>


# Revisão

<div class="columns">
<div class="column" width="48%">

\small

```{.cpp .number-lines}
int maximo3(int a, int b, int c) {
    return maximo(maximo(a, b), c);
}
```
</div>
<div class="column" width="48%">
Estratégia de implementação

Encontrar o máximo entre a e b e depois o máximo entre o resultado e c.
</div>
</div>


# Álcool ou Gasolina?

<div class="columns">
<div class="column" width="48%">
Depois que você fez o programa para o André, a Márcia, amiga em comum de vocês, soube que você está oferecendo serviços desse tipo e também quer a sua ajuda. O problema da Márcia é que ela sempre tem que fazer a conta manualmente para saber se deve abastecer o carro com álcool ou gasolina. A conta que ela faz é verificar se o preço do álcool é até 70% do preço da gasolina, se sim, ela abastece o carro com álcool, senão ela abastece o carro com gasolina. Você pode ajudar a Márcia também?
\pause
</div>
<div class="column" width="48%">
Análise \pause

- Determinar o combustível que será utilizado. Se o preço do álcool for até 70% do preço da gasolina, então deve-se usar o álcool, senão a gasolina.

\pause

Definição de tipos de dados \pause

- O preço do litro do combustível será representado por um número positivo com três casas decimais; \pause

- O tipo de combustível será representado por uma string.
</div>
</div>


# Especificação

Veja no vídeo da aula como chegamos nesse resultado.


# Especificação

\footnotesize

```{.cpp}
// Combustivel é "alcool" ou "gasolina".
```

\pause

```{.cpp}
// Indica o combustível que deve ser utilizado no abastecimento. Produz
// "alcool" se preco-alcool for menor ou igual a 70% do preco-gasolina, produz
// "gasolina" caso contrário.
string indica_combustivel(double preco_alcool, double preco_gasolina) {
    return "alcool";
}
```
\pause

```cpp
examples {
    // 4.000 <= 0.7 * 5.000 -> false -> "gasolina"
    check_expect(indica_combustivel(4.000, 5.000), "gasolina");
    // 4.000 <= 0.7 * 6.000 -> true -> "alcool"
    check_expect(indica_combustivel(4.000, 6.000), "alcool");
    // 3.500 <= 0.7 * 5.000 -> true -> "alcool"
    checK_expect(indica_combustivel(4.200, 6.000), "alcool");
}
```


# Implementação

O resultado depende de uma condição? \pause Sim! \pause Então usamos seleção \pause

\small

```cpp
// Indica o combustível que deve ser utilizado no abastecimento. Produz
// "alcool" se preco-alcool for menor ou igual a 70% do preco-gasolina, produz
// "gasolina" caso contrário.
string indica_combustivel(double preco_alcool, double preco_gasolina) {
    string combustivel
    if (preco_alcool <= 0.7 * preco_gasolina) {
        combustivel = "alcool";
    } else {
        combustivel = "gasolina";
    }
    return combustivel;
}
```


# Verificação e revisão

Verificação: \pause ok. \pause

Revisão: \pause string não parece ser o tipo apropriado. \pause Pela assinatura da função, "qualquer" string pode ser dada como resposta, mas de fato apenas dois valores são possível: "alcool" e "gasolina". \pause Podemos melhorar? \pause Sim.


# Tipos enumerados

Em um tipo enumerado todos os valores válidos para o tipo são enumerados explicitamente. \pause

A forma geral para definir tipos enumerados é

```cpp
enum NomeDoTipo {
    Valor1,
    Valor2,
    ...,
};
```


# Tipos enumerados

```cpp
// O tipo do combustível utilizado no abastecimento.
enum Combustivel {
    Alcool,
    Gasolina,
};
```

\pause

\normalsize

Observações \pause

- Sempre vamos adicionar um comentário sobre o propósito do tipo; \pause
- É necessário finalizar a declaração com um ponto e vírgula;


# Tipos enumerados

Uma variável do tipo `Combustivel` só pode armazenar o valor `Alcool` ou `Gasolina`, se tentarmos atribuir um valor diferente, o compilador indicará um erro. \pause

\small

```cpp
Combustivel c = false;
```

\pause

Erro

```
x.cpp: In function ‘int main()’:
x.cpp:8:21: error: cannot convert ‘bool’ to ‘Combustivel’ in initialization
    8 |     Combustivel c = false;
      |                     ^~~~~
```


# Tipos enumerados

Quando usar tipos enumerados? \pause

Quando todos os valores válidos para o tipo podem ser nomeados. \pause

Porque utilizar tipos enumerados? \pause

Para expressar mais claramente o código e evitar a utilização de valores inválidos (como `"alcoo"`{.cpp} em uma variável string que representa o tipo do combustível).


# Revisão do exemplo

\footnotesize

```cpp
Combustivel indica_combustivel(double preco_alcool, double preco_gasolina)
{
    Combustivel combustivel;
    if (preco_alcool <= 0.7 * preco_gasolina) {
        combustivel = Alcool;
    } else {
        combustivel = Gasolina;
    }
    return combustivel;
}
examples
{
    check_expect(indica_combustivel(4.000, 5.000), Gasolina);
    check_expect(indica_combustivel(4.000, 6.000), Alcool);
    check_expect(indica_combustivel(3.500, 5.000), Alcool);
}
```


# Exemplo

Projete uma função que receba como entrada a cor atual de um semáforo de trânsito e devolva a próxima cor que será ativada (considere um semáforo com três cores: verde, amarelo e vermelho). \pause

Fizemos o projeto desse programa durante a aula obtivemos o seguinte resultado.


# Semáforo

<div class="columns">
<div class="column" width="48%">
\scriptsize

```cpp
// Representa a cor de um semáforo.
enum Cor {
    Verde,
    Vermelho,
    Amarelo,
};
// Produz a próximo cor de um semáforo
// que está com a cor c.
Cor proxima_cor(Cor c) {
    Cor proxima;
    if (c == Verde) {
        proxima = Amarelo;
    } else if (c == Vermelho) {
        proxima = Verde;
    } else { // c == Amarelo
        proxima = Vermelho;
    }
    return proxima;
}
```
</div>
<div class="column" width="48%">

\scriptsize

```cpp
examples
{
    check_expect(proxima_cor(Verde), Amarelo);
    check_expect(proxima_cor(Vermelho), Verde);
    check_expect(proxima_cor(Amarelo), Vermelho);
}
```

\pause

Verificação: \pause Ok. \pause

Revisão: \pause vamos usar uma construção nova, o `switch/case`{.cpp}.

</div>
</div>


# `switch/case`{.cpp}

<div class="columns">
<div class="column" width="48%">
A sintaxe simplificada do `switch/case`{.cpp} é

\scriptsize

```cpp
switch (expressão) {
    // zero ou mais casos
    case caso1:
        instruções;
        break;
    // ...
    case cason:
        instruções;
        break;
    // opcional
    default:
        instruções;
        break;
}
```

\small

Onde `expressão` precisa gerar um valor do tipo inteiro ou enumerado.
</div>
<div class="column" width="48%">
\small
\pause
A instrução `switch/case`{.cpp} funciona da seguinte forma: \pause

A `expressão` é avaliada e seu valor é comparado com cada caso na sequência. \pause

Quando um caso que tem o mesmo valor do resultado da expressão é encontrado, as `instruções` daquele caso são executadas até encontrar um `break`, quando então a instrução `switch/case`{.cpp} termina e o programa continua a execução com a próxima instrução após o `switch/case`{.cpp}. \pause

Se o valor da expressão não é igual a nenhum caso, então as instruções da cláusula `default`{.cpp} é executada.

</div>
</div>


# `switch/case`{.cpp}

Quando utilizar o `switch/case`{.cpp}? \pause

Quando precisamos analisar o valor de um tipo enumerado ou quando precisamos analisar um conjunto de valores inteiros específicos (ex 1,3, 4, 5). \pause

Qual é a vantagem de utilizar `switch/case`{.cpp} ao invés de uma sequência de `if`{.cpp}s? \pause

O código fica mais fácil de ler. \pause

O compilador (usando a opção `-Wall`) gera um aviso se esquecermos de algum valor na análise de valores enumerados.



# Semáforo

Escrevendo a função `proxima_cor` para utilizar o `switch/case`{.cpp} obtemos \pause

\footnotesize

```cpp
Cor proxima_cor(Cor c) {
    Cor proxima;
    switch (c) {
        case Verde:
            proxima = Amarelo;
            break;
        case Vermelho:
            proxima = Verde;
            break;
        case Amarelo:
            proxima = Vermelho;
            break;
    }
    return proxima;
}
```


# Exemplo

Em um determinado programa é necessário exibir para o usuário o tempo que uma operação demorou. Esse tempo está disponível em segundos, mas exibir essa informação em segundos para o usuário pode não ser interessante, afinal, ter uma noção razoável de tempo para 14678 segundos é difícil!

a) Projete uma função que converta uma quantidade de segundos para uma quantidade de horas, minutos e segundos equivalentes.

b) Projete uma função que que converta uma quantidade de horas, minutos e segundos em uma string amigável para o usuário. A string não deve conter informações sobre o tempo que são zeros (por exemplo, não deve informar 0 minutos).


# Exemplo

Análise

- Converter uma quantidade de segundos em horas, minutos e segundos. \pause

Definição de tipos de dados

- Os segundos da entrada serão representados com números inteiros positivos \pause

- A saída são três números inteiros positivos... \pause As funções em C++ só permitem um valor de saída, como proceder? \pause Vamos criar um novo tipo de dado que agrupa esses três valores.



# Tipos de dados

Vamos relembrar alguns tipos de dados que utilizamos até agora:

- Tipos atômicos pré-definidos (primitivos) na linguagem: `int, double, bool`{.cpp}
- Tipos atômicos definidos em bibliotecas: `string`{.cpp}
- Tipos atômicos enumerados definidos pelo usuário: `enum`{.cpp}

\pause

Esses tipos são chamados atômicos porque não são compostos de outros tipos. \pause

Podemos criar novos tipos de dados a partir de tipos existentes. \pause

Uma forma de fazer isso é através de tipos estruturas.


# Tipos estruturas

Um tipo estrutura é um tipo de dado composto por um conjunto fixo de campos com nome e tipo.

A forma geral para definir um tipo estrutura é

```cpp
struct NomeDoTipo {
    Tipo1 campo1;
    Tipo2 campo2;
    ...
};
```


# Tipos estruturas

Podemos definir um novo tipo para representar um tempo da seguinte forma

```cpp
// Representa o tempo de duração de um evento.
struct Tempo {
    int horas;
    int minutos;
    int segundos;
};
```

\pause

Observações

- Assim como para definição de tipos enumerados, sempre vamos adicionar um comentário sobre o propósito do tipo; \pause
- É necessário finalizar a declaração com um ponto e vírgula.


# Tipos estruturas

Para inicializar uma variável de um tipo estrutura, especificamos os valores dos campos (na ordem que eles foram declarados) entre chaves e separados por vírgula \pause

```cpp
Tempo t1 = {0, 20, 10};
Tempo t2 = {4, 0, 20};
```

\pause

Para exibir um valor de um tipo estrutura podemos utilizar a função `repr` da biblioteca `bscpp`

```cpp
cout << repr(t1) << endl; // Tempo {0, 20, 10}
```


# Tipos estruturas

Como valores do tipo `Tempo` são compostos de outros valores (partes), podemos acessar e alterar cada valor de forma separada

```cpp
Tempo t1 = {0, 20, 10};

cout << t1.horas << endl; // exibe 0

t1.minutos = 40; // muda a quantidade de minutos para 40
```

\pause

Agora podemos voltar para o nosso problema.


# Especificação e implementação

<div class="columns">
<div class="column" width="65%">
Especificação

\scriptsize

```cpp
// Converte a quantidade segundos para o tempo equivalente em
// horas, minutos e segundos. A quantidade de segundos e
// minutos da resposta é sempre menor que 60.
Tempo segundos_para_tempo(int segundos) {
    return Tempo {0, 0, 0};
}

examples {
    // 160 / 60 -> 2
    // 160 % 60 -> 40
    check_expect(segundos_para_tempo(160), (Tempo {0, 2, 40}));
    // 3760 / 3600 -> 1
    // 3760 % 3600 -> 160 segundos que sobraram
    // 160 / 60 -> 2
    // 160 % 60 -> 40
    check_expect(segundos_para_tempo(3760), (Tempo {1, 2, 40}));
}
```

\pause
</div>
<div class="column" width="33%">
Implementação

\scriptsize

```cpp
Tempo segundos_para_tempo(int segundos)
{
    int h = segundos / 3600;
    // segundos que não foram
    // convertidos para hora
    int restantes = segundos % 3600;
    int m = restantes / 60;
    int s = restantes % 60;
    return Tempo {h, m, s};
}
```

\pause

Verificação: ok \pause

Revisão: ok
</div>
</div>


# Estruturas

Quando utilizamos estruturas? \pause

Quando a informação consiste de dois ou mais itens que juntos descrevem uma entidade.


# Exemplo

Em um determinado programa é necessário exibir para o usuário o tempo que uma operação demorou. Esse tempo está disponível em segundos, mas exibir essa informação em segundos para o usuário pode não ser interessante, afinal, ter uma noção razoável de tempo para 14678 segundos é difícil!

a) Projete uma função que converta uma quantidade de segundos para uma quantidade de horas, minutos e segundos equivalentes.

b) Projete uma função que que converta uma quantidade de horas, minutos e segundos em uma string amigável para o usuário. A string não deve conter informações sobre o tempo que são zeros (por exemplo, não deve informar 0 minutos).


# Especificação

\scriptsize

```cpp
// Converte t em uma mensagem para os usuários. Cada componente de t aparece
// com a sua unidade, mas se o valor do componente for 0, ele não aparece na
// mensagem. Os componentes são separados com " e " ou ", " respeitando as
// regras do Português. Se t for {0, 0, 0}, devolve "0 segundo(s)".
string tempo_para_string(Tempo t)
{
   return "";
}

examples
{
    check_expect(tempo_para_string(Tempo {0, 0, 0}), "0 segundo(s)");
    check_expect(tempo_para_string(Tempo {0, 0, 10}), "10 segundo(s)");
    check_expect(tempo_para_string(Tempo {0, 1, 20}), "1 minuto(s) e 20 segundo(s)");
    check_expect(tempo_para_string(Tempo {0, 2, 0}), "2 minuto(s)");
    check_expect(tempo_para_string(Tempo {1, 2, 1}), "1 hora(s), 2 minuto(s) e 1 segundo(s)");
    check_expect(tempo_para_string(Tempo {4, 0, 25}), "4 hora(s) e 25 segundo(s)");
    check_expect(tempo_para_string(Tempo {2, 4, 0}), "2 hora(s) e 4 minuto(s)");
}
```


#

<div class="columns">
<div class="column" width="48%">
Implementação

\tiny

```cpp
string tempo_para_string(Tempo t) {
    string h = to_string(t.horas) + " hora(s)";
    string m = to_string(t.minutos) + " minuto(s)";
    string s = to_string(t.segundos) + " segundo(s)";
    string msg = "";
    // nos exemplos são 7 casos distintos
    if (t.horas > 0) {
        if (t.minutos > 0) {
            if (t.segundos > 0) {
                msg = h + ", " + m + " e " + s;
            } else {
                msg = h + " e " + m;
            }
        } else if (t.segundos > 0) {
            msg = h + " e " + s;
        } else {
            msg = h;
        }
    } else if (t.minutos > 0) {
        if (t.segundos > 0) {
            msg = m + " e " + s;
        } else {
            msg = m;
        }
    } else {
        msg = s;
    };
    return msg; }
```

</div>
<div class="column" width="48%">
\pause

Implementação alternativa

\tiny

```cpp
string tempo_para_string(Tempo t) {
    // usado para separar cada componente de t
    string sep = "";
    string msg = "";
    if (t.segundos > 0) {
        sep = " e ";
        msg = to_string(t.segundos) + " segundo(s)";
    }

    if (t.minutos > 0) {
        msg = to_string(t.minutos) + " minuto(s)" + sep + msg;
        if (t.segundos > 0) {
            sep = ", ";
        } else {
            sep = " e ";
        }
    }

    if (t.horas > 0) {
        msg = to_string(t.horas) + " hora(s)" + sep + msg;
    }

    if (msg == "") {
        msg = "0 segundo(s)";
    }

    return msg;
}
```
</div>
</div>


# Exercício

Modifique a especificação e implementação da função anterior para que o plural dos componentes fique de acordo com o Português.


# Exemplo

\small

Segundo a Wikipédia, um pixel é o menor elemento de um dispositivo de exibição, como por exemplo, um monitor, ao qual é possível atribuir uma cor. Nos monitores atuais, os pixels são organizados em linhas e colunas, de maneira a formar a imagem exibida. Cada pixel pode ser referenciado por uma coordenada, que é o número da linha e coluna que ele aparece. Por exemplo, em um monitor de 1920 colunas por 1080 linhas, o pixel no canto superior esquerdo está na posição (0, 0), enquanto o pixel no canto inferior direito está na posição (1079, 1919).

Em um ambiente gráfico com muitas janelas, quando um usuário faz um clique com o mouse é necessário identificar em qual janela ocorreu o clique. Considerando que o espaço que uma janela ocupa pode ser representada pela coordenada do canto superior esquerdo e pela quantidade de pixels da largura e da altura da janela

a) Projete uma função que receba como parâmetros as informações sobre uma janela e um clique do mouse e determine se o clique aconteceu sobre a janela.

b) Projete uma função que verifique se os espaços de duas janelas se sobrepõem.


# Definição de tipos de dados

\scriptsize

```cpp
// Representa o espaço que uma janela ocupa em um ambiente gráfico.
//
// A coordenada (x, y) descreve a posição do canto superior esquerdo.
// A largura representa a quantidade de pixels a direita de (x, y)
// e a altura representa a quantidade de pixels abaixo de (x, y).
//
// Os valores da largura e altura devem ser maiores que zero.
struct Janela {
    int x;
    int y;
    int largura;
    int altura;
};
// Representa a posição de um clique em um ambiente gráfico.
// Os valores de x e y devem ser maiores que 0 e menores do que as dimensões do
// ambiente.
struct Clique {
    int x;
    int y;
};
```


# Especificação

\scriptsize

```cpp
// Devolve true se o clique c esta dentro do espaço da janela j, false contrário.
bool dentro_janela(Janela j, Clique c)
{
   return false;
}
```

# Especificação

\scriptsize

```cpp
examples {
    //  x = 100, y = 100, largura = 300, altura = 200
    //
    //        p5
    //      +-----------+
    //  p4  | p1        | p2
    //      |           |
    //      +-----------+
    //        p3
    Janela janela = { 100, 100, 300, 200 };
    // p1 - dentro da janela
    check_expect(dentro_janela(janela, { 150, 150 }), true);
    // p2 - dentro do espaço da altura e depois do espaço da largura
    check_expect(dentro_janela(janela, { 600, 150 }), false);
    // p3 - depois do espaço da altura e dentro do espaço da largura
    check_expect(dentro_janela(janela, { 150, 300 }), false);
    // p4 - dentro do espaço da altura e antes do espaço da largura
    check_expect(dentro_janela(janela, { 150, 50 }), false);
    // p5 - antes do espaço da altura e dentro do espaço da largura
    check_expect(dentro_janela(janela, { 150, 50 }), false);
```


# Especificação

\scriptsize

```cpp
    // canto superior esquerdo
    check_expect(dentro_janela(janela, { 100, 100 }), true);
    // canto superior direito
    check_expect(dentro_janela(janela, { 399, 100 }), true);
    check_expect(dentro_janela(janela, { 400, 100 }), false);
    // canto inferior direito
    check_expect(dentro_janela(janela, { 399, 299 }), true);
    check_expect(dentro_janela(janela, { 400, 299 }), false);
    check_expect(dentro_janela(janela, { 399, 300 }), false);
    check_expect(dentro_janela(janela, { 400, 300 }), false);
    // canto inferior esquerdo
    check_expect(dentro_janela(janela, { 100, 299 }), true);
    check_expect(dentro_janela(janela, { 100, 300 }), false);
}
```

# Implementação

\scriptsize

```cpp
// Devolve true se o clique c esta dentro do espaço da janela j, false contrário.
bool dentro_janela(Janela j, Clique c)
{
    // c.x está dentro do espaço da largura e c.y dentro do espaço da altura
    return j.x <= c.x && c.x < (j.x + j.largura) && j.y <= c.y && c.y < (j.y + j.altura);
}
```

\pause

\normalsize

Verificação: ok \pause

Revisão: ok


# Especificação

\scriptsize

```cpp
// Produz true se o espaço das janelas a e b se soprepõem, false caso contrário.
bool janelas_soprepoem(Janela a, Janela b)
{
    return false;
}

examples
{
    // fixa (eixo y): caixa a vem antes da caixa b
    // variável: posição da borda direita de a
    check_expect(janelas_soprepoem({  10, 20, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 210, 20, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 310, 20, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 410, 20, 100, 200 }, { 300, 400, 50, 100 }), false);
    // fixa: (eixo y) interseção da parte de baixo de a com a parte de cima de b
    // variável: posição da borda direita de a
    check_expect(janelas_soprepoem({  10, 250, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 210, 250, 100, 200 }, { 300, 400, 50, 100 }), true);
    check_expect(janelas_soprepoem({ 310, 250, 100, 200 }, { 300, 400, 50, 100 }), true);
    check_expect(janelas_soprepoem({ 410, 250, 100, 200 }, { 300, 400, 50, 100 }), false);
```

# Especificação

\scriptsize

```cpp
    // fixa: (eixo y) interseção da parte de cima de a com a parte de baixo de b
    // variável: posição da borda direita de a
    check_expect(janelas_soprepoem({  10, 450, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 210, 450, 100, 200 }, { 300, 400, 50, 100 }), true);
    check_expect(janelas_soprepoem({ 310, 450, 100, 200 }, { 300, 400, 50, 100 }), true);
    check_expect(janelas_soprepoem({ 410, 450, 100, 200 }, { 300, 400, 50, 100 }), false);
    // fixa: (eixo y) caixa a vem depois da caixa b
    // variável: posição da borda direita de a
    check_expect(janelas_soprepoem({  10, 550, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 210, 550, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 310, 550, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 410, 550, 100, 200 }, { 300, 400, 50, 100 }), false);
}
```


# Implementação

\scriptsize

```cpp
// Produz true se o espaço das janelas a e b se soprepõem, false caso contrário.
bool janelas_soprepoem(Janela a, Janela b)
{
    return a.x < (b.x + b.largura) &&
           // borda direta de a vem antes da borda esquerda de b
           b.x < (a.x + a.largura) &&
           // borda direta de b vem antes da borda esquerda de a
           a.y < (b.y + b.altura) &&
           // borda superior de a vem antes da borda inferior de b
           b.y < (a.y + a.altura);
           // borda superior de b vem antes da borda inferior de a
}
```


# Exemplo

\small

Em um jogo de loteria os apostadores fazem apostas escolhendo 6 números distintos entre 1 e 60. No sorteio são sorteados 6 números de forma aleatória. Os apostadores que acertam 4, 5 ou 6 números são contemplados com prêmios. Projete uma função que conte quantos números uma determinada aposta acertou.


# Definição de tipos de dados

\scriptsize

```cpp
// Coleção de 6 números distintos entre 1 e 60.
struct SeisNumeros {
    int a;
    int b;
    int c;
    int d;
    int e;
    int f;
};
```

\pause

\normalsize

As apostas e os números sorteados serão representados pela estrutura `SeisNumeros`.


# Especificação

\scriptsize

```cpp
// Calcula quantos números da aposta estão em sorteados.
int numero_acertos(SeisNumeros aposta, SeisNumeros sorteados)
{
    return 0;
}

examples
{
    check_expect(numero_acertos({1, 2, 3, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 0);
    check_expect(numero_acertos({8, 2, 3, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 1);
    check_expect(numero_acertos({8, 12, 3, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 2);
    check_expect(numero_acertos({8, 12, 20, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 3);
    check_expect(numero_acertos({8, 12, 20, 41, 5, 6}, {8, 12, 20, 41, 52, 57}), 4);
    check_expect(numero_acertos({8, 12, 20, 41, 52, 6}, {8, 12, 20, 41, 52, 57}), 5);
    check_expect(numero_acertos({8, 12, 20, 41, 52, 57}, {8, 12, 20, 41, 52, 57}), 6);
}
```


# Implementação

\scriptsize

```cpp
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
```


# Lista de pendências

\scriptsize

```cpp
// Produz true se n é um dos números em sorteados, false caso contrário.
bool sorteado(int n, SeisNumeros sorteados)
{
    return false;
}

examples
{
    SeisNumeros sorteados = {1, 7, 10, 40, 41, 60};
    check_expect(sorteado(1, sorteados), true);
    check_expect(sorteado(7, sorteados), true);
    check_expect(sorteado(10, sorteados), true);
    check_expect(sorteado(40, sorteados), true);
    check_expect(sorteado(41, sorteados), true);
    check_expect(sorteado(60, sorteados), true);
    check_expect(sorteado(2, sorteados), false);
    check_expect(sorteado(15, sorteados), false);
    check_expect(sorteado(49, sorteados), false);
}
```


# Implementação

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

\scriptsize

```cpp
// Produz true se n é um dos números
// em sorteados, false caso contrário.
bool sorteado(int n, SeisNumeros sorteados)
{
    return n == sorteados.a ||
        n == sorteados.b ||
        n == sorteados.c ||
        n == sorteados.d ||
        n == sorteados.e ||
        n == sorteados.f;
}
```

</div>
</div>


# Verificação e Revisão

Verificação: \pause ok \pause

Revisão: \pause o código parece repetitivo... \pause Vamos ver novas construções!
