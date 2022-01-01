# Recursive 
class Solution:
    def LCS(self,text1,text2,n,m):
        
        key = str(m) +','+ str(n)
        if key in self.memo:
            return self.memo[key]
        
        if n==0 or m==0: 
            return 0 
        
        if text1[n-1] == text2[m-1]:
            self.memo[key] = 1 + self.LCS(text1,text2,n-1,m-1)
        else: 
            self.memo[key] = max(self.LCS(text1,text2,n,m-1),self.LCS(text1,text2,n-1,m))
        return self.memo[key]
    
    def longestCommonSubsequence(self, text1, text2):
        n,m = len(text1),len(text2)
        self.memo = {}
        return self.LCS(text1,text2,n,m)
        