class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        absolute = [abs(i - j) for i, j in zip(nums1, nums2)]
        k = k1 + k2
        
        if sum(absolute) <= k:
            return 0

        absolute.sort(reverse=True)
        absolute.append(0)

        n = len(absolute)
        
        for i in range(1, n):
            diff = (absolute[i-1] - absolute[i]) * i
            if diff > k:
                quotient = k // i
                remainder = k % i

                shaved = absolute[i-1] - quotient
                values = (i - remainder)*(shaved**2) + (remainder * (shaved - 1)**2) + sum(x*x for x in absolute[i:])
                return values

            k -= diff

        return 0
