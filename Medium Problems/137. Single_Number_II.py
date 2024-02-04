from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        element_count = {}
        for element in nums:
            if element in element_count:
                element_count[element] += 1
            else:
                element_count[element] = 1

        # Find the element that appears only once
        for element, count in element_count.items():
            if count == 1:
                return element

# Example usage:
solution = Solution()
nums = [4, 3, 4, 1, 3]
result = solution.singleNumber(nums)
print(result)
