#include <iostream>

using namespace std;

int main()
{
    cout << "Idade: ";
    int idade;
    cin >> idade;

    cout << "E professor? ";
    bool eh_professor;
    cin >> eh_professor;

    // Note que && tem priodade sobre ||
    bool livre = idade < 10 || idade >= 60 || idade >= 50 && eh_professor;

    cout << "Pode usar o transporte publico de forma gratuita? " << livre << endl;
}
