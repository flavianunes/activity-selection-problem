# coding: utf-8
# guloso.py

def selecao(atividades, n):
    
    compativeis = []
    atividades.sort(key=lambda x: x[2])
    i = 0
    compativeis.append(atividades[0][0])
    for m in range (1, n):
        index1, s1, f1 = atividades[m]
        index2, s2, f2 = atividades[i]
        if s1 >= f2:
            compativeis.append(index1)
            i = m
    print compativeis
    
