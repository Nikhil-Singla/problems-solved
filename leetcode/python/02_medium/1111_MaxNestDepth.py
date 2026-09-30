class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        count = 0
        depth_array = []
        for i in seq:
            if i == "(":
                count += 1
                depth_array.append(count)
            else:
                depth_array.append(count)
                count -= 1

        ans = []
        for i in depth_array:
            if i % 2 == 0:
                ans.append(0)
            else:
                ans.append(1)

        return ans
