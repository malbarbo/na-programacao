#include "bscpp.hpp"
#include <vector>

using namespace std;

// Análise
//
// - Determinar o retangulo delimitador de altura e largura mínima que cobre um conjunto de pontos
//
// Definição dos tipos de dados

// Um ponto no plano cartesiano.
struct Ponto {
    int x;
    int y;
};

// Um retangulo delimitador.
struct Retangulo {
    int largura;
    int altura;
};

// Determina o retangulo delimitador de altura e largura mínimas que cobre os
// pontos do arranjo pontos.
// Se existe 1 ou menos pontos, o rentagulo terá altura e largura 0.
Retangulo retangulo_delimitador(vector<Ponto> pontos)
{
    Retangulo r;
    if (pontos.size() == 0) {
        r = {0, 0};
    } else {
        int menor_x = pontos[0].x;
        int maior_x = pontos[0].x;
        int menor_y = pontos[0].y;
        int maior_y = pontos[0].y;
        for (Ponto p : pontos) {
            if (p.x < menor_x) {
                menor_x = p.x;
            } else if (p.x > maior_x) {
                maior_x = p.x;
            }
            if (p.y < menor_y) {
                menor_y = p.y;
            } else if (p.y > maior_y) {
                maior_y = p.y;
            }
        }
        r = {maior_x - menor_x, maior_y - menor_y};
    }
    return r;
}
//               |
//               |        p5
//      p1       |
//               |    p4
//               | p3
// --------------+-------------
//           p2  |
//               |   p6
//               |
examples
{
    Ponto p1 = {-10, 5};
    Ponto p2 = {-3, -1};
    Ponto p3 = {1, 1};
    Ponto p4 = {4, 3};
    Ponto p5 = {9, 8};
    Ponto p6 = {2, -3};
    check_expect(retangulo_delimitador({}), (Retangulo {0, 0}));
    check_expect(retangulo_delimitador({p1}), (Retangulo {0, 0}));
    check_expect(retangulo_delimitador({p2, p3}), (Retangulo {4, 2}));
    check_expect(retangulo_delimitador({p2, p3, p6}), (Retangulo {5, 4}));
    check_expect(retangulo_delimitador({p2, p3, p1, p6, p4, p5}), (Retangulo {19, 11}));
}

int main()
{
    run_tests();
}
