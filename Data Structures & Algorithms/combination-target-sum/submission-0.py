class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, target):
            if target == 0:
                res.append(subset[:])
                return
            if i >= len(nums) or target < 0:
                return
            
            subset.append(nums[i])
            dfs(i, target - nums[i])

            subset.pop()
            dfs(i+1, target)
        
        dfs(0, target)
        return res