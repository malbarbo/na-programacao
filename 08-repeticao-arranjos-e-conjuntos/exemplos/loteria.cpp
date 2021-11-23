#include "bscpp.hpp"
#include <array>

using namespace std;

// Produz true se n é um dos números em sorteados, false caso contrário.
bool sorteado(int n, array<int, 6> sorteados)
{
    bool sorteado = false;
    for (int s : sorteados) {
        if (n == s) {
            sorteado = true;
        }
    }
    return sorteado;
}

examples
{
    array<int, 6> sorteados = {1, 7, 10, 40, 41, 60};
    check_expect(sorteado(1, sorteados), true);
    check_expect(sorteado(7, sorteados), true);
    check_expect(sorteado(10, sorteados), true);
    check_expect(sorteado(40, sorteados), true);
    check_expect(sorteado(41, sorteados), true);
    check_expect(sorteado(60, sorteados), true);
    check_expect(sorteado(2, sorteados), false);
    check_expect(sorteado(15, sorteados), false);
    check_expect(sorteado(49, sorteados), false);
}

// Calcula quantos números da aposta estão em sorteados.
int numero_acertos(array<int, 6> aposta, array<int, 6> sorteados)
{
    int acertos = 0;
    for (int num : aposta) {
        if (sorteado(num, sorteados)) {
            acertos = acertos + 1;
        }
    }
    return acertos;
}

examples
{
    check_expect(numero_acertos({1, 2, 3, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 0);
    check_expect(numero_acertos({8, 2, 3, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 1);
    check_expect(numero_acertos({8, 12, 3, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 2);
    check_expect(numero_acertos({8, 12, 20, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 3);
    check_expect(numero_acertos({8, 12, 20, 41, 5, 6}, {8, 12, 20, 41, 52, 57}), 4);
    check_expect(numero_acertos({8, 12, 20, 41, 52, 6}, {8, 12, 20, 41, 52, 57}), 5);
    check_expect(numero_acertos({8, 12, 20, 41, 52, 57}, {8, 12, 20, 41, 52, 57}), 6);
}

int main()
{
    run_tests();
}
