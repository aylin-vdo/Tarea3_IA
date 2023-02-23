from collections import deque

class Node:
    def __init__(self, peso, ganancia, padre=None):
        self.peso = peso
        self.ganancia = ganancia
        self.padre = padre

def bfs(pesos, ganancias, max_peso):
    n = len(pesos)
    nodes = deque([Node(pesos[0], ganancias[0])])
    
    while nodes:
        node = nodes.popleft()
        if node.peso <= max_peso:
            camino = [node]
            while node.padre:
                camino.append(node.padre)
                node = node.padre
            camino.reverse()
            return [p.ganancia for p in camino], [p.peso for p in camino], sum(p.ganancia for p in camino)
        
        for i in range(1, n):
            new_peso = node.peso + pesos[i]
            if new_peso > max_peso:
                continue
            new_ganancia = node.ganancia + ganancias[i]
            new_node = Node(new_peso, new_ganancia, node)
            nodes.append(new_node)
    
    return [], [], 0

