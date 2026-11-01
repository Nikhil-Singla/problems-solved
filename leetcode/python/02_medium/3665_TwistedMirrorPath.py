class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        MOD = 10**9 + 7
        DOWN = -1
        RIGHT = 1
        
        adder = {DOWN: [0, 1], RIGHT: [1, 0]}

        dp = [[0 for i in range(cols)] for j in range(rows)]

        @cache
        def helper(xcor, ycor, direct):
            if xcor >= rows or ycor >= cols:
                return 0

            if xcor == rows-1 and ycor == cols-1:
                return 1

            if grid[xcor][ycor] == 1:
                direct *= -1 
                dx, dy = adder[direct]
                dp[xcor][ycor] = helper(xcor+dx, ycor+dy, direct)
            
            else:
                dx1, dy1 = adder[direct]
                dx2, dy2 = adder[direct*-1]

                dp[xcor][ycor] = helper(xcor+dx1, ycor+dy1, direct)% MOD + helper(xcor+dx2, ycor+dy2, (direct*-1))% MOD

            return dp[xcor][ycor] % MOD

        return helper(0, 0, DOWN) % MOD
