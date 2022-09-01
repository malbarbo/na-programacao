#include "bscpp.hpp"

// Analise
//
// Calcular o custo em reais para percorrer uma determinada distância levando
// em consideração o desempenho   do carro e o preço do litro do combustível.
//
// Tipos de dados
//
// As informações são a distância em Km, rendimento em Km/l, preço em R$/l e o
// custo da viagem em R$.  Todos os valores serão representados por números
// positivos.

// Calcula o custo para percorrer a distancia especificada considerando o
// rendimento do carro e o preco do litro do combustível.
double custo_viagem(double distancia, double rendimento, double preco)
{
    return (distancia / rendimento) * preco;
}

examples {
    check_expect(custo_viagem(120, 10, 5), 60.0); // (120 / 10) * 5
    check_expect(custo_viagem(300, 15, 6), 120.0); // (300 / 15) * 6
}

int main()
{
    run_tests();
}
