class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i in dp: return dp[i]

            LIS = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    LIS = max(LIS, 1 + dfs(j))

            dp[i] = LIS
            return LIS

        return max(dfs(i) for i in range(len(nums)))
