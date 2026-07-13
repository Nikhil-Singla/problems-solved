class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        length = len(str(low))
        max_len = len(str(high))
        ans = []
        for i in range(length, max_len+1):
            for j in range(1, 11-i):
                num = 0
                for k in range(i):
                    num *= 10
                    num += j + k

                if num > high:
                    break
                if num >= low:
                    ans.append(num)
        
        return ans
