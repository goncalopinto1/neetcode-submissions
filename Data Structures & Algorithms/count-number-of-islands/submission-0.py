from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()

        queue = deque([])

        directions = [[1,0], [-1,0],[0,1],[0,-1]]

        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1" and (r,c) not in seen:
                    queue.appendleft((r,c))
                    islands += 1

                    while len(queue) > 0:
                        val = queue.pop()

                        if val not in seen:
                            seen.add(val)

                            for d in directions:
                                new_r = val[0] + d[0]
                                new_c = val[1] + d[1]

                                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == "1":
                                    queue.appendleft((new_r, new_c))
                    

        return islands
                                