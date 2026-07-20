class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        total = n * m
        k %= total

        ans = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):

                old_index = i * m + j
                new_index = (old_index + k) % total

                new_row  = new_index // m
                new_col = new_index % m

                ans[new_row][new_col] = grid[i][j]

        return ans
