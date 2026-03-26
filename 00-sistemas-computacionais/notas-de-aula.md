---
# vim: set spell spelllang=pt_br:
title: Sistemas computacionais
# TODO: adicionar referências
---

# Introdução

## Introdução

O que é um computador? \pause

- No passado: uma pessoa que faz cálculos (computa) \pause

- Atualmente: uma máquina que pode ser programada para executar sequências de instruções automaticamente


## Introdução

O que é um software? \pause

Uma coleção de instruções que dizem o que um computador deve fazer.


## Introdução

O que é um sistema computacional? \pause

- Um conjunto completo de elementos que permite o uso do computador \pause

- Inclui hardware e software


## Exemplos

Propósito geral \pause

- Computadores pessoais
- _Smartphones_
- _Tablets_

\pause

Propósito específico

- Tocador de música
- Eletrodomésticos
- Automóveis
- Controle industrial


## Funcionamento básico

Como funciona um sistema computacional? \pause

- Entrada
- Processamento
- Saída



# Hardware


## Hardware

Vamos ver os componentes que realizam as funções de entrada, processamento e saída. \pause

Componentes \pause

- Dispositivos de entrada/saída
- Dispositivos de armazenamento
- Memória
- Processador

\pause

A interligação entre esses componentes é feita pela placa-mãe.

## Placa-mãe de um computador de mesa

