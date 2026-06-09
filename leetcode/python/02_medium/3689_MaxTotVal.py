class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        small = min(nums)
        large = max(nums)

        return (large - small) * k
