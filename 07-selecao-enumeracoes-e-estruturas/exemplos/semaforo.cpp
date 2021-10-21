#include "bscpp.hpp"

// Análise
//
// Calcular a próxima cor de uma semaforo que tem as cores verde, amarelo e vermelho.
//
// Definição de tipos de dados

// Representa a cor de um semáforo.
enum Cor {
    Verde,
    Vermelho,
    Amarelo,
};


// Produz a próximo cor de um semáforo que está com a cor c.
Cor proxima_cor(Cor c) {
    Cor proxima;
    switch (c) {
        case Verde:
            proxima = Amarelo;
            break;
        case Vermelho:
            proxima = Verde;
            break;
        case Amarelo:
            proxima = Vermelho;
            break;
    }
    return proxima;
}

examples
{
    check_expect(proxima_cor(Verde), Amarelo);
    check_expect(proxima_cor(Vermelho), Verde);
    check_expect(proxima_cor(Amarelo), Vermelho);
}


int main()
{
    run_tests();
}
