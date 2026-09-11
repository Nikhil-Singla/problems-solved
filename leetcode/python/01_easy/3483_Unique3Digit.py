class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = Counter(digits)
        evens = {0, 2, 4, 6, 8}
        ret = 0
        for i in range(0, 10):
            for j in range(1, 10):
                for k in evens:

                    if count[i] > 0:
                        count[i] -= 1
                    else:
                        continue

                    if count[j] > 0:
                        count[j] -= 1
                    else:
                        count[i] += 1
                        continue

                    if count[k] > 0:
                        count[k] -= 1
                    else:
                        count[i] += 1
                        count[j] += 1
                        continue

                    ret += 1
                    count[i] += 1
                    count[j] += 1
                    count[k] += 1

        return ret
