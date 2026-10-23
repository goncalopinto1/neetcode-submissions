import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []

        # creating a max heap

        for n in stones:
            heapq.heappush(h, -n)
        
        while len(h) > 1:
            rock1 = -heapq.heappop(h)
            rock2 = -heapq.heappop(h)

            if rock1 == rock2:
                continue
            if rock1 > rock2:
                rock1 -= rock2
                heapq.heappush(h, -rock1)

        if len(h) == 0:
            return 0

        return -heapq.heappop(h)