class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ret = 0
        
        prefixes = set()
        for i in arr1:
            temp = i
            while temp:
                prefixes.add(temp)
                temp //= 10
        
        for i in arr2:
            temp = i
            while temp:
                if temp <= ret:
                    break
                elif temp in prefixes:
                    ret = max(ret, temp)
                    break
                else:
                    temp //= 10

        return 0 if ret == 0 else len(str(ret))
