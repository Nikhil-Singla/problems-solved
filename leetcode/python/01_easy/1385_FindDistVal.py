class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        distval = 0
        
        for i in arr1:
            x = bisect.bisect_left(arr2, i)

            if (x == len(arr2) or abs(i - arr2[x]) > d) and (x == 0 or abs(i - arr2[x - 1]) > d):
                    distval += 1

        return distval
