# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1 2 3 N <-4 N 
    S
          F
          s
'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head 
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half 
        second = slow.next
        prev = None 
        slow.next = None 
        
        while second: 
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt 
        
        # merge 2 halves 
        first, second = head, prev 
        while second: 
            # store in temp variables 
            tmp1, tmp2 = first.next, second.next 
            # make first connection 1 -> 4 
            first.next = second
            # make second connection 4 -> 2 
            second.next = tmp1
            # move the pointers front 
            first, second = tmp1, tmp2
            
            