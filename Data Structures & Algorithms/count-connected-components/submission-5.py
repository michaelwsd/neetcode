class DSU:
    def __init__(self, size):
        self.par = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        
        return x
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False 
        else:
            if self.rank[p1] > self.rank[p2]:
                self.par[p2] = p1
                self.rank[p1] += self.rank[p2]
            else:
                self.par[p1] = p2
                self.rank[p2] += self.rank[p1]

        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res