![Fonte: \href{https://commons.wikimedia.org/wiki/File:MicroATX_Motherboard_with_AMD_Athlon_Processor_2_Digon3.jpg}{Wikipedia}](imagens/placa-mae.jpg){ width=7.5cm }

## Placa-mãe de um _smartphone_

![Fonte: \href{https://commons.wikimedia.org/wiki/File:Samsung_galaxy_s2_internal2.JPG}{Wikipedia}](imagens/placa-mae-smartphone.jpg){ width=7.5cm }

## Componentes / Dispositivos de entrada

Fornecem dados para serem processados. \pause Exemplos \pause

- Teclado
- Mouse
- Microfone
- Câmera
- Sensores
- Tela sensível ao toque


## Componentes / Dispositivos de saída

Apresentam ou transmitem dados recuperados do armazenamento e resultados do processamento. \pause Exemplos \pause

- Monitor
- Impressora
- Alto-falante
- Atuadores


## Componentes / Dispositivos de entrada e saída

Dispositivos híbridos \pause

- Adaptadores de rede
- Dispositivos de armazenamento


## Componentes / Dispositivos de armazenamento

Retêm dados para recuperação posterior. \pause Exemplos \pause

- Eletrônico \pause
    - ROMs (memória apenas para leitura)
    - SSD (disco de estado sólido) \pause
- Magnético \pause
    - Disquetes (discos flexíveis)
    - HDD (discos rígidos) \pause
- Óptico
    - CD
    - DVD


## Componentes de um HDD

![Fonte: \href{https://commons.wikimedia.org/wiki/File:HardDiskAnatomy.jpg}{Wikipedia}](imagens/hdd-anatomia.jpg){ width=10cm }


## Funcionamento de um HDD

Vídeos mostrando o funcionamento de um HDD

- \url{https://en.wikipedia.org/wiki/File:HardDisk1.ogv}

- \url{https://en.wikipedia.org/wiki/File:Harddrive-engineerguy.ogv} (Você pode escolher a legenda em português clicando em cc)


## HDD vs SSD

![Fonte: \url{https://ibexinc.wordpress.com/2010/02/13/the-death-of-the-disk/}](imagens/hdd-ssd.jpg){ width=10cm }


## HDD vs SSD

SSD

- Mais rápido
- Menor capacidade
- Mais caro

HDD

- Mais lento
- Maior capacidade
- Mais barato


## Componentes / Memória

Memória principal \pause

- Armazena informações para uso imediato
- Volátil (requer energia para manter os dados armazenados) \pause
- Mais rápida do que os dispositivos de armazenamento


## Componentes / Processador

<div class="columns">
<div class="column" width="50%">
Processador ou CPU (unidade central de processamento) \pause

- Registradores
    - Memória muito rápida que armazena os operandos e os resultados das operações
- Unidade lógica e aritmética (ULA)
    - Lê os operandos dos registradores
    - Executa operações
    - Grava o resultado nos registradores
- Unidade de controle
    - Coordena a leitura das instruções da memória e execução pela ULA

\pause
</div>
<div class="column" width="50%">
![Fonte: \href{https://commons.wikimedia.org/wiki/File:Von_Neumann_Architecture.svg}{Wikipedia}](imagens/arq.pdf){ width=6cm }
</div>
</div>


## Hierarquia de memória

Por que existem tantos tipos de memória? \pause

Porque cada uma tem características específicas de capacidade, velocidade e custo.


## Hierarquia de memória

![Fonte: \href{https://commons.wikimedia.org/wiki/File:ComputerMemoryHierarchy.svg}{Wikipedia}](imagens/hierarquia-memoria.pdf){ width=8cm }


## Conjunto de instruções

Cada processador executa um conjunto específico de instruções (descrito por uma arquitetura) \pause

- X86, AMD64 (computadores em geral)
- Arm, Aarch64 (dispositivos portáteis)
- Mips (roteadores)



# Software


## Licença

Uma questão importante sobre os softwares é a sua licença. \pause

O que é uma licença de software? \pause

É um documento que descreve um contrato entre o fornecedor do software e o usuário do software.


## Classificação por licença

De forma geral, os softwares podem ser classificados de acordo com a sua licença em

- Software proprietário

- Software livre


## Classificação por licença

Software proprietário

- Restringe de alguma maneira a execução, distribuição, modificação, etc.

- Suporte ao usuário geralmente fornecido pela empresa que vende/distribui o software. \pause

- Variantes: shareware, adware, etc. \pause


Exemplos \pause

- Photoshop

- Microsoft Office

- Google Chrome


## Classificação por licença

Software livre

- Permite a execução, redistribuição, modificação do código, etc.

- Algumas licenças requerem a redistribuição do código se ele for modificado.

- Suporte ao usuário geralmente fornecido pela comunidade de usuários e desenvolvedores \pause

Exemplos \pause

- Gimp

- Libreoffice

- Mozilla Firefox


## {.plain}

![Fonte: \href{https://en.wikipedia.org/wiki/File:Software_Categories_expanded.svg}{Wikipédia}](imagens/software-categories-expanded.pdf){width=9cm}


## Boot

Qual é o primeiro programa executado quando ligamos o computador? \pause

- Firmware (BIOS ou UEFI) \pause

E depois? \pause

- Sistema Operacional


## Sistema Operacional

Quais são os papéis do sistema operacional? \pause

- Gerenciar os recursos do sistema computacional \pause

- Prover serviços para outros softwares \pause

Alguns componentes \pause

- Kernel (gerência de processos, memória, entrada/saída, etc)

- Interface com o usuário (shell)


## {.plain}

![Fonte: \href{https://en.wikipedia.org/wiki/File:Operating_system_placement.svg}{Wikipédia}](imagens/camadas.pdf){height=7cm}


## Sistema Operacional

Exemplos de sistemas operacionais proprietários \pause

- Windows \pause

- macOS, iOS \pause

- Android, ChromeOS \pause


Exemplos de sistemas operacionais livres \pause

- Linux (Debian, Ubuntu, LineageOS, etc) \pause

- FreeBSD, OpenBSD, NetBSD \pause

- FreeDOS, ReactOS


## {.plain}

<div class="columns">
<div class="column" width="33%">
![Bill Gates (Windows)](imagens/gates.jpg){height=6cm}
</div>
<div class="column" width="33%">
![Steve Jobs (macOS/iOS)](imagens/jobs.jpg){height=6cm}
</div>
<div class="column" width="33%">
![Linus Torvalds (Linux)](imagens/linus.jpg){height=6cm}
</div>
</div>


## Shell

A interação entre o sistema operacional e o usuário final é feita através de um _Shell_ (lançador em dispositivos móveis).

Um _Shell_ pode oferecer uma interface gráfica ou interface textual. \pause

Quais as principais características de cada tipo de interface?


## Shell

<div class="columns">
<div class="column" width="48%">
Shell Gráfico \pause

- Geralmente utilizam a metáfora de área de trabalho \pause
- Facilidade de uso e aprendizado \pause
- Menos poderosos \pause
</div>
<div class="column" width="48%">
Shell Texto \pause

- Comandos descritos por texto
- Mais difíceis de aprender
- Mais ágeis
- Mais poderosos
</div>
</div>


## Shell Gráfico

![](imagens/gnome.jpg)


## Shell Texto

O shell textual é acessado através de um programa chamado **emulador de terminal** (ou simplesmente **terminal**). Exemplos: GNOME Terminal, Windows Terminal e Termux.

<div class="columns">
<div class="column" width="38%">
![](imagens/terminal.png){ width=4.5cm }
</div>
<div class="column" width="38%">
![](imagens/windows-terminal.png){ width=4.5cm }
</div>
<div class="column" width="20%">
![](imagens/termux-python.png){ width=2.2cm }
</div>
</div>


## Terminal

O termo "terminal" tem origem nos dispositivos físicos que eram usados para interagir com os computadores.

![Fonte: \href{https://commons.wikimedia.org/wiki/File:DEC_VT100_terminal.jpg}{Wikipédia}](imagens/vt100.png){width=6cm}


# Revisão

## Revisão

O que é um sistema computacional? \pause

- Um conjunto de hardware e software que permite o uso do computador. \pause

Qual é o funcionamento básico de um sistema computacional? \pause

- Entrada, processamento e saída. \pause

Quais são os principais componentes de hardware? \pause

- Dispositivos de entrada/saída, dispositivos de armazenamento, memória e processador.


## Revisão

Qual é a diferença entre memória e dispositivos de armazenamento? \pause

- A memória é volátil e mais rápida, usada para dados de uso imediato. Os dispositivos de armazenamento retêm dados de forma permanente, mas são mais lentos. \pause

Quais são as duas principais funções do sistema operacional? \pause

- Gerenciar os recursos do sistema computacional e prover serviços para outros softwares. \pause

Qual é a diferença entre software proprietário e software livre? \pause

- O software proprietário restringe a execução, distribuição ou modificação. O software livre permite a execução, redistribuição e modificação do código.

