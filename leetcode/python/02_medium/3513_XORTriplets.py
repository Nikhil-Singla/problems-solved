class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # XOR with itself gives 0, and then XOR with 0 gives the number itself.
        # So at least 1-N would be inclusive in the XOR, and if n > 3, also 0,
        # With powers of 2, all the numbers can be made, below the outermost bit possible.

        n = len(nums)
        if n <= 2:
            return n
        else:
            return int(math.pow(2, (math.floor(math.log2(n))+1)))
