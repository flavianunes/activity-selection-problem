# coding: utf-8



def selecao(atividades, n):
    compativeis = []
    atividades.sort(key=lambda x: x[1])
    i = 0
    compativeis.append(atividades[0])
    for m in range (1, n):
        s1, f1 = atividades[m]
        s2, f2 = atividades[i]
        if s1 >= f2:
            compativeis.append(atividades[m])
            i = m
    print compativeis
       
#selecao([(1,2),(3,4), (1,1)], 3)
