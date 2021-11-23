#include "bscpp.hpp"
#include <vector>

using namespace std;

// Produz true se os elementos de valores estão em ordem não decrescente, false
// caso contrário.
bool ordem_nao_decrescente(vector<int> valores)
{
    bool ordem = true;
    for (int i = 1; i < valores.size(); i = i + 1) {
        if (valores[i - 1] > valores[i]) {
            ordem = false;
        }
    }
    return ordem;
}

examples {
    check_expect(ordem_nao_decrescente({}), true);
    check_expect(ordem_nao_decrescente({3}), true);
    check_expect(ordem_nao_decrescente({1, 3}), true);
    check_expect(ordem_nao_decrescente({3, 1}), false);
    check_expect(ordem_nao_decrescente({1, 3, 3}), true);
    check_expect(ordem_nao_decrescente({3, 3, 3}), true);
    check_expect(ordem_nao_decrescente({3, 2, 3}), false);
    check_expect(ordem_nao_decrescente({3, 4, 2}), false);
    check_expect(ordem_nao_decrescente({1, 2, 3, 4, 5, 6}), true);
    check_expect(ordem_nao_decrescente({1, 2, 3, 2, 5, 6}), false);
}

int main()
{
    run_tests();
}
