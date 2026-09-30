class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        count = 0
        ans = []
        for i in seq:
            if i == "(":
                count += 1
                ans.append(0 if count%2 == 0 else 1)
            else:
                ans.append(0 if count%2 == 0 else 1)
                count -= 1

        return ans
