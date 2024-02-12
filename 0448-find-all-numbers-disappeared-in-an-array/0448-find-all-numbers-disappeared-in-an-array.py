from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Initialize an array to mark visited numbers
        visited = [False] * (len(nums) + 1)
        
        # Mark visited numbers based on the elements in nums
        for num in nums:
            visited[num] = True

        # Find numbers that were not visited
        disappeared_numbers = [i for i in range(1, len(nums) + 1) if not visited[i]]

        return disappeared_numbers
