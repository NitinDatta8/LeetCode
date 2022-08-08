# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
l1 1 2 4 
l2 2 3 4 
Node(0) -> 1 -> 2  -> 2 -> 3 -> 4 -> 4
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        while list1 and list2: 
            if list1.val < list2.val: 
                cur.next = list1
                list1 = list1.next
            else: 
                cur.next = list2
                list2 = list2.next 
            cur = cur.next 
        
        cur.next = list1 or list2
        return dummy.next