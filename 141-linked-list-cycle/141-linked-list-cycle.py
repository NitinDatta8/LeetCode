# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow = head 
            fast = head.next
            while slow != fast: 
                fast = fast.next.next
                slow = slow.next 
            return True
        except:
            return False