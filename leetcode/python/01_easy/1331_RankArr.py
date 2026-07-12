class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = sorted(set(arr))
        converted = {k:i for i, k in enumerate(ranks)}

        return [converted[k]+1 for k in arr]
