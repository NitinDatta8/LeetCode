class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target>1:
            if target%2==0 and maxDoubles>0:
                target //= 2
                maxDoubles -= 1
                count += 1
            else: 
                if maxDoubles == 0:
                    count += target -1
                    target -= target
                else:
                    target -= 1
                    count += 1
            # print(target)
        return count