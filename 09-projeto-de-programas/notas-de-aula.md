---
# vim: set spell spelllang=pt_br:
title: Projeto de programas
---

# Introdução

Nós estamos trabalhando a bastante tempo o projeto de tipos de dados e funções isoladas (ou em pequenos conjuntos). \pause

Agora vamos ver o projeto de programas, isto é, coleções de tipos e funções para resolver um problema maior. \pause

Antes de ver as técnicas de projeto de programas, vamos ver os tipos de programas e como fazer entrada e saída de dados.


# Composição de um programa

Um programa é composto de: \pause

- **Constantes**: nomeia valores fixos \pause
- **Tipos de dados**: representam as informações \pause
- **Funções**: fazem o processamento e a entrada e saída de dados \pause
- **Função principal**: primeira função chamada no programa, coordena a chamada das outras funções


# Funcionamento de um programa

As atividades realizadas por um programa pode ser divididas em: \pause

- **Entrada**: obtém os dados para processamento \pause
- **Processamento**: computa as saídas a partir das entradas \pause
- **Saída**: exibe as saídas (resultados) e outra informações \pause

O processamento é o "miolo" do programa, feito por funções. \pause

A entrada e a saída são a "casca" que conecta o programa ao mundo externo.


# Tipos de programas

Os programas se distinguem pela forma como **obtêm a entrada** e **interagem** com o mundo: \pause

- **Em lote** (não interativo): recebe todos os dados de uma vez, processa e produz a saída \pause
- **Interativo**: interage com o usuário durante a execução \pause

Vamos ver um exemplo simples escrito escrito dessas duas formas.


# Exemplo - nome de usuário

Projete um programa que gere nomes de usuário a partir de nomes completos. Cada nome de usuário é gerado da seguinte forma: a primeira letra de cada "parte" do nome, mais todas as letras da última parte. O nome do usuário deve ter no máximo 8 caracteres e todos devem ser minúsculos. \pause

Exemplo: "Marco Aurélio Lopes Barbosa" -> malbarbo. \pause

Como começamos? \pause

Temos duas opções: \pause

- Primeiro o projeto da função de processamento e depois a entrada e saída; ou \pause
- Primeiro a entrada e saída e depois o projeto da função de processamento

<!--

# Exemplo - nome de usuário

```
def nome_usuario(nome: str) -> str:
```


# Exemplo - estatísticas de temperaturas

Queremos um programa que receba uma lista de temperaturas e calcule a temperatura **mínima**, a **máxima** e a **média**. \pause

Seguindo o projeto de programas, primeiro projetamos as funções de processamento e depois escrevemos o `main` que as conecta à entrada e à saída.


# Estatísticas - funções de processamento

<div class="columns">
<div class="column" width="50%">
\scriptsize

```python
def minima(temperaturas: list[float]) -> float:
    """
    Devolve a menor temperatura de
    *temperaturas* (não vazia).

    >>> minima([20.5])
    20.5
    >>> minima([20.5, 19.0, 22.0])
    19.0
    """
    menor: float = temperaturas[0]
    for t in temperaturas:
        if t < menor:
            menor = t
    return menor
```
</div>
<div class="column" width="50%">
\scriptsize

```python
def media(temperaturas: list[float]) -> float:
    """
    Devolve a média de
    *temperaturas* (não vazia).

    >>> media([20.0])
    20.0
    >>> media([20.5, 19.0, 22.0])
    20.5
    """
    soma: float = 0.0
    for t in temperaturas:
        soma += t
    return soma / len(temperaturas)
```
</div>
</div>

\pause
\small

A função `maxima` é análoga à `minima` (troca `<`{.python} por `>`{.python}). Nada de novo: são funções projetadas com o processo de sempre.


# Estatísticas - o programa

<div class="columns">
<div class="column" width="55%">
\scriptsize

