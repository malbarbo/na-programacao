#include "bscpp.hpp"
#include <vector>

using namespace std;

// Encontra o índice da primeira ocorrência do valor máximo de valores.
int indice_maximo(vector<int> valores)
{
    int imax = 0;
    for (int i = 1; i < valores.size(); i = i + 1) {
        if (valores[i] > valores[imax]) {
            imax = i;
        }
    }
    return imax;
}

examples
{
    check_expect(indice_maximo({5}), 0);
    check_expect(indice_maximo({5, 5}), 0);
    check_expect(indice_maximo({5, 7, 5}), 1);
    check_expect(indice_maximo({5, 7, 5, 8}), 3);
}

int main()
{
    run_tests();
}
