class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i, prev):
            if i == len(nums):
                return 0
            if (i, prev) in dp:
                return dp[(i, prev)]
            
            res = 0
            for k in range(i, len(nums)):
                if nums[k] <= prev: continue
                res = max(res, 1 + dfs(k+1, nums[k]))
            
            dp[(i, prev)] = res
            return res

        return dfs(0, -1001)

            