#include <iostream>
#include <string>

using namespace std;

int main()
{
    cout << "Nome: ";
    string nome;
    getline(cin, nome);

    cout << "Ola " << nome <<  ", seja bem vindo!" << endl;
}
