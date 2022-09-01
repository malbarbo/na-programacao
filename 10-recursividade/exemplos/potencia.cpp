#include "bscpp.hpp"

using namespace std;

// Calcula a elevado a n.
//
// Requer que a != 0 e n >= 0.
double potencia(double a, int n)
{
    double pot;
    if (n == 0) {
        pot = 1;
    } else {
        pot = a * potencia(a, n - 1);
    }
    return pot;
}

examples
{
    check_expect(potencia(2, 0), 1.0);
    check_expect(potencia(2, 1), 2.0);
    check_expect(potencia(2, 2), 4.0);
    check_expect(potencia(2, 3), 8.0);

    check_expect(potencia(3, 0), 1.0);
    check_expect(potencia(3, 1), 3.0);
    check_expect(potencia(3, 2), 9.0);
    check_expect(potencia(3, 3), 27.0);

    check_expect(potencia(-3, 3), -27.0);
}

int main()
{
    run_tests();
}
