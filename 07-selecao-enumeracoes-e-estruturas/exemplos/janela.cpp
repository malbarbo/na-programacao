#include "bscpp.hpp"

// Analise
//
// - Determinar se um clique aconteceu sobre uma janela
//
// Definição de tipos de dados

// Representa o espaço que uma janela ocupa em um ambiente gráfico.
//
// A coordenada (x, y) descreve a posição do canto superior esquerdo.
// A largura representa a quantidade de pixels à direita de (x, y)
// e a altura representa a quantidade de pixels abaixo de (x, y).
//
// Os valores da largura e altura devem ser maiores que zero.
struct Janela {
    int x;
    int y;
    int largura;
    int altura;
};

// Representa a posição de um clique no ambiente gráfico.
// Os valores de x e y devem ser maiores que 0 e menores do que as dimensões do
// ambiente.
struct Clique {
    int x;
    int y;
};

// Devolve true se o clique c está dentro do espaço da janela j, false contrário.
bool dentro_janela(Janela j, Clique c)
{
    // c.x está dentro do espaço da largura e c.y dentro do espaço da altura
    return j.x <= c.x && c.x < (j.x + j.largura) && j.y <= c.y && c.y < (j.y + j.altura);
}

examples
{
    //  x = 100, y = 100, largura = 300, altura = 200
    //
    //        p5
    //      +-----------+
    //  p4  | p1        | p2
    //      |           |
    //      +-----------+
    //        p3
    Janela janela = { 100, 100, 300, 200 };
    // p1 - dentro da janela
    check_expect(dentro_janela(janela, { 150, 150 }), true);
    // p2 - dentro do espaço da altura e depois do espaço da largura
    check_expect(dentro_janela(janela, { 600, 150 }), false);
    // p3 - depois do espaço da altura e dentro do espaço da largura
    check_expect(dentro_janela(janela, { 150, 300 }), false);
    // p4 - dentro do espaço da altura e antes do espaço da largura
    check_expect(dentro_janela(janela, { 150, 50 }), false);
    // p5 - antes do espaço da altura e dentro do espaço da largura
    check_expect(dentro_janela(janela, { 150, 50 }), false);
    // canto superior esquerdo
    check_expect(dentro_janela(janela, { 100, 100 }), true);
    // canto superior direito
    check_expect(dentro_janela(janela, { 399, 100 }), true);
    check_expect(dentro_janela(janela, { 400, 100 }), false);
    // canto inferior direito
    check_expect(dentro_janela(janela, { 399, 299 }), true);
    check_expect(dentro_janela(janela, { 400, 299 }), false);
    check_expect(dentro_janela(janela, { 399, 300 }), false);
    check_expect(dentro_janela(janela, { 400, 300 }), false);
    // canto inferior esquerdo
    check_expect(dentro_janela(janela, { 100, 299 }), true);
    check_expect(dentro_janela(janela, { 100, 300 }), false);
}

// Produz true se o espaço das janelas a e b se soprepoem, false caso contrário
bool janelas_soprepoem(Janela a, Janela b)
{
    return a.x < (b.x + b.largura) &&
           // borda direta de a vem antes da borda esquerda de b
           b.x < (a.x + a.largura) &&
           // borda direta de b vem antes da borda esquerda de a
           a.y < (b.y + b.altura) &&
           // borda superior de a vem antes da borda inferior de b
           b.y < (a.y + a.altura);
           // borda superior de b vem antes da borda inferior de a
}

examples
{
    // fixa (eixo y): a janela a vem antes da janela b
    // variável: posição da borda direita de a
    check_expect(janelas_soprepoem({  10, 20, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 210, 20, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 310, 20, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 410, 20, 100, 200 }, { 300, 400, 50, 100 }), false);
    // fixa: (eixo y) interseção da parte de baixo de a com a parte de cima de b
    // variável: posição da borda direita de a
    check_expect(janelas_soprepoem({  10, 250, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 210, 250, 100, 200 }, { 300, 400, 50, 100 }), true);
    check_expect(janelas_soprepoem({ 310, 250, 100, 200 }, { 300, 400, 50, 100 }), true);
    check_expect(janelas_soprepoem({ 410, 250, 100, 200 }, { 300, 400, 50, 100 }), false);
    // fixa: (eixo y) interseção da parte de cima de a com a parte de baixo de b
    // variável: posição da borda direita de a
    check_expect(janelas_soprepoem({  10, 450, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 210, 450, 100, 200 }, { 300, 400, 50, 100 }), true);
    check_expect(janelas_soprepoem({ 310, 450, 100, 200 }, { 300, 400, 50, 100 }), true);
    check_expect(janelas_soprepoem({ 410, 450, 100, 200 }, { 300, 400, 50, 100 }), false);
    // fixa: (eixo y) a janela a vem depois da janela b
    // variável: posição da borda direita de a
    check_expect(janelas_soprepoem({  10, 550, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 210, 550, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 310, 550, 100, 200 }, { 300, 400, 50, 100 }), false);
    check_expect(janelas_soprepoem({ 410, 550, 100, 200 }, { 300, 400, 50, 100 }), false);
}

int main()
{
    run_tests();
}
