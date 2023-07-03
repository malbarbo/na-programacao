#include "bscpp.hpp"

// O Tony é consultor de projetos de software e cobra 150 reais a hora de
// consultoria. Ele trabalha entre 20 e 50 horas por semana. Projete um
// programa que calcule quanto o Tony receberá após trabalhar um determinado
// número de horas.

// Análise
//
// Calcular quanto uma pessoa ganhará após trabalhar um determinado número
// de horas, sabendo que ela 150 por hora.
//
// Tipos dados
//
// horas - número inteiro positivo
// salario - número positivo com duas casas decimais
//
// Especificação
// - Assinatura (nome, entradas e as saídas)
// - Propósito
// - Exemplos

// Calcula o salario de um trabalhador que ganha 150 por hora após trabalhar
// h horas.
double salario(int h)
{
    return h * 150;
}

examples
{
    check_expect(salario(3), 450.0); // 3 * 150
    check_expect(salario(10), 1500.0); // 10 * 150
}

int main()
{
    run_tests();
}
