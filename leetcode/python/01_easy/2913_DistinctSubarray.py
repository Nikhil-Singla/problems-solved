class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        all_sets = [ {i} for i in nums ]
        ret_val = n = len(nums)

        for i in range(1, n):
            for j in range(i, n):
                all_sets[j-i].add(nums[j])
                ret_val += len(all_sets[j-i])**2

        return ret_val
