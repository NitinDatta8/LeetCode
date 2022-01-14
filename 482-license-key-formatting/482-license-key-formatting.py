class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-','')
        new_s = []
        orig_k = k
        for i in range(len(s)-1,-1,-1):
            # print(s[i],k)
            if k>0:
                new_s.append(s[i].upper())
                k -= 1
            else: 
                new_s.append('-')
                new_s.append(s[i].upper())
                k = orig_k-1
            
        return ''.join(new_s[::-1])