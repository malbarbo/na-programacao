#include "bscpp.hpp"
#include <string>

using namespace std;

// Concatena as strings de strs uma após a outra.
string concatena(array<string, 5> strs)
{
    string concatenacao = "";
    for (string str : strs) {
        concatenacao = concatenacao + str;
    }
    return concatenacao;
}

examples
{
    check_expect(concatena({"Ola", " ", "mundo", "", "!"}), "Ola mundo!");
    check_expect(concatena({"ab", "c", "de", "", "fgh"}), "abcdefgh");
}

int main()
{
    run_tests();
}
