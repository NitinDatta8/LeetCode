# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 -> 2 -> 3 -> 4 -> 5
# prev = None 
# cur = head 
# nxt = cur.next 
# cur.next = prev 
# prev = cur 
# cur = nxt

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head 
        while cur: 
            nxt = cur.next 
            cur.next = prev 
            prev = cur
            cur = nxt 
        head = prev 
        return head