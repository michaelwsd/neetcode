"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        clone = {}

        def cloneNodes(node):
            if node in clone:
                return 
            
            clone[node] = Node(node.val)
            for nei in node.neighbors:
                cloneNodes(nei)
        
        cloneNodes(node)
        nodes = deque([node])
        seen = set()

        while nodes:
            for _ in range(len(nodes)):
                n = nodes.popleft()
                if n in seen: continue
                seen.add(n)

                for nei in n.neighbors:
                    clone[n].neighbors.append(clone[nei])
                    if nei not in seen:
                        nodes.append(nei)

        return clone[node]