#include "bscpp.hpp"
#include <vector>

using namespace std;

// Cria um nova arranjo inserindo o valor no índice pos de valores.
// Requer que 0 <= pos <= valores.size().
vector<int> insere_posicao(vector<int> valores, int pos, int valor)
{
    vector<int> resultado = {};

    for (int i = 0; i < pos; i = i + 1) {
        resultado.push_back(valores[i]);
    }

    resultado.push_back(valor);

    for (int i = pos; i < valores.size(); i = i + 1) {
        resultado.push_back(valores[i]);
    }

    return resultado;
}

examples {
    check_expect(insere_posicao({}, 0, 10), (vector<int> {10}));
    check_expect(insere_posicao({8}, 0, 10), (vector<int> {10, 8}));
    check_expect(insere_posicao({8}, 1, 10), (vector<int> {8, 10}));
    check_expect(insere_posicao({2, 8}, 0, 3), (vector<int> {3, 2, 8}));
    check_expect(insere_posicao({2, 8}, 1, 3), (vector<int> {2, 3, 8}));
    check_expect(insere_posicao({2, 8}, 2, 3), (vector<int> {2, 8, 3}));
}

int main()
{
    run_tests();
}
