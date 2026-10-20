from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqOfS = Counter(s)
        freqOfT = Counter(t)

        if len(freqOfS) != len(freqOfT): return False

        for n in s:
            if freqOfS[n] != freqOfT[n]: return False
        
        return True