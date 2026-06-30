class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(op, cl, curr):
            if op == 0 and cl == 0:
                res.append("".join(curr))

            if op > 0:
                dfs(op-1, cl, curr + ['('])
            
            if cl > 0 and cl > op:
                dfs(op, cl-1, curr + [')'])

        dfs(n, n, [])
        return res