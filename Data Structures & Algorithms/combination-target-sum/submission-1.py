class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, subset):
            if curr == target:
                res.append(subset[:])
                return 
            if i == len(nums) or curr > target:
                return 

            subset.append(nums[i])
            dfs(i, curr + nums[i], subset)
            subset.pop()
            dfs(i+1, curr, subset)

        dfs(0, 0, [])
        return res
            