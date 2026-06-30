class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        res = 0
        
        p1 = 0
        for p2 in range(len(s)):
            freq[s[p2]] += 1
            currLen, currMax = p2 - p1 + 1, max(freq.values())
            while p1 < p2 and currLen - currMax > k:
                freq[s[p1]] -= 1
                if freq[s[p1]] == 0: del freq[s[p1]]
                p1 += 1
                currLen, currMax = p2 - p1 + 1, max(freq.values())
                
            
            res = max(res, currLen)
        
        return res

