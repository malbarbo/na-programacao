# Este programa calcula o máximo divisor comum entre dois números informados
# na linha de comando.
#
# Este programa não faz nenhuma validação da entrada!
#
# Para executar o programa
#
# python3 mdc.py 52 36

import sys

def main():
    # Entrada
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    # Processamento
    if a < b:
        a, b = b, a

    while b != 0:
        c = a - b
        a = b
        b = c
        if a < b:
            a, b = b, a

    # Saída
    print(a)

if __name__ == "__main__":
    main()
