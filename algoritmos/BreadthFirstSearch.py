from collections import deque

class Node:
    def __init__(self, weight, profit, parent=None):
        self.weight = weight
        self.profit = profit
        self.parent = parent

def bfs(weights, profits, max_weight):
    n = len(weights)
    nodes = deque([Node(weights[0], profits[0])])
    
    while nodes:
        node = nodes.popleft()
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
            new_node = Node(new_weight, new_profit, node)
            nodes.append(new_node)
    
    return [], [], 0
