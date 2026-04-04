class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        running = 1
        hashm = defaultdict(int)
        res = 0

        for i in nums:
            running *= i
            if running < k :
                res += 1
                for key,val in hashm.items():
                    if running // key < k :
                        res += val
            else:
                for key,val in hashm.items():
                    if running // key < k :
                        res += val
            hashm[running] += 1
        print(hashm)
        return res