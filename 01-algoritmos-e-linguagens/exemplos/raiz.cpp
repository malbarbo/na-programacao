// Este programa calcula a raiz quadrada de um número a partir de um chute
// inicial informados na linha de comando.
//
// Este programa não faz a validação da entrada.
//
// Para compilar e executar o programa
//
// # No windows
//
// g++ -o raiz.exe raiz.cpp
// raiz.exe 4 1
//
// # No Linux
//
// g++ -o raiz raiz.cpp
// ./raiz 4 1

#include <cassert>
#include <cmath>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    // Entrada
    assert(argc == 3);
    double n = stof(argv[1]); // número que queremos calcular a raiz
    double c = stof(argv[2]); // chute inicial para a raiz

    // Processamento
    while (abs(c * c - n) >= 0.1) {
        c = (c + n / c) / 2;
    }

    // Saída
    cout << c << endl;
}
