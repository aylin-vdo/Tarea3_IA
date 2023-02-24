from collections import deque

def bestfs(pesos, ganancias, peso_max):

    fila_p = []
    fila_g = []
    c = 0

    fila_p.append(0)
    fila_g.append(ganancias[0])

    for l in pesos:
        if (sum(i for i in fila_p) < peso_max):
            if (ganancias[(c+(c+1))]>ganancias[(c+(c+2))]) and (pesos[(c+(c+1))]<pesos[(c+(c+2))]) and (pesos[(c+(c+1))]+sum(i for i in fila_p))< peso_max:
                fila_p.append(pesos[(c+(c+1))])
                fila_g.append(ganancias[(c+(c+1))])
                c += (c+1)
                if ((c+(c+1)) >= len(ganancias)):
                    break
            if (ganancias[(c+(c+1))]<ganancias[(c+(c+2))]) and (pesos[(c+(c+1))]>pesos[(c+(c+2))] and (pesos[(c+(c+2))]+sum(i for i in fila_p))< peso_max):
                fila_p.append(pesos[(c+(c+2))])
                fila_g.append(ganancias[(c+(c+2))])
                c += (c+2)
                if ((c+(c+1)) >= len(ganancias)):
                    break
            else:
                if (ganancias[(c+(c+1))]/pesos[(c+(c+1))]) > (ganancias[(c+(c+2))]/pesos[(c+(c+2))]) and (pesos[(c+(c+1))]+sum(i for i in fila_p))< peso_max:
                    fila_p.append(pesos[(c+(c+1))])
                    fila_g.append(ganancias[(c+(c+1))])
                    c += (c+1)
                    if ((c+(c+1)) >= len(ganancias)):
                        break
                if (ganancias[(c+(c+1))]/pesos[(c+(c+1))]) < (ganancias[(c+(c+2))]/pesos[(c+(c+2))]) and (pesos[(c+(c+2))]+sum(i for i in fila_p))< peso_max:
                    fila_p.append(pesos[(c+(c+2))])
                    fila_g.append(ganancias[(c+(c+2))])
                    c += (c+2)
                    if ((c+(c+1)) >= len(ganancias)):
                        break
                else:
                    break
        else:
            return fila_g, fila_p, sum(j for j in fila_g)
        
    return fila_g, fila_p, sum(j for j in fila_g)
    
