from T3.BFS import bfs
from T3.A_star import a_star


# BFS prueba
peso = [2, 3, 4, 5]
ganancia = [3, 7, 2, 9]
peso_max = 5
ganancia, peso, ganancia_total = bfs(peso, ganancia, peso_max)
print("ganancia maxima:", ganancia_total)
print("peso:", peso)
print("ganancia:", ganancia)

# A* prueba

peso = [2, 3, 4, 5]
ganancia = [3, 7, 2, 9]
peso_max = 5
ganancia, peso, ganancia_total = a_star(peso, ganancia, peso_max)
print("ganancia maxima:", ganancia_total)
print("peso:", peso)
print("ganancia:", ganancia)
