class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] + nums + [1]
        suffix = [1] + nums + [1]

        for i in range(1, len(prefix)):
            prefix[i] *= prefix[i-1]
        
        for i in range(len(suffix)-2, -1, -1):
            suffix[i] *= suffix[i+1]
        
        res = []
        for i in range(1, len(prefix)-1):
            res.append(prefix[i-1] * suffix[i+1])

        return res