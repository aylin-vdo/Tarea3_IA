from algoritmos.BreadthFirstSearch import bfs
from algoritmos.Greedy import greedy
from collections import namedtuple

#profit weight
# kp_n_wmax donde n = num items, wmax = max capacidad

weights = [2, 3, 4, 5]
profits = [3, 7, 2, 9]
max_weight = 5
profits, weights, total_profit = bfs(weights, profits, max_weight)
print("Maximum profit:", total_profit)
print("Weights:", weights)
print("Profits:", profits)
profits, weights, total_profit = greedy(weights, profits, max_weight)
print("Maximum profit:", total_profit)
print("Weights:", weights)
print("Profits:", profits)

