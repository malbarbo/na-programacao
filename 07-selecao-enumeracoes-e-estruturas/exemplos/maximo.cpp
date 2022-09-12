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

// Encontra o valor máximo entre a, b e c.
int maximo3v1(int a, int b, int c) {
    int max;
    if (a >= b && a >= c) {
        max = a;
    } else if (b >= a && b >= c) {
        max = b;
    } else {
        max = c;
    }
    return max;
}

examples
{
    // a é máximo
    check_expect(maximo3v1(20, 10, 12), 20);
    check_expect(maximo3v1(20, 12, 10), 20);
    check_expect(maximo3v1(20, 12, 12), 20);
    check_expect(maximo3v1(20, 20, 20), 20);
    // b é máximo
    check_expect(maximo3v1(5, 12, 3), 12);
    check_expect(maximo3v1(3, 12, 5), 12);
    check_expect(maximo3v1(5, 12, 5), 12);
    // c é máximo
    check_expect(maximo3v1(4, 8, 18), 18);
    check_expect(maximo3v1(8, 4, 18), 18);
    check_expect(maximo3v1(8, 8, 18), 18);
}

int maximo3v2(int a, int b, int c) {
    int max;
    if (a >= b) {
        if (a >= c) {
            max = a;
        } else {
            max = c;
        }
    } else {
        if (b >= c) {
            max = b;
        } else {
            max = c;
        }
    }
    return max;
}

examples
{
    // a é máximo
    check_expect(maximo3v2(20, 10, 12), 20);
    check_expect(maximo3v2(20, 12, 10), 20);
    check_expect(maximo3v2(20, 12, 12), 20);
    check_expect(maximo3v2(20, 20, 20), 20);
    // b é máximo
    check_expect(maximo3v2(5, 12, 3), 12);
    check_expect(maximo3v2(3, 12, 5), 12);
    check_expect(maximo3v2(5, 12, 5), 12);
    // c é máximo
    check_expect(maximo3v2(4, 8, 18), 18);
    check_expect(maximo3v2(8, 4, 18), 18);
    check_expect(maximo3v2(8, 8, 18), 18);
}

// Encontra o máximo entre a, b e c.
int maximo3v3(int a, int b, int c)
{
    return maximo(maximo(a, b), c);
}

examples
{
    // a é máximo
    check_expect(maximo3v3(20, 10, 12), 20);
    check_expect(maximo3v3(20, 12, 10), 20);
    check_expect(maximo3v3(20, 12, 12), 20);
    check_expect(maximo3v3(20, 20, 20), 20);
    // b é máximo
    check_expect(maximo3v3(5, 12, 3), 12);
    check_expect(maximo3v3(3, 12, 5), 12);
    check_expect(maximo3v3(5, 12, 5), 12);
    // c é máximo
    check_expect(maximo3v3(4, 8, 18), 18);
    check_expect(maximo3v3(8, 4, 18), 18);
    check_expect(maximo3v3(8, 8, 18), 18);
}

int main()
{
    run_tests();
}
