 # people = [3,5,3,4], limit = 5
 # people = [3,3,4,5]
 #           lr   
 # bc = 4
# take sum of left and right 
# if sum is greater than the limit increment boat_count by 1 and reduce right pointer 
# else increment boat count by 1 and move left + 1 and right -1 
# while l<=r


# checking for limit --> reset the sum to 0 and increment boat count 
# checking for 2 people in a boat and sum < limit --> reset sum to 0 and increment boat count 
# [1,1,2,2]
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people)-1
        boat_count = 0 
        msum = 0
        people.sort()
        while l<=r:
            msum = people[l] + people[r]
            if msum > limit: 
                boat_count += 1
                r -= 1
            else:
                boat_count += 1
                l += 1
                r -= 1
        return boat_count 
                