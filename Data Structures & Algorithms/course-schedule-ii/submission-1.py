class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # construct graph
        graph = {i:[] for i in range(numCourses)}
        for prereq in prerequisites:
            u, v = prereq[0], prereq[1]
            graph[u].append(v)
        
        visited, cycle = set(), set()
        res = []

        def dfs(course):
            if course in cycle:
                return False

            if course in visited:
                return True

            if not graph[course]:
                visited.add(course)
                res.append(course)
                return True 
            
            cycle.add(course)
            for p in graph[course]:
                if not dfs(p):
                    return False
            
            cycle.remove(course)
            # this course can be completed, add to visited
            visited.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res 
            
