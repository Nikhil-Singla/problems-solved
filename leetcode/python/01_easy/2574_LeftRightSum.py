class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lSum = 0
        rSum = sum(nums)
        n = len(nums)
        ans = [0] * n
        for idx, i in enumerate(nums):
            rSum -= i
            ans[idx] = abs(lSum - rSum)
            lSum += i

        return ans
