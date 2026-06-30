class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]: continue 
            l, r = i+1, len(nums)-1

            target = -n
            while l < r:
                s = nums[l] + nums[r]
                if s > target:
                    r -= 1
                elif s < target: 
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])

                    l += 1
                    while 0 < l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                    
                    r -= 1
                    while 0 <= r < len(nums)-1 and nums[r] == nums[r+1]:
                        r -= 1

        
        return res
            


