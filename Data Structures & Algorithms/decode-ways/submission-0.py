class Solution:
    def numDecodings(self, s: str) -> int:
        dp = defaultdict(int)
        def dfs(i):
            if i == len(s):
                return 1
            if i >= len(s) or s[i] == '0':
                return 0
            if i in dp:
                return dp[i]

            dp[i] = dfs(i+1)

            # one or two
            if i+1 < len(s) and (int(s[i]) == 1 or (int(s[i]) == 2 and int(s[i+1]) < 7)):
                dp[i] += dfs(i+2)
            
            return dp[i]

        return dfs(0)
            