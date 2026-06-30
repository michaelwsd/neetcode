class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i, j):
            if i == len(nums):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = 0
            for k in range(i, len(nums)):
                if j == -1 or nums[k] > nums[j]: 
                    res = max(res, 1 + dfs(k+1, k))
            
            dp[(i, j)] = res
            return res

        return dfs(0, -1)

            