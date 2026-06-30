class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        if not digits: return []
        
        res = []
        def dfs(i, curr):
            if i == len(digits):
                res.append(curr)
                return
            
            for char in dic[digits[i]]:
                dfs(i+1, curr + char)
        
        dfs(0, "")
        return res