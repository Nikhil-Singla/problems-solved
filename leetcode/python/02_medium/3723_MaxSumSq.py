class Solution:
    def maxSumOfSquares(self, num: int, goal: int) -> str:
        digits = 0
        ans = []

        if goal > num*9:
            return ""

        while (goal - 9) > 0:
            goal -= 9
            digits += 1
            ans.append("9")

        digits += 1
        ans.append(str(goal))
        
        cap = ["0"] * (num-digits)
        ans.extend(cap)
        return "".join(ans)
