from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        top = []

        for key, val in freq.items():
            if len(top) < k:
                heapq.heappush(top, (val, key))
            else:
                if val > top[0][0]:
                    heapq.heappop(top)
                    heapq.heappush(top, (val, key))
        
        return [key for value, key in top]
            




