class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ans = []
        for idx, i in enumerate(nums):
            if i == target:
                ans.append(idx)

        return ans
