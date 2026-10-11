class Solution:
    def expand(self, s: str) -> List[str]:
        options = []
        i = 0
        while i < len(s):
            if s[i].isalpha():
                options.append([s[i]])
            else:
                i += 1
                temp = []
                while s[i] != "}":
                    if s[i] == ",":
                        i += 1
                        continue
                    temp.append(s[i])
                    i += 1
                options.append(temp)
            i += 1
        res = []
        def dfs(i,curr):
            if len(curr) == len(options):
                res.append("".join(curr))
            if i == len(options):
                return 
            for child in options[i]:
                dfs(i + 1,curr + [child])
        dfs(0,[])
        return res 