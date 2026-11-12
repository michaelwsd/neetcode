class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = defaultdict(int)
        for c in s:
            a[c] += 1
        for c in t:
            if c not in a:
                return False
            a[c] -= 1
        for key in a:
            if a[key] !=0:
                return False
        return True
