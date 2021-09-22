#include <cmath>
#include <iostream>

using namespace std;

// Calcula o valor da hipotenusa a partir dos catetos.
// Exemplos
// hipotenusa(3.0, 4.0) -> sqrt(3.0 * 3.0 + 4.0 * 4.0) -> 5.0
// hipotenusa(6.0, 8.0) -> sqrt(6.0 * 6.0 + 8.0 * 8.0) -> 10.0
double hipotenusa(double cat_a, double cat_b)
{
    return sqrt(cat_a * cat_a + cat_b * cat_b);
}

int main()
{
    cout << "cateto a: ";
    double a;
    cin >> a;

    cout << "cateto b: ";
    double b;
    cin >> b;

    double hip = hipotenusa(a, b);

    cout << "hipotenusa: " << hip << endl;
}
