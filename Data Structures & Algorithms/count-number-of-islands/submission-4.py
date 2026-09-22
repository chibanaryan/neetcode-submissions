OFFSETS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r > rows-1 or c < 0 or c > cols-1 or grid[r][c] == "0":
                return
                
            grid[r][c] = "0"
            for dr, dc in OFFSETS:
                dfs(r+dr, c+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0":
                    continue
                
                count += 1
                dfs(r, c)
        return count
        
