# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root):
            nonlocal res
            if not root:
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left[1] - right[1]) > 1:
                res = res and False
                return [False, 1 + max(left[1], right[1])]
            else:
                res = res and True
                return [True, 1 + max(left[1], right[1])]

        dfs(root)
        return res

            