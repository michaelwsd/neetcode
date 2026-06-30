class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        phone = {2: 'abc',
                 3: 'def',
                 4: 'ghi',
                 5: 'jkl',
                 6: 'mno',
                 7: 'pqrs',
                 8: 'tuv',
                 9: 'wxyz'}
        
        res = []
        def dfs(i, curr):
            if len(curr) == len(digits):
                res.append(''.join(curr))
                return 
            
            for c in phone[int(digits[i])]:
                curr.append(c)
                dfs(i+1, curr)
                curr.pop()

        dfs(0, [])
        return res