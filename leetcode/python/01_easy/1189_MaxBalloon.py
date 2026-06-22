class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word_list = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}

        for i in text:
            if i in word_list:
                word_list[i] += 1

        word_list['l'] //= 2
        word_list['o'] //= 2
        
        return min(word_list.values())
