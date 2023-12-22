from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

# Example usage:
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution = Solution()
output = solution.removeDuplicates(nums)

print("Modified List:", nums)
print("Count of elements:", output)
