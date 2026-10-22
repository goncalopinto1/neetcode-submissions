from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        original_counter = Counter(s1)
        c = Counter()

        l = 0
        for r in range(len(s2)):
            if s2[r] in original_counter.keys():
                c[s2[r]] += 1

            if s2[l] in original_counter.keys():
                if (r - l + 1) == len(s1):
                    if original_counter == c: 
                        return True
                    else:
                        c[s2[l]] -= 1
                        l += 1
            else:
                l += 1        



        return False

