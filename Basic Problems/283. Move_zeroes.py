from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Count the number of zeroes
        count_zeros = nums.count(0)

        # Remove all occurrences of zero from the list
        nums[:] = [x for x in nums if x != 0]

        # Append the counted number of zeroes to the end
        nums += [0] * count_zeros

# Example usage:
solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)

print("Modified List:", nums)
