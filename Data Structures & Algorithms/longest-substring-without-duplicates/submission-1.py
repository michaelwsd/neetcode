class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        dup = set()
        res = 0

        while r < len(s):
            if s[r] not in dup:
                dup.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else:
                while l < r and s[r] in dup:
                    dup.remove(s[l])
                    l += 1

        return res 