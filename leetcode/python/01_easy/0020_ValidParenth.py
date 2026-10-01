class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        inputs = {'(', '[', '{'}
        pair_corresponding_to_closer = {
                                            ')': '(', 
                                            ']': '[', 
                                            '}': '{'
                                         }
        
        for i in s:
            if i in inputs:
                stack.append(i)
            else:
                if not stack:
                    return False

                closer = stack.pop()
                if pair_corresponding_to_closer[i] != closer:
                    return False

        return stack == []