```python
import sys


def main() -> None:
    # Entrada
    temperaturas: list[float] = []
    for argumento in sys.argv[1:]:
        temperaturas.append(float(argumento))

    # Processamento e saída
    print("Mínima:", minima(temperaturas))
    print("Máxima:", maxima(temperaturas))
    print("Média:", media(temperaturas))


if __name__ == "__main__":
    main()
```
</div>
<div class="column" width="45%">
\small

`sys.argv` é a lista de argumentos da linha de comando. \pause

`sys.argv[0]` é o nome do programa; os valores começam em `sys.argv[1]`. \pause

Cada argumento é uma `str`; convertemos para `float`{.python}.

</div>
</div>


# O ponto de entrada

Por que `if __name__ == "__main__":`? \pause

Quando o Spython executa os doctests (botão **Run** ou `spython check`), ele **carrega as definições** do arquivo. \pause

Sem o guard, o `main()` seria executado nesse momento — mas o `main` lê a entrada do programa, o que não faz sentido durante os testes. \pause

O guard garante que o `main` só é executado quando rodamos o arquivo **como um programa**, e não quando ele é carregado para testar as funções.


# Estatísticas - executando

Passamos as temperaturas na linha de comando:

\medskip

```
$ python3 estatisticas.py 20.5 19.0 22.0 25.5
Mínima: 19.0
Máxima: 25.5
Média: 21.75
```

\pause
\medskip

No Spython, os valores são informados da mesma forma na linha de comando.


# E se forem muitos valores?

Digitar dezenas de temperaturas na linha de comando é trabalhoso e sujeito a erros. \pause

Melhor guardar os dados em um **arquivo** e pedir que o programa leia de lá. \pause

Agora a linha de comando informa o **nome do arquivo**, não mais os valores.


# Estatísticas - lendo de um arquivo

<div class="columns">
<div class="column" width="55%">
\scriptsize

```python
def main() -> None:
    # Entrada
    temperaturas: list[float] = []
    arquivo = open(sys.argv[1])
    for linha in arquivo:
        temperaturas.append(float(linha))
    arquivo.close()

    # Processamento e saída
    print("Mínima:", minima(temperaturas))
    print("Máxima:", maxima(temperaturas))
    print("Média:", media(temperaturas))
```
</div>
<div class="column" width="45%">
\small

Só a **entrada** muda; o processamento e a saída são os mesmos. \pause

`open(nome)` abre o arquivo; iterar sobre ele percorre as **linhas** (cada uma uma `str`). \pause

`close()` fecha o arquivo ao final.

</div>
</div>


# Estatísticas - executando (arquivo)

<div class="columns">
<div class="column" width="40%">

Arquivo `temperaturas.txt` (uma por linha):

\small

```
18.0
19.0
20.0
21.0
22.0
23.0
24.0
```
</div>
<div class="column" width="60%">
\pause

```
$ python3 estatisticas_arquivo.py \
      temperaturas.txt
Mínima: 18.0
Máxima: 24.0
Média: 21.0
```
</div>
</div>


# O miolo é o mesmo

Repare: as funções `minima`, `maxima` e `media` — o **processamento** — não mudaram entre as duas versões. \pause

Mudou apenas a forma de **obter a entrada** (a casca). \pause

Esse é o coração do projeto de programas: \pause

- o processamento é feito por **funções**, que projetamos e testamos com doctests; \pause
- o programa as **conecta** a uma fonte de entrada e a uma saída.


# Programas interativos

Um programa **interativo** dialoga com o usuário **durante a execução**, lendo dados com `input()` e respondendo com `print()`, em um laço, até o usuário encerrar. \pause


# Programas reativos

Um programa **reativo** (orientado a eventos) fica **em execução**, reagindo a um fluxo de eventos, e não termina sozinho. \pause

Exemplos: jogos, animações e interfaces gráficas (o modelo `World` visto no material de imagens e animações) e também **serviços/servidores**. \pause

Um serviço é **reativo**, não em lote: ele não recebe tudo de uma vez, espera e responde requisições ao longo do tempo.

-->
