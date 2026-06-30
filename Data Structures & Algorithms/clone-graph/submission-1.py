"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeClone = {}
        if not node: return node

        def dfs(node):
            if node in nodeClone: 
                return nodeClone[node]
            
            clone = Node(node.val)
            nodeClone[node] = clone

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            
            return clone

        return dfs(node)
