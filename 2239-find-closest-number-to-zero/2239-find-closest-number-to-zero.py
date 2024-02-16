class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_num = None
        min_abs_diff = float('inf')  # Initialize with positive infinity

        for num in nums:
            abs_diff = abs(num)
            if abs_diff < min_abs_diff or (abs_diff == min_abs_diff and num > 0):
                min_abs_diff = abs_diff
                closest_num = num

        return closest_num

    