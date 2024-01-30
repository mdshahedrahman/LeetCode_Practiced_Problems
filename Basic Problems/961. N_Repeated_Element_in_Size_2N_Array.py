from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        def count_occurrences(arr):
            element_counts = {}
            for element in arr:
                if element in element_counts:
                    element_counts[element] += 1
                else:
                    element_counts[element] = 1
            return element_counts

        def find_majority_element(arr):
            occurrences = count_occurrences(arr)
            length = len(arr)
            threshold = length // 2

            for element, count in occurrences.items():
                if count >= threshold:
                    return element

            return -1

        return find_majority_element(nums)

# Example usage:
solution = Solution()
result = solution.repeatedNTimes([1, 2, 3, 3])
print(result)
