class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1] + nums + [1], [1] + nums + [1]


        for i in range(1, len(suffix)):
            prefix[i] *= prefix[i-1]

        for i in range(len(suffix)-2, -1, -1):
            suffix[i] *= suffix[i+1]

        res = []
        for i in range(1, len(nums)+1):
            res.append(prefix[i-1] * suffix[i+1])

        return res
