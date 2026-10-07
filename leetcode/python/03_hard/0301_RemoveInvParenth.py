class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        open_counter = 0
        
        # timeCounterWentBelowZero = 0
        tcwbz = 0

        for i in s:
            if i == "(":
                open_counter += 1
            elif i == ")":
                open_counter -= 1

            if open_counter < 0:
                tcwbz += 1 # Totally extra redundancy check
                open_counter = 0

        ans = set()

        def helper(index, open_brackets, closed_brackets, max_open_remove, max_close_remove, expression):
            if index == len(s):
                if max_open_remove == 0 and max_close_remove == 0:
                    tmp = "".join(expression)
                    ans.add(tmp)
            else:
                element = s[index]

                if (element == "("):
                    helper(index+1, open_brackets+1, closed_brackets, max_open_remove, max_close_remove, expression + ["("])
                    
                    if (max_open_remove > 0):
                        helper(index+1, open_brackets, closed_brackets, max_open_remove-1, max_close_remove, expression)
                    

                elif (element == ")"):
                    if (open_brackets > closed_brackets):
                        helper(index+1, open_brackets, closed_brackets+1, max_open_remove, max_close_remove, expression + [")"])

                    if (max_close_remove > 0):
                        helper(index+1, open_brackets, closed_brackets, max_open_remove, max_close_remove-1, expression)

                else:
                    helper(index+1, open_brackets, closed_brackets, max_open_remove, max_close_remove, expression+[element])

        helper(0, 0, 0, open_counter, tcwbz, [])
        return list(ans)
