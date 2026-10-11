class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        adder = 0
        n = len(nums)
        for idx, i in enumerate(nums, start=1):
            if n % idx == 0:
                adder += i*i

        return adder
