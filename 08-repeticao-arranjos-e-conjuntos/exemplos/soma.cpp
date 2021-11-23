#include "bscpp.hpp"
#include <array>

using namespace std;

// Projete uma função que some todos os valores de um arranjo de 7 números.

// Soma os valores de numeros.
int soma(array<int, 7> numeros)
{
    int soma = 0;
    for (int n : numeros) {
        soma = soma + n;
    }
    return soma;
}

examples
{
    check_expect(soma({1, 0, 1, 0, 5, 0, -7}), 0);
    check_expect(soma({1, 0, 1, 0, 5, 0, 10}), 17);
    check_expect(soma({0, -4, 1, 0, -5, -10, 0}), -18);
}

int main()
{
    run_tests();
}
