import heapq

class Node:
    def __init__(self, peso, ganancia, padre=None, camino_costo=0, heurist_costo=0):
        self.peso = peso
        self.ganancia = ganancia
        self.padre = padre
        self.camino_costo = camino_costo
        self.heurist_costo = heurist_costo
    
    def __lt__(self, otro):
        return self.camino_costo + self.heurist_costo < otro.camino_costo + otro.heurist_costo

def a_star(pesos, ganancias, max_peso):
    n = len(pesos)
    nodes = [Node(pesos[0], ganancias[0], camino_costo=0, heurist_costo=ganancias[0]/pesos[0])]
    heapq.heapify(nodes)
    
    while nodes:
        node = heapq.heappop(nodes)
        if node.peso <= max_peso:
            path = [node]
            while node.padre:
                path.append(node.padre)
                node = node.padre
            path.reverse()
            return [p.ganancia for p in path], [p.peso for p in path], sum(p.ganancia for p in path)
        
        for i in range(1, n):
            new_peso = node.peso + pesos[i]
            if new_peso > max_peso:
                continue
            new_ganancia = node.ganancia + ganancias[i]
            new_node = Node(new_peso, new_ganancia, node, camino_costo=node.camino_costo+1, heurist_costo=new_ganancia/new_peso)
            heapq.heappush(nodes, new_node)
    
    return [], [], 0
