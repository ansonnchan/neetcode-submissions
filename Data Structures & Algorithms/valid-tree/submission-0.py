class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #undirected graph 
        #a graph is invalid if if there's a cycle and if it's not connected
        #more importantly, [1,2] -> [2,3] -> [3,1]
        #maybe we can try a dictionary; how we map the edges

        if len(edges) > (n-1):
            return False
        
        adjacency_list = [[] for i in range(n)]

        for u,v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in adjacency_list[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor,node):
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n

       