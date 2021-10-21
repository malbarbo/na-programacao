#include "bscpp.hpp"
#include <string>

using namespace std;

// Análise
//
// Colocar um ponto final em um texto se ela não terminar com ponto final.
//
// Definição de tipos de dados
//
// O texto é representada por um string.



// Produz se s se é vazio ou termina com um ponto final, caso contrário
// produz s seguido de um ponto final.
//
// Requer que s não termine com espaço.
string coloca_ponto_se_necessario(string s)
{
    string r;
    // s é vazio ou o último caractere é "."
    if (s == "" || (s.substr(s.length() - 1, 1) == ".")) {
        r = s;
    } else {
        r = s + ".";
    }
    return r;
}

examples
{
    // s = "casa", s.substr(3, 1) -> "a" == "." -> false -> adiciona ponto
    check_expect(coloca_ponto_se_necessario("casa"), "casa.");
    // s = "casa.", s.substr(4, 1) -> "." == "." -> true -> devolve s
    check_expect(coloca_ponto_se_necessario("casa."), "casa.");
    check_expect(coloca_ponto_se_necessario("casa ."), "casa .");
    // s = "eu tambem", s.substr(8, 1) -> "m" == "." -> false -> adiciona ponto
    check_expect(coloca_ponto_se_necessario("eu tambem"), "eu tambem.");
    check_expect(coloca_ponto_se_necessario(""), "");
}

int main()
{
    run_tests();
}
