class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        i = 0
        res = []
        while (i < len(nums)):
            curr = nums[i]
            target = -curr

            l, r = i+1, len(nums)-1
            while (l < r):
                s = nums[l] + nums[r]
                if (s < target): l += 1
                elif (s > target): r -= 1
                else: 
                    res.append([curr, nums[l], nums[r]])
                    while (l+1 < len(nums) and nums[l+1] == nums[l]):
                        l += 1
                    
                    while (r-1 >= 0 and nums[r-1] == nums[r]):
                        r -= 1

                    l += 1
                    r -= 1

            while (i+1 < len(nums) and nums[i+1] == nums[i]):
                i += 1
            
            i += 1
        
        return res

    