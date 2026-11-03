class Solution:
    def minMoves(self, nums: List[int]) -> int:
        high = max(nums)
        return sum([high-i for i in nums])
