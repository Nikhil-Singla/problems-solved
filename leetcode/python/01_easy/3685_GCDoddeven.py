class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # Sum of even numbers = n * n+1
        # Sum of odd numbers = n**2

        return math.gcd(n*(n+1), n**2)
