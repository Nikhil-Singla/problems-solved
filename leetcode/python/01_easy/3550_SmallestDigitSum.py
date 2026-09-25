class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for idx, i in enumerate(nums):
            a = sum(map(int, list(str(i))))
                        
            if a == idx:
                return idx

        return -1
