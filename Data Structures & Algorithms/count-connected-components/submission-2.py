class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * n

        def dfs(node):
            if visited[node]: return 
            
            visited[node] = True
            for nei in graph[node]:
                dfs(nei)

        res = 0
        for node in range(n):
            if visited[node]: continue
            print(node)
            dfs(node)
            res += 1

        return res


