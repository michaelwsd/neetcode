class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        # construct graph
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei, node):
                        return True
                elif nei != parent:
                    return True
            
            return False

        for node in range(n):
            if node not in visited:
                if dfs(node, -1):
                    return False
        
        return len(visited) == n