class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = 1
        decreasing = 1
        retval = 1
        prev = nums[0]

        for i in nums[1:]:
            if i > prev:
                increasing += 1
                decreasing = 1
            elif i < prev:
                decreasing += 1
                increasing = 1
            else:
                increasing = decreasing = 1

            retval = max(retval, increasing, decreasing)
            prev = i

        return retval
