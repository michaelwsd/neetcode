class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        n = len(nums)
        dp = {}

        def dfs(i, first):
            if i >= len(nums) or (first and i == len(nums)-1):
                return 0
            if (i, first) in dp:
                return dp[(i, first)]

            dp[(i, first)] = max(nums[i] + dfs(i+2, first), dfs(i+1, first))
            return dp[(i, first)]
            
            

        return max(dfs(0, True), dfs(1, False)) 
