from dataclasses import dataclass

# Análise
#
# - Determinar o candidado melhor classificado entre dois candidados
# - A classificação é feita pelos pontos (0 a 100), mais pontos fica
#   na frente, seguido pelo menor número de inscrição (que é único).

# Definição de tipos de dados
#
# - Vamos representar um candidado com um estruda com nome, inscrição e pontos.
# - Vamos assumir que a inscrição é um número natural.


@dataclass
class Candidado:
    '''
    Representa o candidado e o seu desempenho no concurso.
    '''
    # positivo
    inscricao: int
    nome: str
    # natutal de 0 a 100
    pontos: int


def melhor_classificado(a: Candidado, b: Candidado) -> Candidado:
    '''
    Determina qual dos candidos, *a* ou *b*, ficou melhor classificado.
    A classificação é determinada pelo maior número de pontos, e se houver
    empate, pelo menor número de inscrição.

    Exemplos
    >>> # a melhor classificado
    >>> melhor_classificado(Candidado(4, 'João', 80), Candidado(5, 'Pedro', 70))
    Candidado(inscricao=4, nome='João', pontos=80)
    >>> melhor_classificado(Candidado(4, 'João', 70), Candidado(5, 'Pedro', 70))
    Candidado(inscricao=4, nome='João', pontos=70)
    >>> # b melhor classificado
    >>> melhor_classificado(Candidado(4, 'João', 70), Candidado(5, 'Pedro', 80))
    Candidado(inscricao=5, nome='Pedro', pontos=80)
    >>> melhor_classificado(Candidado(4, 'João', 70), Candidado(3, 'Pedro', 70))
    Candidado(inscricao=3, nome='Pedro', pontos=70)
    '''
    if a.pontos > b.pontos or \
            (a.pontos == b.pontos and a.inscricao < b.inscricao):
        melhor = a
    else:
        melhor = b
    return melhor
