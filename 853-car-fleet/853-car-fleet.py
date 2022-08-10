'''
combine speed and position together and sort based on position 
reverse iterate and calculate time it takes to reach the target 
if 
 target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
 (10, 2), (8, 4), (0, 1), (5, 1), (3, 3)

(0,1) (3,3) (5,1) (10,2)
time taken to reach target: 
so iterate reverse and add to stack 
check if time taken for previous is greater than current then remove the current 
3 fleets 


'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pairs)[::-1]: 
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()
        return len(stack)