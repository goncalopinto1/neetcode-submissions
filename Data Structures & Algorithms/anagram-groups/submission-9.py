from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anam = defaultdict(list)

        for s in strs:
            l = [0] * 26

            for ch in s:
                l[ord(ch) - ord('a')] += 1
        
            t = tuple(l)

            anam[t].append(s)
        
        return list(anam.values())
        
            
        


