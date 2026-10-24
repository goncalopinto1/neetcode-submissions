from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        seen = set()
        queue = deque([])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        time = 0
        contaminated_someone = False
        non_infected = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.appendleft((r,c))
                elif grid[r][c] == 1:
                    non_infected += 1

        
        while len(queue) > 0:
            for _ in range(len(queue)): #each level
                r, c = queue.pop()
                seen.add((r,c))

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and (new_r, new_c) not in seen and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        queue.appendleft((new_r, new_c))
                        contaminated_someone = True
                        non_infected -= 1

            if contaminated_someone:
                time += 1
                contaminated_someone = False
            
        if non_infected > 0:
            return -1 

        return time