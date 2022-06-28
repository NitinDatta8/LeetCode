# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head 
        count = 0 
        while cur: 
            count += 1
            cur = cur.next 
        
        if count == n: 
            head = head.next 
            return head 
        
        prev = None
        cur = head
        while cur and count != n: 
            prev = cur 
            cur = cur.next 
            count -= 1
        
        prev.next = cur.next
        cur = None 
        return head