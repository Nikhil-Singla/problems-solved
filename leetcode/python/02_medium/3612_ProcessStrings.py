class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for i in s:
            if i == '*': 
                if result:
                    result.pop()
            elif i == '#':
                result = result * 2
            elif i == '%':
                result.reverse()
            else:
                result.append(i)

        return "".join(result)
