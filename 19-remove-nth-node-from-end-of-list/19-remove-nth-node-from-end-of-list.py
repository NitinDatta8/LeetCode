# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0 
        cur = head 
        while cur: 
            cur = cur.next 
            count += 1
        
        cur = head 
        if count == n: 
            head = cur.next 
            return head 
        
        prev = ListNode(None)
        while cur and count != n: 
            prev = cur 
            cur = cur.next 
            count -= 1
        
        prev.next = cur.next 
        cur = None
        return head