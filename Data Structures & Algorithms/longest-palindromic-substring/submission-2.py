class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        res, resStr = 1, s[0]

        def getPali(l, r):
            length, st = 1, ""
            while (l >= 0 and r < len(s)) and s[l] == s[r]:
                if r - l + 1 > length:
                    length = max(length, r - l + 1)
                    st = s[l:r+1]
                l -= 1
                r += 1
            
            return [length, st]
        
        for i in range(len(s)):
            # even length
            even = getPali(i, i+1)
            if even[0] > res:
                res, resStr = even[0], even[1]

            # odd length
            odd = getPali(i-1, i+1)
            if odd[0] > res:
                res, resStr = odd[0], odd[1]
        
        return resStr
