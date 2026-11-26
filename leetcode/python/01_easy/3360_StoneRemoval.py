class Solution:
    def canAliceWin(self, n: int) -> bool:
        is_AliceTurn = True 
        cnt = 10
        while(cnt <= n):
            n -= cnt
            cnt -= 1
            is_AliceTurn = not is_AliceTurn

        if is_AliceTurn:
            return False
        else:
            return True
