class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0

        best = 1
        acc = 1

        freq = set() 

        if len(s) == 0: 
            return 0
        else:
            freq.add(s[l])


        for r in range(1, len(s)):
            if s[r] not in freq:
                freq.add(s[r])
                acc += 1

            else:
                best = max(best, acc)
                acc += 1
                while l <= r:
                    if s[l] == s[r]:
                        acc -= 1
                        l += 1
                        break
                    if s[l] in freq:
                        freq.remove(s[l])
                    acc -= 1
                    l += 1
        
        best = max(best, acc)


        return best

