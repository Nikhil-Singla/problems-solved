class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return True

        count = 0
        added = 0

        for i in s:
            count += (1 if i == "(" else -1)

            if count < 0:
                added -= count
                count = 0

        return (count + added)
