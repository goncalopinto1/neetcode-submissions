class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            if area > best:
                best = area
            
            if min(heights[r], heights[l]) == heights[r]:
                r -= 1
            else:
                l += 1
        
        return best