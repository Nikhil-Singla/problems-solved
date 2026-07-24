class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        nums = set(nums)
        pairs_xor = set()
        
        for i in nums:
            for j in nums:
                pairs_xor.add(i ^ j)

        triple_xor = set()

        for i in pairs_xor:
            for j in nums:
                triple_xor.add(i ^ j)

        return len(triple_xor)
