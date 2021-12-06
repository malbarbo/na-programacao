#include "bscpp.hpp"

using namespace std;

// Soma todos os número naturais menores ou iguais que n.
//
// Requer que n >= 0.
int soma_naturais(int n)
{
    int soma;
    if (n == 0) {
        soma = 0;
    } else {
        soma = n + soma_naturais(n - 1);
    }
    return soma;
}

examples
{
    check_expect(soma_naturais(0), 0);
    check_expect(soma_naturais(1), 1);
    check_expect(soma_naturais(2), 3);
    check_expect(soma_naturais(3), 6);
    check_expect(soma_naturais(4), 10);
}

int main()
{
    run_tests();
}
