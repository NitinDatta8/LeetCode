use BFS
maintain time and fresh oranges
in first 2 loops count fresh oranges and add rotten oranges to a queue
run the queue and popleft and use for loop to check adjacent cells
change adjacent 1s to 2s and append to queue
reduce fresh
increase time
return time if fresh == 0 else -1