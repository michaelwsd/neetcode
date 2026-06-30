class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        freq = Counter(list(s1))
        count = defaultdict(int)

        p1, p2 = 0, 0
        count[s2[0]] += 1
        while p2 - p1 + 1 < len(s1):
            p2 += 1
            count[s2[p2]] += 1

        while p2 < len(s2):
            # validate
            valid = True
            for key in freq:
                if key not in count or count[key] != freq[key]:
                    valid = False
                    break
            
            if valid: return True
     
            # shift window
            count[s2[p1]] -= 1
            if count[s2[p1]] == 0: del count[s2[p1]]
            p1 += 1
            p2 += 1
            if p2 < len(s2): count[s2[p2]] += 1

        return False