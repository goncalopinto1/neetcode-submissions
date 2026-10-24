from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        best_area = 0
        area = 0
        seen = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        stack = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in seen:
                    seen.add((r,c))
                    stack.append((r,c))
                    area += 1

                    while len(stack) > 0:
                        nr, nc = stack.pop()

                        for d in directions:
                            new_r = nr + d[0]
                            new_c = nc + d[1]

                            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and (new_r, new_c) not in seen and grid[new_r][new_c] == 1:
                                seen.add((new_r, new_c))
                                area += 1 
                                stack.append((new_r, new_c))
                
                best_area = max(best_area, area)
                area = 0
        return best_area
                    