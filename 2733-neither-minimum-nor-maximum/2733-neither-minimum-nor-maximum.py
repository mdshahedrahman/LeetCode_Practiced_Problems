class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        for element in nums:
            if element > min(nums) and element < max(nums):
                return element
                break
        return -1
        