class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set(Counter(nums).values())

        if not nums: return False
        return not (1 in dup and len(dup) == 1)