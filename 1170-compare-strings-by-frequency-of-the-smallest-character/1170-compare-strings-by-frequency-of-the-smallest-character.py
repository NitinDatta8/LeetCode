class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        result = []
        for query in queries: 
            main_count = 0 
            q_sort = sorted(query)
            q_first = q_sort[0]
            q_count = 0 
            for x in q_sort: 
                if x == q_first: 
                    q_count += 1
                else:
                    break 
            for word in words: 
                w_sort = sorted(word)
                w_first = w_sort[0]
                w_count = 0 
                for y in w_sort: 
                    if y == w_first: 
                        w_count += 1
                    else: 
                        break
                if q_count<w_count: 
                    main_count += 1
            result.append(main_count)
        return result