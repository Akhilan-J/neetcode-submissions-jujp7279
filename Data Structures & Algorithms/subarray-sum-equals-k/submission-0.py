class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashm = defaultdict(int)
        run = 0
        hashm[0] = 1
        res = 0
        for i in nums:
            run += i
            compliment = run - k
            if compliment in hashm:
                res += hashm[compliment]
            hashm[run] += 1
        return res