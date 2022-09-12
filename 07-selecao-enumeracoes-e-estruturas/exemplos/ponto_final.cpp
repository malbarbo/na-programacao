#include "bscpp.hpp"
#include <string>

using namespace std;

// Análise
//
// Colocar um ponto final em um texto se ela não terminar com ponto final.
//
// Definição de tipos de dados
//
// O texto é representada por uma string.



// Produz s se s é vazia ou termina com um ponto final, caso contrário
// produz s seguido de um ponto final.
//
// Requer que s não termine com espaço.
string coloca_ponto_se_necessario(string s)
{
    string r;
    // s é vazia ou o último caractere é "."
    if (s == "" || s.substr(s.length() - 1, 1) == ".") {
        r = s;
    } else {
        r = s + ".";
    }
    return r;
}

examples
{
    // Coloca o ponto
    // s.substr(s.length() - 1, 1) == "." é false
    check_expect(coloca_ponto_se_necessario("casa"), "casa.");
    // s.substr(s.length() - 1, 1) == "." é false
    check_expect(coloca_ponto_se_necessario("eu tambem"), "eu tambem.");
    // Não coloca o ponto
    // s.substr(s.length() - 1, 1) == "." é true
    check_expect(coloca_ponto_se_necessario("casa."), "casa.");
    // s == "" é true
    check_expect(coloca_ponto_se_necessario(""), "");
}

int main()
{
    run_tests();
}
