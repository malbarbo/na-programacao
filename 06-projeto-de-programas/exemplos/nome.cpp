#include <iostream>

using namespace std;

// Devolve true se o primeiro nome de nome_completo é "Paula",
// false caso contrário.
// Exemplos
// primeiro_nome_paula("Paula Silva") -> true
// primeiro_nome_paula("Paulas Silva") -> false
// primeiro_nome_paula("Paula") -> true
// primeiro_nome_paula("Paulas") -> false
// primeiro_nome_paula("Paulana") -> false
// primeiro_nome_paula("paula") -> false
// primeiro_nome_paula("PAULA") -> false
bool primeiro_nome_paula(string nome_completo)
{
    return nome_completo == "Paula" || nome_completo.substr(0, 6) == "Paula ";
}

// Devolve true se o último sobrenome de nome_completo é "Silva",
// false caso contrario.
// Exemplo
// sobrenome_silva("Paula Silva") -> true
//   nome_completo.substr(nome_completo.length() - 6, 6) == " Silva"
// sobrenome_silva("Jose Roberto Silva") -> true
//   nome_completo.substr(nome_completo.length() - 6, 6) == " Silva"
// sobrenome_silva("Silva") -> false
// sobrenome_silva("Jose SaSilva") -> false
// sobrenome_silva("Paula Silvana") -> false
// sobrenome_silva("Jose Silva Roberto") -> false
// sobrenome_silva("paula silva") -> false
bool sobrenome_silva(string nome_completo) {
    return (nome_completo.length() >= 6) && nome_completo.substr(nome_completo.length() - 6, 6) == " Silva";
}

int main()
{
    cout << "nome: ";
    string nome;
    getline(cin, nome);

    bool eh_paula = primeiro_nome_paula(nome);
    bool eh_silva = sobrenome_silva(nome);

    cout << boolalpha;
    cout << "primeiro nome paula? " << eh_paula << endl;
    cout << "sobrenome silva? " << eh_silva << endl;
}
