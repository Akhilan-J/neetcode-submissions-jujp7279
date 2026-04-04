class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mini = 1
        while mini in nums:
            mini += 1
        return mini 