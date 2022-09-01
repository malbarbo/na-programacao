#include "bscpp.hpp"

using namespace std;

// Calcula a unidade de n.
int unidade(int n)
{
    return n % 10;
}

examples {
    check_expect(unidade(152), 2); // 152 % 10
    check_expect(unidade(17), 7); // 17 % 10
}


// Calcula a dezena de n.
int dezena(int n)
{
    return (n / 10) % 10;
}

examples {
    check_expect(dezena(152), 5); // (152 / 10) % 10 -> 15 % 10 -> 5
    check_expect(dezena(423), 2); // (423 / 10) % 10 -> 42 % 10 -> 2
    check_expect(dezena(7), 0); // (7 / 10) % 10 -> 0 % 10 -> 0
}


// Calcula a centena de n.
int centena(int n)
{
    return (n / 100) % 10;
}

examples {
    check_expect(centena(152), 1); // (152 / 100) % 10 -> 1 % 10 -> 1
    check_expect(centena(4567), 5); // (4567 / 100) % 10 -> 45 % 10 -> 5
}

int main()
{
    run_tests();
}
