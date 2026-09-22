from collections import deque


OFFSETS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque([])
        fresh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
            

        
        minutes = 0        
        while q and fresh:
            minutes += 1
            print(grid, q)
            for _ in range(len(q)):
                cr, cc = q.popleft()
                for dr, dc in OFFSETS:
                    nr, nc = cr+dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        print("append ", (nr, nc))
                        q.append((nr, nc))

        if fresh > 0:
            return -1

        return minutes
