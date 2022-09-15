#include "bscpp.hpp"
#include <iostream>
#include <string>

using namespace std;

// Análise
//
// Converter uma quantidade de segundos em horas, minutos e segundos.
//
// Definição de tipos de dados
//
// Os segundos da entrada serão representados com números inteiros positivos

// Representa o tempo de duração de um evento.
// horas, minutos e segundos devem ser positivos.
// minutos e segundos devem ser menores que 60.
struct Tempo {
    int horas;
    int minutos;
    int segundos;
};

// Converte a quantidade segundos para o tempo equivalente em horas, minutos e
// segundos. A quantidade de segundos e minutos da resposta é sempre menor
// que 60.
Tempo segundos_para_tempo(int segundos)
{
    int h = segundos / 3600;
    // os segundos que não foram convertidos para hora
    int restantes = segundos % 3600;
    int m = restantes / 60;
    int s = restantes % 60;
    return Tempo {h, m, s};
}

examples
{
    check_expect(segundos_para_tempo(10), (Tempo {0, 0, 10}));
    check_expect(segundos_para_tempo(60), (Tempo {0, 1, 0}));
    // 160 / 60 -> 2
    // 160 % 60 -> 40
    check_expect(segundos_para_tempo(160), (Tempo {0, 2, 40}));
    check_expect(segundos_para_tempo(3600), (Tempo {1, 0, 0}));
    // 3760 / 3600 -> 1
    // 3760 % 3600 -> 160 segundos que sobraram
    // 160 / 60 -> 2
    // 160 % 60 -> 40
    check_expect(segundos_para_tempo(3760), (Tempo {1, 2, 40}));
}


// Converte t em uma mensagem para os usuários. Cada componente de t aparece
// com a sua unidade, mas se o valor do componente for 0, ele não aparece na
// mensagem. Os componentes são separados com " e " ou ", " respeitando as
// regras do Português. Se t for {0, 0, 0}, devolve "0 segundo(s)".
string tempo_para_string(Tempo t)
{
    string h = to_string(t.horas) + " hora(s)";
    string m = to_string(t.minutos) + " minuto(s)";
    string s = to_string(t.segundos) + " segundo(s)";
    string msg = "";

    if (t.horas > 0) {
        if (t.minutos > 0) {
            if (t.segundos > 0) {
                msg = h + ", " + m + " e " + s;
            } else {
                msg = h + " e " + m;
            }
        } else if (t.segundos > 0) {
            msg = h + " e " + s;
        } else {
            msg = h;
        }
    } else if (t.minutos > 0) {
        if (t.segundos > 0) {
            msg = m + " e " + s;
        } else {
            msg = m;
        }
    } else {
        msg = s;
    };

    return msg;
}

examples
{
    check_expect(tempo_para_string(Tempo {0, 0, 0}), "0 segundo(s)");
    check_expect(tempo_para_string(Tempo {0, 0, 1}), "1 segundo(s)");
    check_expect(tempo_para_string(Tempo {0, 0, 10}), "10 segundo(s)");
    check_expect(tempo_para_string(Tempo {0, 1, 20}), "1 minuto(s) e 20 segundo(s)");
    check_expect(tempo_para_string(Tempo {0, 2, 0}), "2 minuto(s)");
    check_expect(tempo_para_string(Tempo {1, 2, 1}), "1 hora(s), 2 minuto(s) e 1 segundo(s)");
    check_expect(tempo_para_string(Tempo {4, 0, 25}), "4 hora(s) e 25 segundo(s)");
    check_expect(tempo_para_string(Tempo {2, 4, 0}), "2 hora(s) e 4 minuto(s)");
    check_expect(tempo_para_string(Tempo {3, 0, 0}), "3 hora(s)");
}


string tempo_para_string2(Tempo t)
{
    // usado para separar cada componente de t
    string sep = "";
    string msg = "";
    if (t.segundos > 0) {
        sep = " e ";
        msg = to_string(t.segundos) + " segundo(s)";
    }

    if (t.minutos > 0) {
        msg = to_string(t.minutos) + " minuto(s)" + sep + msg;
        if (t.segundos > 0) {
            sep = ", ";
        } else {
            sep = " e ";
        }
    }

    if (t.horas > 0) {
        msg = to_string(t.horas) + " hora(s)" + sep + msg;
    }

    if (msg == "") {
        msg = "0 segundo(s)";
    }

    return msg;
}

examples
{
    check_expect(tempo_para_string(Tempo {0, 0, 0}), "0 segundo(s)");
    check_expect(tempo_para_string(Tempo {0, 0, 1}), "1 segundo(s)");
    check_expect(tempo_para_string(Tempo {0, 0, 10}), "10 segundo(s)");
    check_expect(tempo_para_string(Tempo {0, 1, 20}), "1 minuto(s) e 20 segundo(s)");
    check_expect(tempo_para_string(Tempo {0, 2, 0}), "2 minuto(s)");
    check_expect(tempo_para_string(Tempo {1, 2, 1}), "1 hora(s), 2 minuto(s) e 1 segundo(s)");
    check_expect(tempo_para_string(Tempo {4, 0, 25}), "4 hora(s) e 25 segundo(s)");
    check_expect(tempo_para_string(Tempo {2, 4, 0}), "2 hora(s) e 4 minuto(s)");
}

int main()
{
    run_tests();
}
