from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        total_distance = 0

        # Iterate through each bit position
        for i in range(32):  # Assuming integers are 32-bit in Python
            count_set_bits = sum(((num >> i) & 1) for num in nums)
            count_unset_bits = n - count_set_bits
            total_distance += count_set_bits * count_unset_bits

        return total_distance
