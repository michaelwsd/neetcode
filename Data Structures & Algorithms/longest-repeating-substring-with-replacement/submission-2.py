class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l, maxf = 0, 0
        res = 0

        for r, c in enumerate(s):
            count[c] += 1
            maxf = max(maxf, count[c])
            
            # check window 
            while r - l + 1 - maxf > k:
                lc = s[l]
                count[lc] -= 1
                if count[lc] == 0:
                    del count[lc]
                l += 1

            res = max(res, r - l + 1)

        return res

