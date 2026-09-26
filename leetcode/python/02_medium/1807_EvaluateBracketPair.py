class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        up_know = defaultdict(lambda: '?')

        for i in knowledge:
            up_know[i[0]] = i[1]

        idx = 0
        n = len(s)
        adder = None
        ans = []

        while(idx < n):
            if s[idx] == "(":
                start = idx + 1
                
                while s[idx] != ")":
                    idx += 1
                
                end = idx
                key = s[start:end]
                adder = up_know[key]
        
            if adder:
                ans.append(adder)
                adder = None
            else:
                ans.append(s[idx])

            idx += 1

        return "".join(ans)
