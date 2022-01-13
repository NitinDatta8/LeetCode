class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        ans = ''
        for i,a in enumerate(arr):
            for j,b in enumerate(arr):
                for k,c in enumerate(arr):
                    if i==j or i==k or j==k:
                        continue
                    hour, minute = str(a) + str(b), str(c) + str(arr[6 - i - j - k])
                    if hour < '24' and minute < '60':
                        ans = max(ans, hour + ':' + minute)
        return ans