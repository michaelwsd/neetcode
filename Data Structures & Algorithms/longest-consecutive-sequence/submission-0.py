class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dup = set()
        for num in nums: dup.add(num)

        res = 0
        for num in nums:
            prev = num-1
            nxt = num+1
            count = 1

            while (prev in dup):
                dup.remove(prev)
                prev -= 1
                count += 1    
            
            while (nxt in dup):
                dup.remove(nxt)
                nxt += 1
                count += 1

            res = max(res, count)
        
        return res