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
            cur = cur.next 
            count += 1
        
        if count == n: 
            head = head.next 
            return head
        
        cur = head 
        prev = None
        while cur and count != n:
            prev = cur
            cur = cur.next 
            count -= 1
            
        prev.next = cur.next 
        cur.next = None
        return head