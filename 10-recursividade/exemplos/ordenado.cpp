#include "bscpp.hpp"

using namespace std;

// Verifica se os primeiros n elementos de valores estão em ordem
// não-decrescente.
//
// Requer que 0 <= n <= valores.size()
bool ordenado(const vector<int>& valores, int n)
{
    bool ord;
    if (n <= 1) {
        ord = true;
    } else {
        ord = valores[n - 2] <= valores[n - 1] && ordenado(valores, n - 1);
    }
    return ord;
}

examples
{
    check_expect(ordenado({ 1, 2, 3, 2 }, 0), true);
    check_expect(ordenado({ 1, 2, 3, 2 }, 1), true);
    check_expect(ordenado({ 1, 2, 3, 2 }, 2), true);
    check_expect(ordenado({ 1, 2, 3, 2 }, 3), true);
    check_expect(ordenado({ 1, 2, 3, 2 }, 4), false);
}

int main()
{
    run_tests();
}
