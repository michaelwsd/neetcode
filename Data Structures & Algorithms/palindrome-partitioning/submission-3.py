class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, j, curr):
            if i == len(s):
                res.append(curr[:])
                return 
            
            for k in range(i, len(s)):
                currStr = s[i:k+1]
                if currStr == currStr[::-1]:
                    curr.append(currStr)
                    dfs(k+1, k+1, curr)
                    curr.pop()

        dfs(0, 0, [])
        return res 