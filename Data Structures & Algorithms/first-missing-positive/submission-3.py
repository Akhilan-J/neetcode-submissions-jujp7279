class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ser = set(nums)
        mini = 1
        while mini in ser:
            mini += 1
        return mini 