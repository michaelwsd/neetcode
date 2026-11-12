class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        for c in t:
            if c not in dic:
                return False
            dic[c] -= 1

        for key in dic:
            if dic[key] != 0:
                return False

        return True 