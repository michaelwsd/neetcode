class Solution:
    def isPalindrome(self, s: str) -> bool:
        fin = []

        for c in s:
            if c.isalnum():
                fin.append(c.lower())   

        fins = ''.join(fin)
        return fins == fins[::-1]