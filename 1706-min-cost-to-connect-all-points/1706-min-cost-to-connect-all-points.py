class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return abs(self.x-other.x) + abs(self.y-other.y)
class DSU:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
    def find(self, node):
        node = node
        result = self.parent[node]
        while result != self.parent[result]:
            self.parent[result] = self.parent[self.parent[result]]
            result = self.parent[result]
        return result
    def union(self, first, second):
        parent1 = self.find(first)
        parent2 = self.find(second)
        if parent1 == parent2:
            return
        self.parent[parent1] = parent2
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        nodes = []
        for (x, y) in points:
            node = Node(x, y)
            nodes.append(node)
        dsu = DSU(nodes)
        edges = []
        for i in range(length):
            for j in range(i+1, length):
                first, second = nodes[i], nodes[j]
                distance = first-second
                edges.append((first, second, distance))
        edges.sort(key=lambda x: x[2])
        index = 0
        edge_count = 0
        result = 0
        while edge_count < length-1:
            first, second, weight = edges[index]
            if dsu.find(first) != dsu.find(second):
                dsu.union(first, second)
                result += weight
                edge_count += 1
            index += 1
        return result