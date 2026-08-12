class Solution:
    def isValid(self, s: str) -> bool:
        maper = {")":"(","]":"[","}":"{"}
        stack = []
        for i in s:
            if i in maper:
                if not stack:
                    return False
                if stack[-1] == maper[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return False if stack else True