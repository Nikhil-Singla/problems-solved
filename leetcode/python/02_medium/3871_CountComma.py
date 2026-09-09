class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        digits_processed = 1000
        count = 0

        while digits_processed <= n:
            count += n - digits_processed + 1
            digits_processed *= 1000

        return count
