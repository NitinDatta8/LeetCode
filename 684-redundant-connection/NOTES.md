we will use union find by rank
par is a list [1,2,3,...len(edges)]
rank is a list [1,1,1,.... 1] len is len(edges)
​
go over every edge and do union on it
update the par and rank lists at the same time
while doing union we need to find its parent
if the parent is same for 2 nodes which we are trying to union then it is already connected so we return those 2 nodes as they form the extra edge which creates a cycle