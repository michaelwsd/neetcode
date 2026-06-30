class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for crs in range(numCourses): graph[crs] = []
        for u, v in prerequisites:
            graph[u].append(v)

        visited, cycle = set(), set()
        res = []
        print(graph)
        def dfs(crs):
            if crs in cycle:
                return False 
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False 
            
            visited.add(crs)
            res.append(crs)
            cycle.remove(crs)
            return True 
        
        for crs in range(numCourses):
            r = dfs(crs)
            if not r: 
                return []

        return res

            
