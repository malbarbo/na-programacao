#include "bscpp.hpp"
#include <vector>

using namespace std;

// Produz true se n é um número primo, isto é, se n tem exatamente dois
// divisores distintos, 1 e ele mesmo. Produz false se n não é primo.
bool primo(int n)
{
    bool primo = n > 1;
    for (int i = 2; i <= n / 2 && primo; i = i + 1) {
        if (n % i == 0) {
            primo = false;
        }
    }
    return primo;
}

examples
{
    check_expect(primo(1), false);
    check_expect(primo(2), true);
    check_expect(primo(3), true);
    check_expect(primo(4), false);
    check_expect(primo(5), true);
    check_expect(primo(8), false);
    check_expect(primo(11), true);
}

int main()
{
    run_tests();
}
