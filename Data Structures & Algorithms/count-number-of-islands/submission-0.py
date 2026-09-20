from collections import deque
from pprint import pp

OFFSETS = [
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0),
]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        pp(grid)
        count = 0
        
        rows, cols = len(grid), len(grid[0])
        # Iterate row-wise and column-wise
        for r in range(rows):
            for c in range(cols):
                val = grid[r][c]
                if grid[r][c] != "1":
                    continue
                count += 1
                q = deque([(r, c)])
                grid[r][c] = "0"
                while q:
                    # print(q)
                    # Check validity
                    cr, cc = q.popleft()
                    for dr, dc in OFFSETS:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            q.append((nr, nc))
        return count

                    
            # If 0, increment count and queue up valid neighbors until exhausted and set to 1
            # Else continue