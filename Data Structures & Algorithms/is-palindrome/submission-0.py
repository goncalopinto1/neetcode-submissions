class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = 0
        l = len(s) - 1

        while r < l:
            if not s[r].isalnum():
                r += 1
                continue
            elif not s[l].isalnum():
                l -= 1
                continue
            elif s[r].lower() != s[l].lower(): return False
            r += 1
            l -= 1
        
        return True