class Solution:
    def findGCD(self, nums: List[int]) -> int:
        low = high = nums[0]

        for i in nums:
            if i < low:
                low = i
            
            if i > high:
                high = i

        while (low != 0):
            prev = low
            high, low = low, (high % low)

        return prev
