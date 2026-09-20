OFFSETS = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            grid[r][c] = "0"
            for offset in OFFSETS:
                dr, dc = offset
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue
                count += 1
                dfs(r, c)
        return count