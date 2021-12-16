#include "bscpp.hpp"
#include <cmath>

using namespace std;

// Calcula o número de azulejos de 0,2mx0,2m necessários para azulejar uma area
// de tamanho comprimento x altura (em metros) considerando que nenhum azulejo
// é perdido e que recordes são descartados.
int numero_azulejos(double comprimento, double altura)
{
    return ceil(comprimento / 0.2) * ceil(altura / 0.2);
}

examples
{
   // alguns exemplos práticos
   // ceil(2.0 / 0.2) * ceil(2.4 / 0.2) -> 10 * 12 -> 120
   check_expect(numero_azulejos(2.0, 2.4), 120);

   // ceil(1.5 / 0.2) * ceil(2.3 / 0.2) -> 8 * 12 = 96
   check_expect(numero_azulejos(1.5, 2.3), 96);

   // alguns casos extremos
   check_expect(numero_azulejos(0.2, 0.2), 1);
   check_expect(numero_azulejos(0.3, 0.2), 2);
   check_expect(numero_azulejos(0.3, 0.3), 4);
   check_expect(numero_azulejos(0.4, 0.4), 4);
}

int main()
{
    run_tests();
}
