# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
 1 2 3 4 5 
 k = 2
 length = 5
 breakpoint = 4
 cur = 4
 prev = 3
 count = 3 
'''  
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # find the length 
        cur = head 
        length = 0 
        while cur: 
            length += 1
            cur = cur.next

        if k == 0 or length==0 or length==1:
            return head
        
        k %= length
        if k==0:
            return head
        # handle bigger than len(list)
        

        breakpoint = length -k 
        cur = head 
        prev = None 
        count = 0 
        while cur and breakpoint != count: 
            prev = cur 
            count += 1
            cur = cur.next
        
        prev.next = None 
        dummy = cur 
        
        while cur.next: 
            cur = cur.next
        cur.next = head 
        head = dummy
        
        return head
            