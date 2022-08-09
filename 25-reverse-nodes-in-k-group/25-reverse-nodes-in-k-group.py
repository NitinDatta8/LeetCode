# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy 
        
        while True: 
            kth = self.get_kth(group_prev, k)
            if not kth: 
                break 
            group_next = kth.next
            
            prev, cur = kth.next, group_prev.next
            while cur != group_next: 
                nxt = cur.next 
                cur.next = prev 
                prev = cur 
                cur = nxt
            tmp = group_prev.next 
            group_prev.next = kth
            group_prev = tmp 
            
        return dummy.next
    
    def get_kth(self, cur, k): 
        while cur and k > 0: 
            cur = cur.next 
            k -= 1
        return cur