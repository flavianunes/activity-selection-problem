# coding: utf-8
# backtracking.py

def selecao(atividades, n):
    
    compativeis = subproblema(atividades, [])
    print([indice for indice, s1, f1 in compativeis])
    
def subproblema(atividades, selecionadas):
    
    # Criando versão com atividade da lista de selecionadas
    sel = selecionadas[:]
    sel.append(atividades[0])
    
    # Se só houver uma atividade não é necessário recursão
    if len(atividades) == 1:
        return sel if isConjuntoValido(sel) else selecionadas
    
    # Teste com a atividade. Se a inclusão da atividade nos dá um conjunto inválido, descarta-se.
    x = subproblema(atividades[1:], sel) if isConjuntoValido(sel) else selecionadas 
    
    # Teste sem a atividade
    y = subproblema(atividades[1:], selecionadas)
    
    return x if len(x) >= len(y) else y
    

def isConjuntoValido(atividades):
    n = len(atividades)
    for i in range(n-1):
        index1, s1, f1 = atividades[i]
        for j in range(i+1, n):
            index2, s2, f2 = atividades[j]
            if s2 >= s1 and s2 < f1 or s1 >= s2 and s1 < f2:
                return False
    return True
