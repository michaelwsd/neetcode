class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # construct graph
        for prereq in prerequisites:
            u, v = prereq[0], prereq[1]
            graph[u].append(v)
        
        def dfs(course, visited):
            if len(graph[course]) == 0:
                return True
            if visited[course]:
                return False
            
            visited[course] = True
            
            for prereq in graph[course]:
                taken = dfs(prereq, visited)
                if taken: graph[prereq] = []
                else: return False

            graph[course] = []
            return True
             
        visited = [False] * numCourses
        for course in range(numCourses):
            if not dfs(course, visited):
                return False
        
        return True