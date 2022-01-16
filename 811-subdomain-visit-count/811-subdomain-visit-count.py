class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        freq = {}
        for i in cpdomains: 
            count,domain = i.split(' ')
            x = domain.split('.')
            subdomains = []
            if len(x) == 3: 
                subdomains.append(domain)
                subdomains.append(x[1]+'.'+x[2])
                subdomains.append(x[2])
            else:
                subdomains.append(domain)
                subdomains.append(x[1])
            for dom in subdomains:
                if dom not in freq: 
                    freq[dom] = int(count)
                else:
                    freq[dom] += int(count)
        return [str(str(val) + ' ' + key) for key,val in freq.items()]