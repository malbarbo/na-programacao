#include "bscpp.hpp"
#include <array>

using namespace std;

// O sinal de um número.
enum Sinal {
    Positivo,
    Negativo,
    Nenhum,
};

// Verifica se existem mais números positivos ou negativos no arranjo numeros.
// Devolve Positivo se existem mais positivos do que negativos.
// Devolve Negativo se existem mais negativos do que positivos.
// Devolve Nenhum se a quantidade de positivos é igual a de negativos.
Sinal mais_positivos_ou_negativos(array<int, 5> numeros)
{
    int num_positivos = 0;
    int num_negativos = 0;
    for (int num : numeros) {
        if (num > 0) {
            num_positivos = num_positivos + 1;
        } else if (num < 0) {
            num_negativos = num_negativos + 1;
        }
    }
    Sinal sinal = Nenhum;
    if (num_positivos > num_negativos) {
        sinal = Positivo;
    } else if (num_negativos > num_positivos) {
        sinal = Negativo;
    }
    return sinal;
}

examples
{
    check_expect(mais_positivos_ou_negativos({1, 2, 3, -1, 0}), Positivo);
    check_expect(mais_positivos_ou_negativos({1, 2, 3, -1, -2}), Positivo);
    check_expect(mais_positivos_ou_negativos({-4, 2, 3, -1, -2}), Negativo);
    check_expect(mais_positivos_ou_negativos({-4, 2, 3, 0, -2}), Nenhum);
}


int main()
{
    run_tests();
}
