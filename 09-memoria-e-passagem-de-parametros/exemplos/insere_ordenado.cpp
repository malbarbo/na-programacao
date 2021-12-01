#include "bscpp.hpp"
#include <vector>

using namespace std;

// Insere v em valores de maneira que valores continue em ordem.
//
// Requer que valores esteja ordenado em ordem não decrescente.
void insere_ordenado(vector<int> &valores, int v)
{
    valores.push_back(v);
    for (int i = valores.size() - 1; i > 0 && valores[i - 1] > valores[i]; i = i - 1) {
        int t = valores[i];
        valores[i] = valores[i - 1];
        valores[i - 1] = t;
    }
}

examples
{
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
    check_expect(valores, (vector<int> {1, 2, 10, 10, 12}));
}

int main()
{
    run_tests();
}
