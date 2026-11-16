class Solution:
    def digitSum(self, s: str, k: int) -> str:
        digits = list(map(int, list(s)))

        while(len(digits) > k):
            tmp = 0
            newdigit = []
            while(tmp < len(digits)):
                newdigit.extend(map(int, list(str(sum(digits[tmp:tmp+k])))))
                tmp += k

            digits = newdigit

        return "".join(list(map(str, digits)))
