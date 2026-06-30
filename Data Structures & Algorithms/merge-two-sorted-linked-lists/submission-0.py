# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        p1, p2 = list1, list2
        while p1 or p2:
            val1 = p1.val if p1 else 101
            val2 = p2.val if p2 else 101
            if val1 < val2:
                curr.next = ListNode(val1)
                p1 = p1.next if p1 else None
            else:
                curr.next = ListNode(val2)
                p2 = p2.next if p2 else None
            
            curr = curr.next
        
        return dummy.next
