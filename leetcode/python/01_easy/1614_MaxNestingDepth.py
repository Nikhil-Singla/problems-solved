class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        ret = 0
        for i in s:
            if i == '(':
                depth += 1
                ret = max(ret, depth)
            elif i == ')':
                depth -= 1

        return ret
