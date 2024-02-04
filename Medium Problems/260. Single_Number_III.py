from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        element_count = {}
        for element in nums:
            if element in element_count:
                element_count[element] += 1
            else:
                element_count[element] = 1

        # Filter elements that appear only once
        unique_elements = [element for element, count in element_count.items() if count == 1]

        return unique_elements