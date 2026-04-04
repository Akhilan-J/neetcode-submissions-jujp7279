class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ser = set(nums)
        return not len(nums) == len(ser)