class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False # cycle
        
        if self.rank[rx] >= self.rank[ry]:
            self.parent[ry] = rx
            self.rank[rx] += self.rank[ry]
        else:
            self.parent[rx] = ry
            self.rank[ry] += self.rank(rx)
        
        self.components -= 1
        return True 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)
        
        return dsu.components





