class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perm = self.permute(nums[1:])
        res = []

        # add nums[0] to every position in each perm
        for p in perm:
            for i in range(len(p) + 1):
                p_copy = p[:]
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        
        return res