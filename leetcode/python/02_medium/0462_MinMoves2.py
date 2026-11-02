class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums) // 2
        median = sorted(nums)[n]
        
        return sum([abs(i-median) for i in nums])
