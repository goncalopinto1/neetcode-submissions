from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        seen = set()
        stack = []

        def dfs(r,c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or (r,c) in seen or grid[r][c] != 1:
                return 0
            seen.add((r,c))
            return 1 + dfs(r +1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = max(area, dfs(r,c))
        
        return area
                    