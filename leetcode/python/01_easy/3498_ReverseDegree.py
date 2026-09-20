class Solution:
    def reverseDegree(self, s: str) -> int:
        pos = 1
        alphabet = { chr(97 + (26 - value)):value for value in range(26, 0, -1)}

        ans = 0
        for i in s:
            ans += pos * alphabet[i]
            pos += 1

        return ans
