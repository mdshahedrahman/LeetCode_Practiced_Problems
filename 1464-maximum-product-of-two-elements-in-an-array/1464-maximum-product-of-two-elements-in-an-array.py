#from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        k = len(nums) - 1
        
        return ((nums[k]-1) * (nums[k-1]-1))