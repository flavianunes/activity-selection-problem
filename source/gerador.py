# coding: utf-8
from random import randint

# Aleatorio
def random(n):
    for i in range(0, 10):
        file = open('../instancias/random'+ str(n) + '-' + str(i+1) + '.txt', "w")
        file.write(str(n) + '\n')
        for j in range (0, n):
            s = randint(0, 20 * n)
            f = randint(s + 1, 21 * n) #garantir que o tempo final vem depois do inicial
            file.write(str(s) + ' ' + str(f) + '\n')
        file.close()

# Otimista 
def optimistic(n, c):
    s = 0
    f = c
    for i in range(0, 10):
        file = open('../instancias/optimistic'+ str(n) + '-' + str(i+1) +'.txt', "w")
        file.write(str(n) + '\n')
        for j in range (0, n):
            file.write(str(s) + ' ' + str(f) + '\n')
            s = f + 1
            f += c
        file.close()

# Pessimista 
def pessimist(n, c):
    for i in range(0, 10):
        file = open('../instancias/pessimist'+ str(n) + '-' + str(i+1) +'.txt', "w")
        file.write(str(n) + '\n')
        for j in range (0, n):
            s = randint(0, c)
            f = randint(c, 20 * n) #constante deve ser menor que 20n, se nao -> erro
            file.write(str(s) + ' ' + str(f) + '\n')
        file.close()
    

random(10)
random(15)
random(20)

optimistic(10, 3)
optimistic(15, 3)
optimistic(20, 3)

pessimist(10, 5)
pessimist(15, 10)
pessimist(20, 200)
