import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        res = []

        for p in points:
            d = math.sqrt((p[0]**2) + (p[1]**2))

            heapq.heappush(h, (d, p))

        for i in range(k):
            res.append(heapq.heappop(h)[1])

        return res