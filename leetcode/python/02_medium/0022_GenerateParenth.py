class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 1:
            return ['()']

        ans = set()

        def helper(stack, opened, depth):
            if depth == n:
                ans.add("".join(stack + ([')'] * opened)))
                return

            helper(stack + ['('], opened+1, depth+1)

            for i in range(1, opened+1):
                helper(stack + ([')']*i), opened-i, depth)

        helper([], 0, 0)

        return list(ans)
