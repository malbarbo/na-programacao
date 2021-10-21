#include "bscpp.hpp"

using namespace std;

// Representa o tipo do combustível.
enum Combustivel {
    Alcool,
    Gasolina,
};

// Indica o combustível que deve ser utilizado no abastecimento. Produz
// Alcool se preco-alcool for menor ou igual a 70% do preco-gasolina,
// produz Gasolina caso contrário.
Combustivel indica_combustivel(double preco_alcool, double preco_gasolina)
{
    Combustivel combustivel;
    if (preco_alcool <= 0.7 * preco_gasolina) {
        combustivel = Alcool;
    } else {
        combustivel = Gasolina;
    }
    return combustivel;
}

examples
{
    // 4.000 <= 0.7 * 5.000 -> 4.000 <= 3.500 -> false -> Gasolina
    check_expect(indica_combustivel(4.000, 5.000), Gasolina);
    // 4.000 <= 0.7 * 6.000 -> 4.000 <= 4.200 -> true -> Alcool
    check_expect(indica_combustivel(4.000, 6.000), Alcool);
    // 3.500 <= 0.7 * 5.000 -> 3.500 <= 3.500 -> true -> Alcool
    check_expect(indica_combustivel(3.500, 5.000), Alcool);
}

int main()
{
    run_tests();
}
