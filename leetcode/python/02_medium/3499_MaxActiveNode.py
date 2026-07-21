class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # s = "100100110011110110"
        # convert = 1 1 00 1 00 11 00 1111 0 11 0 1
        n = len(s)
        idx = 1
        cur = s[0]
        count = 1
        partition = [('1', 0)]

        while idx < n:
            if s[idx] == cur:
                count += 1
            else:
                partition.append(
                    (cur, count)
                )

                cur = s[idx]
                count = 1

            idx += 1

        partition.append((cur, count))
        partition.append(('1', 0))

        m = len(partition)
        idx = 1
        best_trade = 0
        
        while idx < m-1:
            if partition[idx][0] == '1' and partition[idx-1][0] == '0' and partition[idx+1][0] == '0':
                best_trade = max(partition[idx-1][1] + partition[idx+1][1], best_trade)

            idx += 1

        return s.count('1') + best_trade
