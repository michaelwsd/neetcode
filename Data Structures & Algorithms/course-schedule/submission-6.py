class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[v].append(u)
        
        # 0 = unvisited, 1 = in current path, 2 = confirmed safe
        state = [0] * numCourses

        def check(c):
            if state[c] == 1: return False # cycle
            if state[c] == 2: return True 

            state[c] = 1
            for nbr in graph[c]:
                if not check(nbr):
                    return False 
                
            state[c] = 2
            return True 
        
        return all(check(i) for i in range(numCourses))

            
