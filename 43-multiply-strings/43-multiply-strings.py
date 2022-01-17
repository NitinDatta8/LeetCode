class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        lnums1, lnums2 = len(num1), len(num2)
        int_nums1, int_nums2 = 0,0
        for i in range(lnums1):
            val = num1[i]
            intval= 10**(lnums1-i-1) * (ord(val)-ord('0'))
            int_nums1 += intval
        
        for i in range(lnums2):
            val = num2[i]
            intval= 10**(lnums2-i-1) * (ord(val)-ord('0'))
            int_nums2 += intval
            
        return str(int_nums1*int_nums2)
            
            