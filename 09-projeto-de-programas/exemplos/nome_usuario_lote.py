def nome_usuario(nome: str) -> str:
    '''
    Cria um nome de usuário a partir de *nome* da seguinte forma:
    - divide *nome* em partes (separadas por espaço)
    - junta a primeira letra de cada parte (exceto a última) e a última parte toda
    O resultado é truncado para 8 caractes em minúsculo.
    >>> nome_usuario('Maria')
    'maria'
    >>> nome_usuario('José Paulo da Silveira')
    'jpdsilve'
    >>> nome_usuario('Qin U Em Ca Oi Iter Sol An Do')
    'quecoisa'
    '''
    partes = nome.split()
    usuario = ''
    for i in range(len(partes) - 1):
        usuario = usuario + partes[i][:1]
    # tem pelo menos uma parte
    if len(partes) >= 1:
        usuario = usuario + partes[len(partes) - 1]
    return usuario[:8].lower()
