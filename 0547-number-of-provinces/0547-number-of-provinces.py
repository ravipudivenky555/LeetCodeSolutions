class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        c=0
        nodes=[i for i in range(len(isConnected))]
        def dfs(graph,i,visited):
            for j in range(len(graph[i])):
                if graph[i][j]==1 and j not in visited:
                    visited.add(j)
                    dfs(graph,j,visited)
            return visited
        while nodes:
            c+=1
            for i in dfs(isConnected,nodes[0],{nodes[0]}):
                if i in nodes:
                    nodes.remove(i)
        return c