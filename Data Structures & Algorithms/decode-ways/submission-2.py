from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:

        @lru_cache(maxsize=None)
        def dfs(i, curr):
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            if s[i] == '0' and not curr:
                return 0

            res = 0

            # first number, not 0 -> accumulate
            if s[i] != '0':
                res += dfs(i+1, s[i])

            # second number
            if len(curr) == 1:
                if ((curr == '1' and '0' <= s[i] <= '9') or 
                    (curr  == '2' and '0' <= s[i] <= '6')):
                    res += dfs(i+1, '')
            
            return res

        return dfs(0, '')
