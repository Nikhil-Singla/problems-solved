class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        counter = 0
        for i in range(0, n-1, 2):
            if s[i] != s[i+1]:
                counter += 1

        return counter
