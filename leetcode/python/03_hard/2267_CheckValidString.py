class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == ')' or grid[m-1][n-1] == "(":
            return False

        @cache
        def helper(row, col, m, n, count):
            if (row, col) == (m-1, n-1):
                return count == 1 

            if grid[row][col] == "(":
                if row+1 < m and helper(row+1, col, m, n, count+1):
                    return True
                elif col+1 < n and helper(row, col+1, m, n, count+1):
                    return True

            else:
                if count <= 0:
                    return False
                elif row+1 < m and helper(row+1, col, m, n, count-1):
                    return True
                elif col+1 < n and helper(row, col+1, m, n, count-1):
                    return True

            return False

        return helper(0, 0, m, n, 0)
