class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
# Count occurrences in each array
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

# Find the common elements considering duplicates
        common_elements = (counter1 & counter2).elements()

# Convert the result to a list
        common_elements_list = list(common_elements)

        return common_elements_list