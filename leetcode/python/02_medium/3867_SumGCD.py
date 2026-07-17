class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = nums[0]
        prefixGCD = [mx]

        for i in nums[1:]:
            if i > mx:
                mx = i
                prefixGCD.append(i)
            else:
                prefixGCD.append(math.gcd(mx, i))

        prefixGCD.sort()
        
        n = len(prefixGCD)
        summate = 0
        for i in range(n//2):
            summate += math.gcd(prefixGCD[i], prefixGCD[n-1-i])

        return summate
