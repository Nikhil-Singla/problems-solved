class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if costBoth > cost1+cost2:
            costBoth = cost1+cost2

        if costBoth < cost1:
            cost1 = costBoth
        
        if costBoth < cost2:
            cost2 = costBoth

        lesser = min(need1, need2)
        start = (lesser * costBoth) + ((need1-lesser)*cost1) + ((need2-lesser)*cost2)
        return start
