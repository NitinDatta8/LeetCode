class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        if len(edges) != n-1: 
            return False
        
        def find(n): 
            p = par[n]
            
            while p != par[p]: 
                par[p] = par[par[p]] # path compression (makes algorithm faster)
                p = par[p]
            
            return p 
        
        def union(n1, n2): 
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return False 
            
            par[p2] = p1
            
            return True 
        
        for n1, n2 in edges: 
            if not union(n1, n2): 
                return False 
            
        return True