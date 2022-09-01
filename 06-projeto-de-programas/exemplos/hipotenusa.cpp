#include "bscpp.hpp"
#include <cmath>

using namespace std;

// Calcula o valor da hipotenusa a partir dos catetos cat_a e cat_b.
// hipotenusa(3.0, 4.0) -> sqrt(3.0 * 3.0 + 4.0 * 4.0) -> 5.0
// hipotenusa(6.0, 8.0) -> sqrt(6.0 * 6.0 + 8.0 * 8.0) -> 10.0
double hipotenusa(double cat_a, double cat_b)
{
    return sqrt(cat_a * cat_a + cat_b * cat_b);
}

examples {
    check_expect(hipotenusa(3.0, 4.0), 5.0); // sqrt(3.0 * 3.0 + 4.0 * 4.0) -> 5.0
    check_expect(hipotenusa(6.0, 8.0), 10.0); // sqrt(6.0 * 6.0 + 8.0 * 8.0) -> 10.0
}

int main()
{
    run_tests();
}
