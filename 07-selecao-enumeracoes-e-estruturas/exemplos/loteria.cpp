#include "bscpp.hpp"

// Coleção de 6 números distintos entre 1 e 60.
struct SeisNumeros {
    int a;
    int b;
    int c;
    int d;
    int e;
    int f;
};

// Produz true se n é um dos números em sorteados, false caso contrário.
bool sorteado(int n, SeisNumeros sorteados)
{
    return n == sorteados.a ||
        n == sorteados.b ||
        n == sorteados.c ||
        n == sorteados.d ||
        n == sorteados.e ||
        n == sorteados.f;
}

examples
{
    SeisNumeros sorteados = {1, 7, 10, 40, 41, 60};
    check_expect((SeisNumeros {1, 7, 10, 40, 41, 60}), sorteados)
    check_expect(sorteado(1, sorteados), true);
    check_expect(sorteado(7, sorteados), true);
    check_expect(sorteado(10, sorteados), true);
    check_expect(sorteado(40, sorteados), true);
    check_expect(sorteado(41, sorteados), true);
    check_expect(sorteado(60, sorteados), true);
    check_expect(sorteado(2, sorteados), false);
    check_expect(sorteado(15, sorteados), false);
    check_expect(sorteado(49, sorteados), false);
}

// Calcula quantos números da aposta estão em sorteados.
int numero_acertos(SeisNumeros aposta, SeisNumeros sorteados)
{
    int acertos = 0;
    if (sorteado(aposta.a, sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta.b, sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta.c, sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta.d, sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta.e, sorteados)) {
        acertos = acertos + 1;
    }
    if (sorteado(aposta.f, sorteados)) {
        acertos = acertos + 1;
    }
    return acertos;
}

examples
{
    // verificar cada número de aposta e conta 1 se estiver em sorteados
    check_expect(numero_acertos({1, 2, 3, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 0);
    check_expect(numero_acertos({8, 2, 3, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 1);
    check_expect(numero_acertos({8, 12, 3, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 2);
    check_expect(numero_acertos({8, 12, 20, 4, 5, 6}, {8, 12, 20, 41, 52, 57}), 3);
    check_expect(numero_acertos({8, 12, 20, 41, 5, 6}, {8, 12, 20, 41, 52, 57}), 4);
    check_expect(numero_acertos({8, 12, 20, 41, 52, 6}, {8, 12, 20, 41, 52, 57}), 5);
    check_expect(numero_acertos({8, 12, 20, 41, 52, 57}, {8, 12, 20, 41, 52, 57}), 6);
}

int main()
{
    run_tests();
}
