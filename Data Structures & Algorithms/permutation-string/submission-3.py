from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        base_counter = Counter(s1)

        window_counter = Counter()

        l = 0

        for r in range(len(s2)):
            if s2[r] not in base_counter.keys():
                if s2[l] in window_counter.keys():
                    window_counter[s2[l]] -= 1

                if window_counter[s2[l]] == 0:
                    del window_counter[s2[l]]

                l += 1
                continue
            
            window_counter[s2[r]] += 1

            if (r - l + 1) < len(s1):
                continue
            
            else:
                if base_counter == window_counter:
                    return True
                else:
                    if s2[l] in window_counter.keys():
                        window_counter[s2[l]] -= 1

                    if window_counter[s2[l]] == 0:
                        del window_counter[s2[l]]
                    
                    l += 1
                    continue
        
        return False

        '''
        ab

        lecabee
        '''
