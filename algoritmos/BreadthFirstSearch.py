from collections import deque



def breadthfs(pesos, ganancias, peso_max):

    fila_p = []
    fila_g = []

    visitado_p = []
    no_visitado_p = deque(pesos)
    visitado_g = []
    no_visitado_g = deque(pesos)

    pos = 1

    fila_p.append(0)
    fila_g.append(ganancias[0])

    for l in pesos:
        if sum(i for i in fila_p) < peso_max:
            if sum(i for i in fila_p) + pesos[pos+1] >= peso_max:
                return fila_g, fila_p, sum(j for j in fila_g)
            else:
                fila_p.append(pesos[pos])
            fila_g.append(ganancias[pos])
            visitado_p.append(pesos[pos])
            visitado_g.append(ganancias[pos])
            no_visitado_p.popleft()
            no_visitado_g.popleft()
            pos += 1 
        else:
            #print(fila_p)
            return fila_g, fila_p, sum(j for j in fila_g)
        


