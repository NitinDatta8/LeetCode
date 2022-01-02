class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        counts = []
        for i in bank:
            count_1 = i.count('1')
            counts.append(count_1)
        
        
        X = [i for i in counts if i != 0]
        
        final_list = []
        for i in range(len(X)-1):
            final_list.append(X[i]*X[i+1])
            
        return sum(final_list)