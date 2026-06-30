class DSU:
    def __init__(self, size):
        self.par = [i for i in range(size+1)]
        self.rank = [1] * (size+1) 

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]

        return x 
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False 
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1 
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))

        for u, v in edges:
            if not dsu.union(u, v): 
                return [u, v]
        
        return []