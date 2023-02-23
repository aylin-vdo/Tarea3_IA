from collections import deque

def bfs(grafo, inicio):
    fila = deque([inicio])
    visitado = set([inicio])

    while fila:
        nodo = fila.popleft()
        for vecino in grafo[nodo]:
            if vecino not in visitado:
                visitado.add(vecino)
                fila.append(vecino)
    return fila
