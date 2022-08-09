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
        
        while len(lists) > 1:
            merged_lists = []
            
            for i in range(0, len(lists), 2): 
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.merge_two_lists(l1, l2))
            lists = merged_lists
        return lists[0]
    
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