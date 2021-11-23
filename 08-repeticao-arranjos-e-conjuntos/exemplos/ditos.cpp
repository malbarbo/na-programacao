#include "bscpp.hpp"
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

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

examples
{
    string dito1 = "Esmola demais até santo desconfia";
    string dito2 = "Diga com quem anda que lhe direi quem és";
    string dito3 = "Saco vazio não para em pé";
    check_expect(classifica_ditos_unicos_em_ordem({}),
                 (vector<string> {}));

    check_expect(classifica_ditos_unicos_em_ordem({dito1, dito2, dito1}),
                 (vector<string> {dito2, dito1}));

    check_expect(classifica_ditos_unicos_em_ordem({dito3, dito1, dito2, dito1, dito3, dito1, dito3, dito2}),
                 (vector<string> {dito2, dito1, dito3}));
}

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

// Escreve na saída padrão os ditos.
void escreve_ditos(vector<string> ditos)
{
    for (string dito: ditos) {
        cout << dito << endl;
    }
}

int main()
{
    // run_tests();

    // Leitura da entrada
    vector<string> ditos = le_ditos();

    // Processamento
    vector<string> ditos_unicos = classifica_ditos_unicos_em_ordem(ditos);

    // Saída
    escreve_ditos(ditos_unicos);
}
