from typing import List
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def digit_sum(num):
            return sum(int(digit) for digit in str(num))
            # Calculate the digit sum for each element in the array

        digit_sums = [digit_sum(element) for element in nums]

        # Calculate the sum of all elements in the array
        element_sum = sum(nums)

        result = abs(element_sum - sum(digit_sums))

        return result