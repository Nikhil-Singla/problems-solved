class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = sorted(set(arr))
        converted = {k:i for i, k in enumerate(ranks)}

        for i, k in enumerate(arr):
            arr[i] = converted[k] + 1

        return arr
