"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = {None:None}
        
        cur = head 
        while cur: 
            copy = Node(cur.val)
            old_to_copy[cur] = copy
            cur = cur.next
        
        cur = head 
        while cur: 
            copy = old_to_copy[cur]
            copy.next = old_to_copy[cur.next]
            copy.random = old_to_copy[cur.random]
            cur = cur.next
        
        return old_to_copy[head]