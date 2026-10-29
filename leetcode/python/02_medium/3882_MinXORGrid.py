class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        row = [ grid[0][0] ]
        
        n = len(grid)       # Rows
        m = len(grid[0])    # Cols

        # Make the first row filled with path XOR's
        for i in range(1, m):
            row.append( grid[0][i] ^ row[-1] )

        # Convert the elements to sets
        row = [{i} for i in row]

        # Going through each row
        for i in range(1, n):
            left = {}
            tmp_row = []

            for j in range(m):
                tmp_set = set()
                
                cur = grid[i][j]
                row[j].update(left) # Extend the set of XOR's above with the ones on the left
                
                for k in row[j]:
                    tmp_set.add(k ^ cur)
                
                tmp_row.append(tmp_set)
                left = tmp_set

            row = tmp_row

        return min(row[-1])
