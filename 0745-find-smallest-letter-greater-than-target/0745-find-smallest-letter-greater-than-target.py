class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s, e = 0, len(letters) - 1
        while s <= e: 
            mid = (s + e) // 2
            if ord(letters[mid]) == ord(target) and mid < len(letters) - 1:
                if letters[mid] == letters[mid + 1]: 
                    s = mid + 1
                else: 
                    return letters[mid + 1]
            elif ord(letters[mid]) > ord(target): 
                e = mid - 1
            else: 
                s = mid + 1

        print(s, e, mid)
        if s > len(letters) - 1: 
            return letters[0]
        return letters[s]