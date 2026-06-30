class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = Counter(nums)
        longest = 0

        for n in c:
            if c[n] == 0:
                continue 
            
            c[n] = 0
            curr, cnt = n-1, 1
            # explore left 
            while curr in c and c[curr] > 0:
                c[curr] = 0
                cnt += 1
                curr -= 1
            
            # explore right
            curr = n+1
            while curr in c and c[curr] > 0:
                c[curr] = 0
                cnt += 1
                curr += 1
            
            longest = max(longest, cnt)
            
        return longest


