class Solution:
    def checkString(self, s: str) -> bool:
        start = s.find("b")
        last = s.rfind("a")

        return (start == -1) or (last == -1) or (last < start)
