class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # stairs [0, 1, 2, 3, 4, 5, 6]
        # costs starting from step 1 = [5, 1, 6, 2, 9, 8, 3]
        # costs at 0, 1, 2, 3 = [0, 5, 1, ]   costs[target] + [targetindex-startindex]**2
        # target and start index are 1-indexed in the array.

        dp = [0] * (n+1)

        for idx, targetcost in enumerate(costs, start=1):
            dp[idx] = targetcost + min(
                           k**2 + dp[idx-k] 
                           for k in (1, 2, 3) if idx-k >= 0
                        # [
                        #     (1)**2 + dp[idx-1],
                        #     (2)**2 + dp[idx-2],
                        #     (3)**2 + dp[idx-3]
                        # ]
                        )

        return dp[-1]
