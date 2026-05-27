class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        START = 1
        LOWER = 2
        UPPER = 3

        ascii_a = 97
        ascii_A = 65

        alpha = [START] * 26

        for i in word:
            letter = ord(i)
            truth = i.islower()
            idx = (letter-ascii_a if truth else letter-ascii_A)
            state = LOWER if truth else UPPER

            if alpha[idx] != False and (0 <= state-alpha[idx] <= 1):
                alpha[idx] = state
            else:
                alpha[idx] = False
        
        return alpha.count(UPPER)
