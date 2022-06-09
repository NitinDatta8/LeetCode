# Brute force
# go over each element 
# store left of it and right of it. ArithmeticError
# check if that is pallindrome (write helper function or use reverse method)

# Optimized 
# use 2 pointers 
# check left and right if same reduce right and increment left
# 
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1 
        while l < r: 
            if s[l] != s[r]: 
                skipL, skipR = s[l+1:r+1], s[l:r]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            l, r = l + 1, r - 1
        return True