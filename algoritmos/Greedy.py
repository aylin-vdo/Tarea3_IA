
def greedy(weights, profits, max_weight):
    n = len(weights)
    ratios = [(profits[i] / weights[i], i) for i in range(n)]
    ratios.sort(reverse=True)
    weight, profit = 0, 0
    for ratio, i in ratios:
        if weight + weights[i] <= max_weight:
            weight += weights[i]
            profit += profits[i]
    return [profit], [weight], profit
