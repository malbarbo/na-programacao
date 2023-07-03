#include "bscpp.hpp"
#include <string>

using namespace std;

// Como parte de um jogo educativo online, você deve projetar uma função que
// gere uma sentença descrevendo quantas letras uma palavra tem. Por
// exemplo, para a palavras “casa”, a função deve gerar a sentença “A
// palavra ‘casa’ tem 4 letras”.

// Análise
//
// Gerar uma sentença dizendo quantos letras uma palavra tem.
//
// Tipos de dados
//
// A palavra e a sentença serão representadas por strings.
//
// Especificação
//
// - Assinatura (nome, entradas e saídas)
// - Propósito
// - Exemplos

// Gera uma sentença dizendo quantas letras a palavra p tem.
// A senteça tem a forma "A palavra 'p' tem x letras", onde
// p é a palavra e x é a quantidade de letras de p.
string msg_quantas_letras(string p)
{
    return "A palavra '" + p + "' tem " + to_string(p.length()) + "letras";
}

examples
{
    check_expect(msg_quantas_letras("casa"),
                 "A palavra 'casa' tem 4 letras");
    // "A palavra '" + p + "' tem " + to_string(p.length()) + "letras"
}

int main()
{
    run_tests();
}
