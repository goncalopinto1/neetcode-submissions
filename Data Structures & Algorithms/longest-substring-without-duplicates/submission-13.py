class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0

        best = 1

        window = set() 

        if len(s) == 0: 
            return 0
        else:
            window.add(s[l])


        for r in range(1, len(s)):
            if s[r] not in window:
                window.add(s[r])
            
            else:
                while s[r] in window:
                    window.remove(s[l])
                    l += 1
                window.add(s[r])
            
            best = max(best, r - l + 1)
        return best

