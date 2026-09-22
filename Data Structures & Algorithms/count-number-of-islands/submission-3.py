from collections import deque


OFFSETS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    grid[r][c] = "0"
                    q.append((r, c))
                    while q:
                        cr, cc = q.popleft()
                        for dr, dc in OFFSETS:
                            nr, nc = cr+dr, cc+dc
                            if (0 <= nr < rows and 0 <= nc < cols) and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                q.append((nr, nc))
        return count
                    