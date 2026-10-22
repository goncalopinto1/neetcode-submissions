class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '[': ']', '{': '}'}

        stack = []

        for ch in s:
            if ch in pairs.keys():
                stack.append(ch)
                continue

            if not stack:
                return False

            val = stack.pop()

            if ch != pairs[val]: 
                return False
        
        if stack:
            return False
        
        return True

