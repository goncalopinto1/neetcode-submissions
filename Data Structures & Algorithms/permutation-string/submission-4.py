from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)

        window = Counter()

        for r in range(len(s2)):
            window[s2[r]] += 1

            if r >= len(s1):
                window[s2[r - len(s1)]] -= 1

                if window[s2[r - len(s1)]] == 0:
                    del window[s2[r - len(s1)]]

            if window == need:
                return True
        
        return False
