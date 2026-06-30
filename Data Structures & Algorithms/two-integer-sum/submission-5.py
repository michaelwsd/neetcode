class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp in c:
                return [c[comp], i]
            
            c[n] = i

        return []
