class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""  # Invalid case
        
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited, cycle = set(), set()
        res = []

        def dfs(char):
            if char in cycle: 
                return False  # Cycle detected
            if char in visited:
                return True  # Already processed

            cycle.add(char)
            for neighChar in adj[char]:
                if not dfs(neighChar):  # If a cycle is found, propagate False
                    return False

            cycle.remove(char)
            visited.add(char)
            res.append(char)  # Append to result after all neighbors are processed
            return True

        for char in adj:

            if not dfs(char):  # If cycle is found, return ""
                return ""

        res.reverse()
        return "".join(res)
