class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 1:
            return ['()']

        ans = []

        def helper(stack, opened_brackets, total_brackets):
            if len(stack) == 2*n:
                ans.append("".join(stack))                
                return

            if total_brackets < n:
                helper(stack + ['('], opened_brackets+1, total_brackets+1)

            if opened_brackets > 0:
                helper(stack + [')'], opened_brackets-1, total_brackets)

        helper([], 0, 0)

        return ans
