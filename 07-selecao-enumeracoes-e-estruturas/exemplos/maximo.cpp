#include "bscpp.hpp"

// Encontra o valor máximo entre a e b.
int maximo(int a, int b)
{
    int max;
    if (a >= b) {
        max = a;
    } else {
        max = b;
    }
    return max;
}

examples
{
    check_expect(maximo(20, 10), 20);
    check_expect(maximo(5, 10), 10);
    check_expect(maximo(5, 5), 5);
}

// Encontra o máximo entre a, b e c.
int maximo3(int a, int b, int c)
{
    return maximo(maximo(a, b), c);
}

examples
{
    // máximo é o a
    check_expect(maximo3(4, 3, 1), 4);
    check_expect(maximo3(4, 1, 3), 4);
    check_expect(maximo3(4, 4, 3), 4);
    check_expect(maximo3(-1, -2, -1), -1);
    // máximo é o b
    check_expect(maximo3(3, 4, 1), 4);
    check_expect(maximo3(1, 4, 3), 4);
    check_expect(maximo3(1, 8, 8), 8);
    // máximo é o c
    check_expect(maximo3(3, 1, 4), 4);
    check_expect(maximo3(1, 3, 4), 4);
    check_expect(maximo3(-2, -2, -2), -2);
}

int main()
{
    run_tests();
}
