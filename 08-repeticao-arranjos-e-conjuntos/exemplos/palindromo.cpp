#include "bscpp.hpp"
#include <vector>

using namespace std;

// Produz true se valores é palíndromo, isto é, os elementos de valores vistos
// da esquerda para direita e da direita para esquerda são os mesmos. Produz
// false se valores não é palíndromo.
bool palindromo(vector<int> valores)
{
    bool palindromo = true;
    for (int i = 0, j = valores.size() - 1; i < j && palindromo; i = i + 1, j = j - 1) {
        if (valores[i] != valores[j]) {
            palindromo = false;
        }
    }
    return palindromo;
}

examples {
    check_expect(palindromo({}), true);
    check_expect(palindromo({1}), true);
    check_expect(palindromo({2, 1}), false);
    check_expect(palindromo({1, 2}), false);
    check_expect(palindromo({2, 2}), true);
    check_expect(palindromo({2, 1, 2}), true);
    check_expect(palindromo({4, 4, 2}), false);
    check_expect(palindromo({2, 1, 1, 2}), true);
    check_expect(palindromo({2, 0, 1, 2}), false);
}

int main()
{
    run_tests();
}
