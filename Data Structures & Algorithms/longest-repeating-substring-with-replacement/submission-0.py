from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()

        l = 0
        best = 0

        for r in range(len(s)):
            count[s[r]] += 1

            while (r - l + 1) - max(count.values()) > k: # tenho de retirar da esquerda ate ser igual a k 
                count[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)

        return best
        
                
            