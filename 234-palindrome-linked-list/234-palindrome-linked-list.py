# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head 
        slow = head 
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
            
        # reverse second half
        prev = None
        while slow: 
            tmp = slow.next 
            slow.next = prev
            prev = slow 
            slow = tmp
            
        # check for pallindrome 
        left, right = head, prev 
        while right: 
            if left.val != right.val: 
                return False 
            left = left.next 
            right = right.next 
        return True