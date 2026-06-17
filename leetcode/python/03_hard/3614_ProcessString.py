from collections import deque

class Solution:
    def processStr(self, s: str, k: int) -> str:
        ans = 0

        for i in s:
            if i == '*':
                if ans > 0: ans -= 1
            
            elif i == '#':
                ans *= 2

            elif i == '%':
                continue

            else:
                ans += 1

        if ans <= k:
            return '.'
        
        for i in reversed(s):
            if i == '*':
                ans += 1
            
            elif i == '#':
                ans //= 2
                if k >= ans:
                    k -= ans

            elif i == '%':
                k = ans - k - 1

            else:
                if k+1 == ans:
                    return i
                ans -= 1

    
        return "."
