# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        heap = []
        for ln in lists:
            heapq.heappush(heap, NodeWrapper(ln))
        
        while len(heap) > 0:
            n = heapq.heappop(heap)
            # add to result
            curr.next = ListNode(n.node.val)
            curr = curr.next

            # add the next node
            if n.node.next:
                n.node = n.node.next
                heapq.heappush(heap, n)
        
        return dummy.next


