#include "bscpp.hpp"
#include <string>
#include <vector>
#include <iostream>

using namespace std;

// Produz uma lista das "partes" de s usando espaços como delimitador.
vector<string> separa(string s)
{
    vector<string> palavras = {};
    int inicio = 0;
    while (inicio < s.length()) {
        int fim = s.find(" ", inicio);
        if (fim != -1) {
            if (fim != inicio) {
                palavras.push_back(s.substr(inicio, fim - inicio));
            }
            inicio = fim + 1;
        } else {
            palavras.push_back(s.substr(inicio, s.length() - inicio));
            inicio = s.length();
        }
    }
    return palavras;
}

examples
{
    check_expect(separa(""), (vector<string> {}));
    check_expect(separa("    "), (vector<string> {}));
    check_expect(separa("casa"), (vector<string> {"casa"}));
    check_expect(separa("  minha   casa  "), (vector<string> {"minha", "casa"}));
    check_expect(separa("Seu Jorge cantou"), (vector<string> {"Seu", "Jorge", "cantou"}));
}

int main()
{
    run_tests();
}
