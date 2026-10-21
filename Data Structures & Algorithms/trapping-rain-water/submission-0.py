class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        postfix = [0] * len(height)

        best = 0

        for idx in range(len(height)):
            if idx == 0: 
                prefix[idx] = 0
                best = max(best, height[idx])
                continue 

            prefix[idx] = best

            best = max(best, height[idx])
        
        best = 0

        for idx in reversed(range(len(height))):
            if idx == len(height) - 1: 
                postfix[idx] = 0
                best = max(best, height[idx])
                continue
            
            postfix[idx] = best

            best = max(best, height[idx])

        water = 0
        for i in range(len(height)):
            water += max(0, min(prefix[i], postfix[i]) - height[i])

        return water
           