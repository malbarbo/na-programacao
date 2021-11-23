#include "bscpp.hpp"
#include <vector>

using namespace std;

// Analise
//
// - Ordenar os valores de um arranjo de entrada em um novo arranjo de saída.
// - Usando o algoritmo de ordenação por inserção.
// - Ordenados em ordem não-decrescente
//
// Definição de tipos de dados
//
// - Os arranjos de entrada e saída serão de elementos inteiros


// Cria um novo vector com os mesmos elementos de valores e com n em ordem não
// decrescente. Ou seja, insere o valor de forma ordenada em valores.
// Requer que valores esteja em ordem não decrescente.
vector<int> insere_ordenado(vector<int> valores, int n)
{
    // seleciona os menores ou iguais a n
    vector<int> saida = {};
    for (int valor : valores) {
        if (valor <= n) {
            saida.push_back(valor);
        }
    }

    saida.push_back(n);

    // seleciona os maiores que n
    for (int valor : valores) {
        if (valor > n) {
            saida.push_back(valor);
        }
    }

    return saida;
}

examples
{
    check_expect(insere_ordenado({}, 4), (vector<int> {4}));
    check_expect(insere_ordenado({1}, 4), (vector<int> {1, 4}));
    check_expect(insere_ordenado({1}, 0), (vector<int> {0, 1}));
    check_expect(insere_ordenado({1, 3}, 1), (vector<int> {1, 1, 3}));
    check_expect(insere_ordenado({3, 3, 5, 5, 8}, 4), (vector<int> {3, 3, 4, 5, 5, 8}));
}

// Ordena os valores do arranjo valores em ordem não-decrescente usando o
// algoritmo de ordenação por inserção.
vector<int> ordenacao_insercao(vector<int> valores)
{
    vector<int> saida = {};
    for (int valor : valores) {
        saida = insere_ordenado(saida, valor);
    }
    return saida;
}

examples
{
    check_expect(ordenacao_insercao({}), (vector<int> {}));
    check_expect(ordenacao_insercao({8}), (vector<int> {8}));
    check_expect(ordenacao_insercao({8, 2}), (vector<int> {2, 8}));
    check_expect(ordenacao_insercao({5, 3, 7, 1}), (vector<int> {1, 3, 5, 7}));
    check_expect(ordenacao_insercao({1, 3, 3, 1}), (vector<int> {1, 1, 3, 3}));
}

int main()
{
    run_tests();
}
