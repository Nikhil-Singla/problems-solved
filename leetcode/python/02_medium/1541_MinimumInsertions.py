class Solution:
    def minInsertions(self, s: str) -> int:
        closed_brackets = 0
        added = 0
        
        for i in s[::-1]:
            if i == ")":
                closed_brackets += 1

            if i == "(":
                if closed_brackets%2 == 1:
                    closed_brackets += 1
                    added += 1

                closed_brackets -= 2
                if closed_brackets < 0:
                    added += 2
                    closed_brackets = 0

        if closed_brackets%2 == 1:
            closed_brackets += 1
            added += 1

        return (added + (closed_brackets//2))
