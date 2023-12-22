from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
        return len(nums)

# Example usage:
solution = Solution()
nums = [3, 2, 2, 3]
val = 3

output_length = solution.removeElement(nums, val)

print("Modified Array:", nums[:output_length])
