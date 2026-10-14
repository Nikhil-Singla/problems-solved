class Solution:
    def maxSumOfSquares(self, num: int, goal: int) -> str:
        if goal > num*9:
            return ""

        start = goal // 9
        left = goal % 9

        ans = (["9"] * start) + ([str(left)] if left else [""]) + (["0"] * ((num-start-1) if left else (num-start))) 
        return "".join(ans)
