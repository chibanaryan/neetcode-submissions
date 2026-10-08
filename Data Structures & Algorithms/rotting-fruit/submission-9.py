from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque([])
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))

        timer = 0
        offsets = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        while q:
            for i in range(len(q)):
                cr, cc = q.popleft()
                for dr, dc in offsets:
                    nr, nc = cr+dr, cc+dc
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            if q:
                timer += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return timer
                