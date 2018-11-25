# coding: utf-8
# dinamico.py

# criando a tabela atividades x tempo 
# que armazena a quantidade de atividades na soluçao
tabela_quantidades = []
compativeis = []
       

def selecao(atividades, n):
    #selecionando o tempo maximo total das atividades
    tempo_maximo = max(atividades,key=lambda item:item[2])[2]
    atividades.sort(key=lambda x: x[2])

    for y in range(n+1):
        linha = []
        for x in range(tempo_maximo+1):
            linha.append(-1)
        tabela_quantidades.append(linha)
        
    resolve(0, 0, atividades) 
    print resultado(0, 0, atividades)
        
def resolve(indice, tempo_final, atv):
    
    n = len(atv)
    
    if indice == n:
        return 0
    
    v1 = 0
    v2 = 0
    
    
    if tabela_quantidades[indice][tempo_final] != -1:        
        return tabela_quantidades[indice][tempo_final]
    
    # se eu nao pegar a tarefa
    v1 = resolve(indice+1, tempo_final, atv)
    
    # se eu pegar a tarefa
    if atv[indice][1] >= tempo_final:
        v2 = resolve(indice+1, atv[indice][2], atv) +1
    
        
    tabela_quantidades[indice][tempo_final] = max(v1,v2)
    
    return tabela_quantidades[indice][tempo_final]
    
def resultado(indice, tempo_final, atv):
    n = len(atv) - 1
    if indice == n:
        #ultima atividade
        if tabela_quantidades[indice][tempo_final] == 1:
            compativeis.append(atv[indice][0])
        return compativeis
    
    if tabela_quantidades[indice][tempo_final] == 0:
        #nao tem mais tarefa pra pegar
        return compativeis
    
    if tabela_quantidades[indice][tempo_final] == tabela_quantidades[indice+1][tempo_final]:
        #nao peguei a tarefa (olha pra baixo)
        resultado(indice+1, tempo_final, atv)
        return compativeis
    else:
        compativeis.append(atv[indice][0])
        #peguei a tarefa (olha na diagonal)
        resultado(indice+1, atv[indice][2], atv)
        return compativeis
