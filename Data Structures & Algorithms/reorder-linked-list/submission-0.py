# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse linked list
        curr = slow.next
        l2 = slow.next = None
        while curr:
            tmp = curr.next
            curr.next = l2
            l2 = curr
            curr = tmp

        
        l1 = head
        while l1 and l2:
            l1nxt, l2nxt = l1.next, l2.next
            l1.next = l2
            l2.next = l1nxt
            l1 = l1nxt
            l2 = l2nxt




