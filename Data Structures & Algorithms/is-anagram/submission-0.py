class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        for char in t:
            freq[ord(char) - ord('a')] -= 1
        
        for i in range(26):
            if freq[i] != 0: return False
        
        return True