class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum = 0
        ret = 0
        for i in gain:
            sum += i
            ret = max(ret, sum)

        return ret
