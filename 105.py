def notas(*nota, sit= True):
    """
    Faz a analize de varias notas e apresenta a quantidade de notas adicionadas,
    a maior nota, a menor nota e a media das notas.
    Tambem tem um parametro opcional para ver a situaçao da pessoa.

    :Param notas: notas para os calculos 
    :Param sit: Define se vai ou nao ser mostrado a situaçao do aluno. 

    """
    dicionario = {}
    tabela = list(nota)  
    dicionario['quantidade'] = len(tabela)
    dicionario['maior'] = max(tabela)
    dicionario['menor'] = min(tabela)
    dicionario['media'] = sum(tabela) / dicionario['quantidade']
    if sit:
        if dicionario['media'] >= 7:
            dicionario['situaçao'] =  'boa'
        else:
            dicionario['situaçao'] =  'ruim'
    return dicionario
print(notas(1, 2, 7.73, 88, sit = False))
