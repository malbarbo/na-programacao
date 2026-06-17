# Demonstra a diferença entre a saída padrão e a saída de erro padrão.
#
# Para executar:
#
#     python3 saida.py
#     python3 saida.py 2> erro.txt

import sys

# mesmo que sys.stdout.write("tudo certo\n")
print("tudo certo")

# mesmo que sys.stderr.write("deu ruim\n")
print("deu ruim", file=sys.stderr)
