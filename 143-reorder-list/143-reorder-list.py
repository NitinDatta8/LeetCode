# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1 -> 2 <- 3 <- 4
          SE    
1 -> 4 -> 2 -> 3

1. use fast slow pointers to find the middle of list 
2. as fast pointer will be on end of list use it and move reverse till slow pointer to reverse the list 
3. start from start and end 
'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nums = []
        cur = head 
        while cur: 
            nums.append(cur.val)
            cur = cur.next 
        l, r = 0, len(nums)-1
        res = []
        flag = 0
        while l<=r:
            if flag == 0: 
                res.append(nums[l])
                l += 1
                flag = 1
            else: 
                res.append(nums[r])
                r -= 1
                flag = 0 
        cur = dummy = ListNode(0)
        for e in res:
            cur.next = ListNode(e)
            cur = cur.next
        
        head.next = dummy.next.next
        # print(head)
        # return dummy.next