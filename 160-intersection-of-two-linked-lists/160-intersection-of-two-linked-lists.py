# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
  P p1
  4 1 8 4 5 
  4 1 8 4 5
    p2



'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lena, lenb = 0,0 
        cur = headA
        while cur: 
            lena += 1
            cur = cur.next

        cur = headB
        while cur: 
            lenb += 1
            cur = cur.next 

        diff  = abs(lena - lenb)
        flag = 0
        if lena > lenb:
            cur = headA
            while cur and diff!=0: 
                cur = cur.next
                diff -= 1
        else: 
            cur = headB 
            flag = 1
            while cur and diff!=0:
                cur = cur.next 
                diff -= 1
        # so cur points 6 in ListB        
        if flag == 1: 
            new_cur = headA
        else: 
            new_cur = headB
        
        print(cur.val, new_cur.val)
        while cur and new_cur: 
            if  cur == new_cur: 
                return new_cur
            cur = cur.next
            new_cur = new_cur.next
    