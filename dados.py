# acessou_home, acessou_como_funciona,
# acessou_contato, comprou

# X são os dados que voce tem e y os dados que voce deseja prever

import csv

def carregar_accessos():
    X = []
    Y = []

    arquivo = open('acesso_pagina.csv', 'r')
    leitor = csv.reader(arquivo)
    next(leitor)

    for home, como_funciona, contato, comprou in leitor:
        X.append([int(home), int(como_funciona),
            int(contato)])
        
        Y.append(int(comprou))
    return X, Y

def carregar_buscas():
    X = []
    Y = []

    arquivo = open('buscas.csv', 'r')
    leitor = csv.reader(arquivo)
    next(leitor)

    for home, busca, logado, comprou in leitor:
        X.append([int(home), busca,
            int(logado)])
        
        Y.append(int(comprou))
    return X, Y

