# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1. find the middle of list using fast and slow pointer 
2. reverse the second half of list 
3. combine first half and second half by modifying the pointers
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        prev = None
        second = slow.next 
        slow.next = None
        
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
            