from algoritmos.BreadthFirstSearch import bfs
from algoritmos.Greedy import greedy
from collections import namedtuple
from problemas.large_scale import *

list1 = [0,0]
ganancias = []
pesos = []

input = open("knapPI_1_100_1000_1").read() ###------cambiar nombre de archivo por problema------###
lineas = input.split('\n')
elementos = lineas.split()

numeros = [eval(i) for i in elementos]

list1.append(numeros)

for i in list1:
    if i!=0 and i!=1:
        if (i % 2) == 0:
            ganancias.append(list1[i])
        else:
            pesos.append(list1[i])


#profit weight
# kp_n_wmax donde n = num items, wmax = max capacidad


###------cambiar peso maximo cada problema------###
peso_max = 1000

ganancias, pesos, gan_total = bfs(pesos, ganancias, peso_max)
print("Ganancia max:", gan_total)
print("Pesos:", pesos)
print("Ganancias:", ganancias)
ganancias, pesos, gan_total = greedy(pesos, ganancias, peso_max)
print("Maximum profit:", gan_total)
print("Pesos:", pesos)
print("Ganancias:", ganancias)