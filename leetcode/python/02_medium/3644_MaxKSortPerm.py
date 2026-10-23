class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        expected = sorted(nums)
        ans = None

        for i, j in zip(nums, expected):
            if i != j:
                if ans is None:
                    ans = i
                else:
                    ans = ans & i

        return ans if ans else 0
