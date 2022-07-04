1. iterate over all the elements of grid using r and c
2. call a helper function that performs traversal with params -> grid, r, c, visited
3. create the explore function
4. inside this create a name to add to visited if its not visited
5. create rowinbounds and colinbounds where 0<=r and r < len(grid) and so on
6. if not rowinbounds or colinbounds return False
7. if the cell contains water return false
8. if visited return false
9. add the cell to visted
10. Run explore function all 4 sides recursively (r-1, c) (r+1, c) (r, c-1) and (r,c+1)
11. return a True
​
12. Check if explore == True in main function then increment count and return count