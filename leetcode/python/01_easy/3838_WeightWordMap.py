class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        start = ord('a')
        ans = []
        for i in words:
            weight_word = 0
            for letter in i:
                weight_word += weights[ord(letter) - start]

            weight_word %= 26
            ans.append(chr(25-weight_word + start))

        return ''.join(ans)
