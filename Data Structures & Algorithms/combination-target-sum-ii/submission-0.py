class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def dfs(i, target):
            if target == 0:
                res.append(subset[:])
                return
            if i == len(candidates) or target < 0:
                return

            subset.append(candidates[i])
            dfs(i+1, target - candidates[i])
            subset.pop()

            while (i+1 < len(candidates) and candidates[i+1] == candidates[i]):
                i += 1
            dfs(i+1, target)
        
        dfs(0, target)
        return res