class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map sorted string to list of strings
        dic = defaultdict(list)

        for s in strs:
            dic["".join(sorted(s))].append(s)
        
        res = []
        for key in dic:
            res.append(dic[key])
        
        return res