#include <iostream>

using namespace std;

// Calcula a unidade de n.
// Exemplos
// unidade(152) -> 152 % 10 -> 2
// unidade(17) -> 17 % 10 -> 7
// unidade(40) -> 40 % 10 -> 0
int unidade(int n)
{
    return n % 10;
}


// Calcula a dezena de n.
// Exemplos
// dezena(152) -> (152 / 10) % 10 -> 15 % 10 -> 5
// dezena(423) -> (423 / 10) % 10 -> 42 % 10 -> 2
// dezena(7)   -> (7 / 10) % 10 -> 0 % 10 -> 0
// dezena(1234) -> (1234 / 10) % 10 -> 123 % 10 -> 3
int dezena(int n)
{
    return (n / 10) % 10;
}


// Calcula a centena de n.
// Exemplo
// centena(152) -> (152 / 100) % 10 -> 1 % 10 -> 1
// centena(4567) -> (4567 / 100) % 10 -> 45 % 10 -> 5
int centena(int n)
{
    return (n / 100) % 10;
}

int main()
{
    cout << "numero: ";
    int x;
    cin >> x;

    int u = unidade(x);
    cout << "unidade: " << u << endl;

    int d = dezena(x);
    cout << "dezena: " << d << endl;

    int c = centena(x);
    cout << "centena: " << c << endl;
}
