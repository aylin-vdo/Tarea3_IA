
def greedy(pesos, ganancias, peso_max):
    n = len(pesos)
    ratios = [(ganancias[i] / pesos[i], i) for i in range(n)]
    ratios.sort(reverse=True)
    peso, ganancia = 0, 0
    for ratio, i in ratios:
        if peso + pesos[i] <= peso_max:
            peso += pesos[i]
            ganancia += ganancias[i]
    return [ganancia], [peso], ganancia
