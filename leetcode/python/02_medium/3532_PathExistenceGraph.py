class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        if n <= 1:
            return [True] * len(queries)
        
        node_groups = [0] * n
        curr_group = 0

        prev = nums[0]
        for idx, i in enumerate(nums[1:], start=1):
            if i - prev > maxDiff:
                curr_group += 1
            
            prev = i
            node_groups[idx] = curr_group
        
        ans = []
        for i, j in queries:
            ans.append(node_groups[i] == node_groups[j])

        return ans
