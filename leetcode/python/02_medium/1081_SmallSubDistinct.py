class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_pos = [0] * 26
        ms = [] # Mono Stack
        contained = set()

        for idx, i in enumerate(s):
            last_pos[ord(i) - ord('a')] = idx

        for idx, i in enumerate(s):
            if i in contained:
                continue

            while (ms) and (i < ms[-1]) and (last_pos[ord(ms[-1]) - ord('a')] > idx):
                contained.remove(ms.pop())

            ms.append(i)
            contained.add(i)

        return "".join(ms)
