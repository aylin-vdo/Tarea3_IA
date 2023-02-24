from algoritmos.BreadthFirstSearch import breadthfs
from algoritmos.BestFirstSearch import bestfs
from collections import namedtuple
from problemas.large_scale import *

ganancias = []
pesos = []

input = open('D:\Codigo\IA\T3\problemas\large_scale\knapPI_1_100_1000_1').read()
lineas = input.split('\n')
elementos = [item.split() for item in lineas]
lista_final = [item for l in elementos for item in l]

numeros = [eval(i) for i in lista_final]

cuenta = 0
for num in numeros:
    if (cuenta % 2) == 0:
        par = numeros[cuenta]
        ganancias.append(par)
        cuenta+=1
    else:
        otro = numeros[cuenta]
        pesos.append(otro)
        cuenta+=1


#profit weight
# kp_n_wmax donde n = num items, wmax = max capacidad

peso_max = 1000

ganancias1, pesos1, gan_total1 = breadthfs(pesos, ganancias, peso_max)
print("Ganancia max:", gan_total1)
print("Pesos:", pesos1)
print("Ganancias:", ganancias1)

ganancias2, pesos2, gan_total2 = bestfs(pesos, ganancias, peso_max)
print("Ganancia max:", gan_total2)
print("Pesos:", pesos2)
print("Ganancias:", ganancias2)