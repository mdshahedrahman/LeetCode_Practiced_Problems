from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        array = []

        # Compare adjacent elements and append to the array if equal
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
                array.append(nums[i])
            else:
                array.append(nums[i])

        array.append(nums[-1])
        array = [x for x in array if x != 0] + [0] * array.count(0)

        return array

# Example usage:
solution = Solution()
nums = [1, 2, 2, 1, 1, 0]
result = solution.applyOperations(nums)
print("Result:", result)
