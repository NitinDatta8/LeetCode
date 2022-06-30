# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        O(n)time  o(1) space
        slow, fast
        while fast and fast.next: 
        
        1 2 3->N<-4<-5
        1->5->2
            s         
        head1 = 1
        head2 = 5
        tmp1 = 2
        tmp2 = 4
        
        '''  
        # step1: middle of linked list 
        slow = fast = head 
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        
        # step2: reverse second half of the linked list 
        second = slow.next
        slow.next = None 
        prev = None 
        while second: 
            nxt = second.next
            second.next = prev
            prev = second 
            second = nxt
        
        head1 = head 
        head2 = prev
        while head2: 
            tmp1, tmp2 = head1.next, head2.next
            head1.next = head2
            head2.next = tmp1
            head1 = tmp1
            head2 = tmp2 
        
        return head
            