#include "bscpp.hpp"

// Calcula o custo em reais para percorrer a distancia especificada
// considerando o rendimento do carro e o preco do litro do combustível.
double custo_viagem(double distancia, double rendimento, double preco)
{
    return (distancia / rendimento) * preco;
}

examples {
    check_expect(custo_viagem(120, 10, 5), 60);
    check_expect(custo_viagem(300, 15, 6), 120);
}

int main()
{
    run_tests();
}
