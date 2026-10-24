from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        best_area = 0
        area = 0

        seen = set()

        queue = deque([])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(len(grid)):
            for c in range(len(grid[r])):

                if grid[r][c] == 1 and (r,c) not in seen:
                    seen.add((r,c))

                    queue.appendleft((r,c))

                    while len(queue) > 0:

                        area += 1

                        val = queue.pop()

                        for d in directions:
                            new_r = val[0] + d[0]
                            new_c = val[1] + d[1]

                            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[r]) and (new_r, new_c) not in seen and grid[new_r][new_c] == 1:
                                seen.add((new_r, new_c))
                                queue.appendleft((new_r, new_c))
                
                    best_area = max(best_area, area)
                    area = 0

        return best_area