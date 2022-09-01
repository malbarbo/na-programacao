#include "bscpp.hpp"
#include <string>

using namespace std;

// Análise
//
// Verificar se o primeiro nome de uma pessoa é Paula.
//
// Definição de tipos de dados
//
// O nome da pessoa será representado por uma string.

// Devolve true se o primeiro nome de nome_completo é "Paula", false caso
// contrário.
bool primeiro_nome_eh_paula(string nome_completo)
{
    return nome_completo == "Paula" || nome_completo.substr(0, 6) == "Paula ";
}

examples {
    // nome_completo == "Paula"  ||  nome_completo.substr(0, 6) == "Paula "
    check_expect(primeiro_nome_eh_paula("Paula"), true);
    check_expect(primeiro_nome_eh_paula("Paula de Souza"), true);
    check_expect(primeiro_nome_eh_paula("Paulas de Souza"), false);
    check_expect(primeiro_nome_eh_paula("Alberto de Souza"), false);
    check_expect(primeiro_nome_eh_paula("Paulo de Freitas"), false);
    check_expect(primeiro_nome_eh_paula("Jorge de Paula Souza"), false);
    check_expect(primeiro_nome_eh_paula("Aida"), false);
    check_expect(primeiro_nome_eh_paula("Paula"), true);
}


// Análise
//
// Verificar se o sobrenome de uma pessoa é Silva
//
// Tipos de dados
//
// O nome será representado por uma string.

// Devolve true se o último nome de nome_completo é "Silva" (nome_completo
// precisa ter pelo menos dois nomes), false caso contrário.
bool ultimo_nome_eh_silva(string nome_completo)
{
    return nome_completo.length() >= 6 &&
        // termina com " Silva"
        nome_completo.substr(nome_completo.length() - 6, 6) == " Silva";
}

examples {
    // nome_completo.length() >= 6 && nome_completo.substr(nome_completo.length() - 6, 6) == " Silva"
    check_expect(ultimo_nome_eh_silva("Paulo Silva"), true);
    check_expect(ultimo_nome_eh_silva("Paulo D'Silva"), false);
    check_expect(ultimo_nome_eh_silva("Paulo Silva Barbosa"), false);
    check_expect(ultimo_nome_eh_silva("Paulo Barbosa Silva"), true);
    check_expect(ultimo_nome_eh_silva("Silva"), false);
    check_expect(ultimo_nome_eh_silva("Aida"), false);
}

int main()
{
    run_tests();
}
