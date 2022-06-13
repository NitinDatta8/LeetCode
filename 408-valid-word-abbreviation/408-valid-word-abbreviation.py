# use i for word and j for abbr 
# if j isalpha and i == j: increment both else return False 
# if j isnumeric pointer X : while j is not numeric j ++: num = int(abbr[X:j])
# increment i by num 
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i,j = 0, 0 
        x = 0 
        while i < len(word) and j < len(abbr):
            if abbr[j] == word[i]:
                i += 1
                j += 1
            elif abbr[j] == '0':
                return False 
            elif abbr[j].isnumeric(): 
                k = j 
                while k < len(abbr) and abbr[k].isnumeric():
                    k += 1
                i += int(abbr[j:k])
                j = k 
            else: 
                return False 
        return i == len(word) and j == len(abbr) 