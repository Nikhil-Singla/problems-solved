class Solution:
    def minOperations(self, s: str) -> int:
        ans = sorted(s)
                
        if s == "".join(ans):
            return 0
        
        small, large = min(s), max(s)
        test = set([small, large])

        if len(s) == 2:
            return -1

        if small == s[0] or large == s[-1]:
            return 1

        for i in s[1:-1]:
            if i in test:
                return 2
            
        return 3
