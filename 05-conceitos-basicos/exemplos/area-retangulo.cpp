// Este programa calcula a area de um retangulo a partir da medida da
// base e da altura informados pelo usuário.
//
// Obs: Os dados de entrada não são validados.

#include <iostream>

using namespace std;

int main()
{
    cout << "Digite a medida da base: ";
    double base;
    cin >> base;

    cout << "Digite a medida da altura: ";
    double altura;
    cin >> altura;

    double area = base * altura;
    cout << "A area do retangulo e "
         << area
         << "."
         << endl;
}
