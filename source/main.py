# coding: utf-8
# main.py

import sys
import guloso
import dinamico
import backtracking
import timeit

if len(sys.argv) < 3:
    print ("Por favor, confira se está fornecendo o nome do arquivo de instância e o método como parâmetros")
    print ("Métodos: guloso, dinamico e backt")
    sys.exit()
    
# Coletando parâmetros
nome_arquivo = sys.argv[1]
metodo = sys.argv[2]

# Criando estrutura de dados
referencia_arquivo = open(nome_arquivo, 'r')
linha = referencia_arquivo.readline()
valores = linha.split()

n = int(valores[0])
atividades = []

index = 1

for linha in referencia_arquivo:
    valores = linha.split()
    atividades.append((index, int(valores[0]), int(valores[1])))
    index = index + 1

# Garantindo que a instância tem o tamanho correto
assert n == len(atividades)

# Execução do método
if metodo == 'guloso':
    start = timeit.default_timer()
    guloso.selecao(atividades, n)
    stop = timeit.default_timer()
    print('Tempo: ' + str(stop - start) + ' segundos')

elif metodo == 'dinamico':
    start = timeit.default_timer()
    dinamico.selecao(atividades, n)
    stop = timeit.default_timer()
    print('Tempo: ' + str(stop - start) + ' segundos')
    
elif metodo == 'backt':
    start = timeit.default_timer()
    backtracking.selecao(atividades, n)
    stop = timeit.default_timer()
    print('Tempo: ' + str(stop - start) + ' segundos')
    
else:
    print("Método não reconhecido")
