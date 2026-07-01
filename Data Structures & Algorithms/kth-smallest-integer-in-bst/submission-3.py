# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest = None
        seen = 0

        def dfs(root):
            nonlocal smallest, seen
            if not root or smallest:
                return 
            
            dfs(root.left)
            seen += 1
            if seen == k: smallest = root.val
            dfs(root.right)
        
        dfs(root)
        return smallest
            
