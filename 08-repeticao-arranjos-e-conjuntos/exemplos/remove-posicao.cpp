#include "bscpp.hpp"
#include <vector>

using namespace std;

// Cria um nova arranjo removendo o elemento da posição pos de valores.
// Requer que 0 <= pos < valores.size().
vector<int> remove_posicao(vector<int> valores, int pos)
{
    vector<int> resultado = {};

    for (int i = 0; i < pos; i = i + 1) {
        resultado.push_back(valores[i]);
    }

    for (int i = pos + 1; i < valores.size(); i = i + 1) {
        resultado.push_back(valores[i]);
    }

    return resultado;
}

examples {
    check_expect(remove_posicao({8}, 0), (vector<int> {}));
    check_expect(remove_posicao({2, 8}, 0), (vector<int> {8}));
    check_expect(remove_posicao({2, 8}, 1), (vector<int> {2}));
    check_expect(remove_posicao({7, 2, 8}, 0), (vector<int> {2, 8}));
    check_expect(remove_posicao({7, 2, 8}, 1), (vector<int> {7, 8}));
    check_expect(remove_posicao({7, 2, 8}, 2), (vector<int> {7, 2}));
}

int main()
{
    run_tests();
}
