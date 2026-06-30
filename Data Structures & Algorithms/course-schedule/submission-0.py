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
            
            satisfy = True
            for prereq in graph[course]:
                satisfy = satisfy and dfs(prereq, visited)

            return satisfy
             

        for course in range(numCourses):
            visited = [False] * numCourses
            if not dfs(course, visited):
                return False
            graph[course] = []
        
        return True