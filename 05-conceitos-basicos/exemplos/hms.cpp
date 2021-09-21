// Projete um programa que a partir de um tempo especificado em número de
// horas, minuto e segundos, calcule o total de segundos do tempo.

#include <iostream>

using namespace std;

// As h, m, s serão representados por inteiros positivos

// Calcula o total de segundos do tempo com h horas,
// m minutos e s segundos.
// Exemplos
// h=0 m=0 s=4 -> 4 + 0 * 60 + 0 * 3600 -> 4
// h=0 m=10 s=5 -> 5 + 10 * 60 + 0 * 3600 -> 605
// h=3 m=2 s=25 -> 25 + 2 * 60 + 3 * 3600 -> 10945
int total_segundos(int h, int m, int s)
{
    return s + m * 60 + h * 3600;
}

int main()
{
    cout << "Horas: ";
    int horas;
    cin >> horas;

    cout << "Minutos: ";
    int min;
    cin >> min;

    cout << "Segundos: ";
    int segs;
    cin >> segs;

    int t = total_segundos(horas, min, segs);

    cout << "Total de segundos: " << t << endl;
}
