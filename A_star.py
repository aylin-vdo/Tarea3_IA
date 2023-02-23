import heapq

def astar(inicio, final, h, vecinos, costo):

    fila = [(h(inicio), inicio)]
    visitado = set()
    padres = {}
    costos = {inicio: 0}

    while fila:
        _, actual = heapq.heappop(fila)
        if actual == final:
            camino = [actual]
            while actual in padres:
                actual = padres[actual]
                camino.append(actual)
            camino.reverse()
            return camino

        visitado.add(actual)

        for vecino in vecinos(actual):
            costosnuevo = costos[actual] + costo(actual, vecino)
            if vecino in visitado and costosnuevo >= costos.get(vecino, float('inf')):
                continue

            if costosnuevo < costos.get(vecino, float('inf')):
                padres[vecino] = actual
                costos[vecino] = costosnuevo
                costo_2 = costosnuevo + h(vecino)
                heapq.heappush(fila, (costo_2, vecino))

    return None
