class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i, prev):
            if i == len(nums): return 0
            if (i, prev) in dp: return dp[(i, prev)]

            dp[(i, prev)] = dfs(i+1, prev)
            if prev == -1 or (prev != -1 and nums[i] > nums[prev]):
                dp[(i, prev)] = max(dp[(i, prev)], 1 + dfs(i+1, i))

            return dp[(i, prev)]

        return dfs(0, -1)
