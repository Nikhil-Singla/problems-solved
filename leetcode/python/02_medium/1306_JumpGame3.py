class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        front = set([start])
        visited = set()
        n = len(arr)
        while front:
            top = front.pop()
            if top in visited:
                continue

            visited.add(top)
            if arr[top] == 0:
                return True
    
            first_jump = top + arr[top]
            second_jump = top - arr[top]

            if 0 <= first_jump < n:
                front.add(first_jump)
            
            if 0 <= second_jump < n:
                front.add(second_jump)
        
        return False
