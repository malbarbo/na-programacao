#include "bscpp.hpp"

using namespace std;

// Conta quantas vezes val aparece nos
// primeiros n elementos de valores.
// Requer que 0 <= n <= valores.size()
int freq(int val,
         const vector<int> &valores,
         int n) {
    int cont;
    if (n == 0) {
        cont = 0;
    } else {
        if (valores[n - 1] == val) {
            cont = 1 + freq(val, valores, n - 1);
        } else {
            cont = freq(val, valores, n - 1);
        }
    }
    return cont;
}

examples
{
    check_expect(freq(1, {5, 1, 4, 1}, 0), 0);
    check_expect(freq(1, {5, 1, 4, 1}, 1), 0);
    check_expect(freq(1, {5, 1, 4, 1}, 2), 1);
    check_expect(freq(1, {5, 1, 4, 1}, 3), 1);
    check_expect(freq(1, {5, 1, 4, 1}, 4), 2);
}

int main()
{
    run_tests();
}
