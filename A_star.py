import heapq

class Node:
    def __init__(self, weight, profit, parent=None, path_cost=0, heuristic_cost=0):
        self.weight = weight
        self.profit = profit
        self.parent = parent
        self.path_cost = path_cost
        self.heuristic_cost = heuristic_cost
    
    def __lt__(self, other):
        return self.path_cost + self.heuristic_cost < other.path_cost + other.heuristic_cost

def a_star(weights, profits, max_weight):
    n = len(weights)
    nodes = [Node(weights[0], profits[0], path_cost=0, heuristic_cost=profits[0]/weights[0])]
    heapq.heapify(nodes)
    
    while nodes:
        node = heapq.heappop(nodes)
        if node.weight <= max_weight:
            path = [node]
            while node.parent:
                path.append(node.parent)
                node = node.parent
            path.reverse()
            return [p.profit for p in path], [p.weight for p in path], sum(p.profit for p in path)
        
        for i in range(1, n):
            new_weight = node.weight + weights[i]
            if new_weight > max_weight:
                continue
            new_profit = node.profit + profits[i]
            new_node = Node(new_weight, new_profit, node, path_cost=node.path_cost+1, heuristic_cost=new_profit/new_weight)
            heapq.heappush(nodes, new_node)
    
    return [], [], 0
