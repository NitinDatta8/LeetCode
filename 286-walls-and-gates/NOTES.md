'''
run 2 for loops and find all the gates put them in a queue
create a visited set
dist = 0
while q:
loop through the q and assign dist to popped element
add in all 4 directions and increment dist  by 1
use helper function to add to q and visited
'''
here we perform BFS from the gates and increase 1 as we go far from gates
from each gate BFS is done simultaneously