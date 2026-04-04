from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        @lru_cache(None)
        def dp(i):
            if i == len(s):
                return True
            for j in range(i,len(s)):
                trial = s[i:j+1]
                if trial in words and dp(j+1):
                    return True
            return False
        return dp(0)