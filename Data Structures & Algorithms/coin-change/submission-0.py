class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(i, curr):
            if curr == amount:
                return 0
            if curr > amount or i >= len(coins):
                return float('inf')
            if (i, curr) in dp: return dp[(i, curr)]

            dp[(i, curr)] = float('inf')
            dp[(i, curr)] = min(dp[(i, curr)], 1 + dfs(i, curr + coins[i]), dfs(i+1, curr))

            return dp[(i, curr)]

        res = dfs(0, 0)
        return res if res != float('inf') else -1
        