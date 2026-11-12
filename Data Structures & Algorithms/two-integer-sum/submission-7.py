class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {} #key nums[i] value i
        for i, n in enumerate(nums):
            a = target - n
            if a in dic:
                return [dic[a],i]
            dic[n]=i