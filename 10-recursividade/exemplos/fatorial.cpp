#include "bscpp.hpp"

using namespace std;

// Calcula o fatorial de n, isto é, o produto dos n primeiros números naturais
// maiores que 0.
//
// Requer que n >= 0.
int fatorial(int n)
{
    int fat;
    if (n == 0) {
        fat = 1;
    } else {
        fat = n * fatorial(n - 1);
    }
    return fat;
}

examples
{
    check_expect(fatorial(0), 1);
    check_expect(fatorial(1), 1);
    check_expect(fatorial(2), 2);
    check_expect(fatorial(3), 6);
    check_expect(fatorial(4), 24);
}

int main()
{
    run_tests();
}
