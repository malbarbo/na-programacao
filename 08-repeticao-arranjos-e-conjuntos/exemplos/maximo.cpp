#include "bscpp.hpp"
#include <array>

using namespace std;

// Encontra o valor máximo de numeros.
int maximo(array<int, 5> numeros)
{
    int max = numeros[0];
    for (int num : numeros) {
        if (num > max) {
            max = num;
        }
    }
    return max;
}

examples
{
    check_expect(maximo({5, 4, 1, 0, 7}), 7);
    check_expect(maximo({1, -5, 8, 1, 2}), 8);
    check_expect(maximo({-4, -6, -1, -1, -3}), -1);
}

int main()
{
    run_tests();
}
