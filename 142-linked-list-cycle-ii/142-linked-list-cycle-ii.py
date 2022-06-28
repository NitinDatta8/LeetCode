# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# {3:2, 2:0, 0:-4, }
# 2
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast: 
                break 
        
        else: 
            return None 
        
        while head != slow: 
            slow = slow.next 
            head = head.next
        
        return head
        
            
        
        