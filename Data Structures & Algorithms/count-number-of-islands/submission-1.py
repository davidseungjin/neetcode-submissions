class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # direction = ((1,0), (-1,0), (0,1), (0,-1))
        # rows = len(grid)
        # cols = len(grid[0])
        # island = 0

        # def dfs(r, c):
        #     if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c]=="0"):
        #         return
        #     grid[r][c] = '0'
        #     for dr, dc in direction:
        #         dfs(r + dr, c + dc)


        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1":
        #             dfs(r, c)
        #             island += 1
        # return island

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == "0"
                    ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands