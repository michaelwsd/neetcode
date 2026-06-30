class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = defaultdict(list) # count -> [words]

        for s in strs:
            count = tuple(sorted(Counter(s).items()))
            c[count].append(s)

        return list(c.values())

        


