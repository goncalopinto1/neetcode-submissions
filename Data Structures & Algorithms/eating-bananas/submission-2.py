import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) # O(n)

        res = r

        while l <= r:
            middle = (r + l) // 2

            acc = 0

            for n in piles:
                acc += math.ceil(n / middle)
            if acc <= h:
                res = middle
                r = middle - 1
                acc = 0
            else:
                l = middle + 1
                acc = 0
        
        return res
            