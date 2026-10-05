class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count = 0
        stack = []

        for i in s:
            if i == "(":
                stack.append(i)

            elif i == ")":  # Assume always balanced parentheses

                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)

                    while(len(stack) > 1 and stack[-2] != '('):
                        i, j = stack.pop(), stack.pop()
                        stack.append(i+j)

                else:
                    num = stack.pop() * 2
                    stack.pop() # Gets rid of the bracket
                    stack.append(num)

                    while(len(stack) > 1 and stack[-2] != '('):
                        i, j = stack.pop(), stack.pop()
                        stack.append(i+j)


        return stack[0]
