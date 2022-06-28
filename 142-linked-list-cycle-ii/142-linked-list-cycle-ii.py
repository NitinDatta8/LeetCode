# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# {3:2, 2:0, 0:-4, }
# 2
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = {}
        cur = head 
        while cur: 
            if cur not in nodes: 
                nodes[cur] = cur.next 
                if cur.next in nodes: 
                    return cur.next 
            cur = cur.next 
        return None