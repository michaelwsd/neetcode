# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root: return res
        
        queue = deque([root])

        while queue:
            length = len(queue)
            curr = []
            for _ in range(length):
                node = queue.popleft()
                curr.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right) 

            res.append(curr)

        return res