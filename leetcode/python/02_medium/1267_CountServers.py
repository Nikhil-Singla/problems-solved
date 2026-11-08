class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        rows = [False] * n
        cols = [False] * m

        for i in range(n):
            if sum(grid[i]) >= 2:
                rows[i] = True

        for i in range(m):
            if sum([eachrow[i] for eachrow in grid]) >= 2:
                cols[i] = True

        count = 0
        for i in range(n):
            for j in range(m):
                if (grid[i][j] == 1) and (rows[i] or cols[j]):
                    count += 1

        return count
