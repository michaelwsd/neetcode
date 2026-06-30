class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)

        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            
            if dp[i] != -1:
                return dp[i]

            ways = dfs(i+1) + dfs(i+2)
            dp[i] = ways

            return ways

        return dfs(0)
