from algoritmos.BreadthFirstSearch import bfs
from algoritmos.Greedy import greedy
from collections import namedtuple

#profit weight
# kp_n_wmax donde n = num items, wmax = max capacidad

pesos = [2, 3, 4, 5]
ganancias = [3, 7, 2, 9]
peso_max = 5
ganancias, pesos, gan_total = bfs(pesos, ganancias, peso_max)
print("Ganancia max:", gan_total)
print("Pesos:", pesos)
print("Ganancias:", ganancias)
ganancias, pesos, gan_total = greedy(pesos, ganancias, peso_max)
print("Maximum profit:", gan_total)
print("Pesos:", pesos)
print("Ganancias:", ganancias)

