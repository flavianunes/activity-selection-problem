# coding: utf-8

compativeis = []

def selecao(atividades, n):
    atividades.sort(key=lambda x: x[1])
    i = 1
    compativeis.append(atividades[0])
    for m in range (2, n):
        s1, f1 = atividades[m]
        s2, f2 = atividades[i]
        if s1 >= f2:
            compativeis.append(atividades[m])
    print compativeis
       
