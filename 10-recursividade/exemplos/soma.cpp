#include "bscpp.hpp"

using namespace std;

// Soma os primeiros n elementos de valores.
// Requere que 0 <= n <= valores.size()
int soma(const vector<int> &valores, int n)
{
    int s;
    if (n == 0) {
        s = 0;
    } else {
        s = valores[n - 1] + soma(valores, n - 1);
    }
    return s;
}

examples
{
    check_expect(soma({5, 1, 4, 3}, 0), 0);
    check_expect(soma({5, 1, 4, 3}, 1), 5);
    check_expect(soma({5, 1, 4, 3}, 2), 6);
    check_expect(soma({5, 1, 4, 3}, 3), 10);
    check_expect(soma({5, 1, 4, 3}, 4), 13);
}

int main()
{
    run_tests();
}
