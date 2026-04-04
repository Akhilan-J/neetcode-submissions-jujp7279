from functools import lru_cache
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        summ = sum(stones)
        target = summ//2
        @lru_cache(None)
        def dfs(i,curr):
            if curr == target:
                return abs(summ - 2 * curr)
            if i == len(stones):
                return abs(summ - 2 * curr)
            if curr > target:
                return float('inf')
            
            return min(dfs(i+1,curr+stones[i]),dfs(i+1,curr))
        return dfs(0,0)
            