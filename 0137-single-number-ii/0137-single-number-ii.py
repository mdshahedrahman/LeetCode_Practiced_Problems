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