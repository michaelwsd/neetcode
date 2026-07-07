class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}

        for u, v in prerequisites:
            graph[v].append(u)
        
        canTake = [False] * numCourses

        def check(c, visited):
            if c in visited:
                return False
            if not graph[c]:
                canTake[c] = True
                return True 
            
            visited.add(c)

            for pre in graph[c]:
                if not check(pre, visited):
                    return False 
            
            return True 
        
        for i in range(numCourses):
            if not canTake[i] and not check(i, set()):
                return False 
        
        return True

            
