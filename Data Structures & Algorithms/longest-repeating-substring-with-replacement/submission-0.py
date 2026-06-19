class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            print(curr)
            curr[s[r]] += 1
            if ((r-l) + 1) - max(curr.values()) > k:
                curr[s[l]] -= 1
                l += 1 
            res = max((r - l) + 1, res)
            print(curr,res)
        return res