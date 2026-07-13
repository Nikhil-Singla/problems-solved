class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        start = list(range(1,10))
        curr_num = 2
        ans = set()
        while(curr_num < 10):
            for i in range(9):
                if i + curr_num > 9:
                    break
                start[i] *= 10
                start[i] += i + curr_num

            for i in start:
                if low <= i <= high:
                    ans.add(i)
            
            curr_num += 1

        return sorted(list(ans))
