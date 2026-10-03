class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ret = 0
        for idx, i in enumerate(s):
            if i == "(":
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    last = stack[-1]
                    length = idx - last
                    ret = max(ret, length)

        return ret
