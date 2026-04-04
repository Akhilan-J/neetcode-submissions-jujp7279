from functools import lru_cache
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        res = []
        words = set(dictionary)
        @lru_cache
        def dfs(i):
            if i == len(s):
                return 0
            
            res = 1 + dfs(i+1)
            for word in words:
                if s[i:i + len(word)] == word:
                    res = min(res,dfs(0+i +len(word)))
            return res
        return dfs(0)