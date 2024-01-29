from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Initialize an array to mark visited numbers
        visited = [0] * (len(nums) + 1)

        # Mark visited numbers based on the elements in nums
        for num in nums:
            visited[num] += 1

        # Find numbers that were visited more than once
        duplicates = [i for i in range(1, len(nums) + 1) if visited[i] == 2]

        return duplicates
