class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        res = 0

        p1 = 0
        for p2 in range(len(s)):
            if s[p2] in freq:
                while s[p2] in freq:
                    freq[s[p1]] -= 1
                    if freq[s[p1]] == 0:
                        del freq[s[p1]]
                    p1 += 1
            freq[s[p2]] += 1
            res = max(res, p2 - p1 + 1)
        
        return res
                    