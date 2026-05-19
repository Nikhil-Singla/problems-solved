class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[-1] < nums2[0]:
            return -1
        if nums2[-1] < nums1[0]:
            return -1

        n, m = len(nums1), len(nums2)
        idx1, idx2 = 0, 0

        while (idx1 < n) and (idx2 < m):
            if nums1[idx1] == nums2[idx2]:
                return nums1[idx1]
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        
        return -1
