class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        
        freq, count = Counter(list(t)), defaultdict(int)
        have, need = 0, len(t)
        res, resLen = [-1, -1], float('inf')

        p1 = 0
        for p2 in range(len(s)):
            # add character at p2
            count[s[p2]] += 1
            if s[p2] in freq and count[s[p2]] <= freq[s[p2]]:
                have += 1

            # case to shrink window
            while have == need:
                if p2 - p1 + 1 < resLen:
                    resLen = p2 - p1 + 1
                    res = [p1, p2+1]
                count[s[p1]] -= 1
                if s[p1] in freq and count[s[p1]] < freq[s[p1]]:
                    have -= 1
                if count[s[p1]] == 0: del count[s[p1]]
                p1 += 1
        
        return s[res[0]:res[1]] if resLen != float('inf') else ""




        