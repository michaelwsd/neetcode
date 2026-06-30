class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1, c2 = Counter(s), Counter(t)
        if len(c1) != len(c2): return False 

        for x in c1:
            if x not in c2 or c1[x] != c2[x]:
                return False

        return True