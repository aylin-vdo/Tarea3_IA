from collections import deque

class Nodo:
    def __init__(self, peso, ganancia, padre=None):
        self.peso = peso
        self.ganancia = ganancia
        self.padre = padre

def breadthfs(pesos, ganancias, peso_max):
    n = len(pesos)
    nodos = deque([Nodo(pesos[0], ganancias[0])])
    
    while nodos:
        nodo = nodos.popleft()
        if nodo.peso <= peso_max:
            camino = [nodo]
            while nodo.padre:
                camino.append(nodo.padre)
                nodo = nodo.padre
            camino.reverse()
            return [p.ganancia for p in camino], [p.peso for p in camino], sum(p.ganancia for p in camino)
        
        for i in range(1, n):
            nuevo_peso = nodo.peso + pesos[i]
            if nuevo_peso > peso_max:
                continue
            nueva_gan = nodo.ganancia + ganancias[i]
            nuevo_nodo = Nodo(nuevo_peso, nueva_gan, nodo)
            nodos.append(nuevo_nodo)
    
    return [], [], 0
