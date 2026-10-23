from collections import Counter,deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # equal task[i] must be separated by n time
        c = Counter(tasks) # O(1) here

        h = []
        iddle = deque([])

        time = 0

        for v in c.values():
            heapq.heappush(h, -v)
        
        while len(h) > 0 or len(iddle) > 0:

            time += 1

            if len(h) > 0:
                val = heapq.heappop(h)

                val += 1

                if val != 0:
                    iddle.appendleft((val, time + n))
            
            if len(iddle) > 0:
                if iddle[-1][1] == time:
                    val = iddle.pop()
                    heapq.heappush(h, val[0])

        return time