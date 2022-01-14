class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        freq = {}
        count=0
        for i in emails:
            local,domain = i.split('@')
            local = local.replace('.','')
            local = local.split('+')[0]
            mail = local+'@'+domain
            if mail not in freq: 
                count += 1
                freq[mail] = 1
            else:
                freq[mail] += 1
        return count