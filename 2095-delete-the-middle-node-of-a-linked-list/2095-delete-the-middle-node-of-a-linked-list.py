# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        if head.next is None: 
            return None
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
        
        cur = head
        prev = None
        while cur and slow!=cur:
            prev = cur 
            cur = cur.next 
        
        prev.next = slow.next 
        slow = None
        return head