class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        # first = (n+1) // 2
        # second = n - first
        first = 0
        last = n-1

        nums.sort(key=abs, reverse=True)
        ret = 0
        while(first < last):
            ret += (nums[first]**2) - (nums[last]**2)
            
            first += 1
            last -= 1

        if first == last:
            ret += nums[first]**2

        return ret
