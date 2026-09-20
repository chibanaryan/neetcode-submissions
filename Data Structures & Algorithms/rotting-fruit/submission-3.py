from collections import deque


OFFSETS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = -1
        # Iterate, track rotten coords
        rows, cols = len(grid), len(grid[0])
        q = deque([])
        has_fresh = False

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    has_fresh = True
        
        if not has_fresh:
            return 0
        
        # BFS loop, increment time
        while q:
            time += 1
            for _ in range(len(q)):
                cr, cc = q.popleft()
                for offset in OFFSETS:
                    dr, dc = offset
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        print(nr, nc)
                        grid[nr][nc] = 2
                        q.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return time

        
        # Iterate, if find fresh fruit, return -1
        # Return time