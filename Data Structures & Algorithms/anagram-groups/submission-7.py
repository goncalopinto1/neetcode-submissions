from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anam = defaultdict(list)
        final = list()

        for s in strs:
            l = [0] * 26

            for ch in s:
                l[ord(ch) - ord('a')] += 1
        
            t = tuple(l)

            anam[t].append(s)

        for k, v in anam.items():
            final.append(v)
        
        return final
        
            
        


