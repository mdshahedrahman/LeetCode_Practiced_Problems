from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                # If we reach the end of the array, add the current permutation
                result.append(nums.copy())
                return

            # Keep track of used elements to avoid duplicates
            used = set()

            for i in range(start, len(nums)):
                # Skip if the element is already used
                if nums[i] in used:
                    continue

                # Swap the current element with the element at the start index
                nums[start], nums[i] = nums[i], nums[start]

                # Recursively generate permutations for the rest of the array
                backtrack(start + 1)

                # Backtrack to restore the original order for the next iteration
                nums[start], nums[i] = nums[i], nums[start]

                # Mark the current element as used
                used.add(nums[i])

        result = []
        backtrack(0)
        return result

# Example usage:
solution_instance = Solution()
array = [1, 1, 2]
permutations = solution_instance.permuteUnique(array)
print(permutations)
