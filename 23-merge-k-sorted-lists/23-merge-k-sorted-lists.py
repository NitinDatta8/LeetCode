# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
take pairs of lists and combine them together 
repeat this operation till only one list is left and return that list 

'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: 
            return None
        
        final_list = lists[0]
        for i in range(1, len(lists)): 
            final_list = self.merge_two_lists(final_list,lists[i])
        
        return final_list
    def merge_two_lists(self, list1, list2):
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