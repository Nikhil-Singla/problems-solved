class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = deque()
        stack = []

        for idx, i in enumerate(s):
            if i == "*":
                stars.append(idx)

            elif i == "(":
                stack.append(idx)

            elif i == ")":
                if stack:
                    stack.pop()
                elif stars:
                    stars.popleft()
                else:
                    return False

        while stack and stars:
            if stars[-1] > stack[-1]:
                stack.pop()
                stars.pop()
            else:
                return False

        return not stack
