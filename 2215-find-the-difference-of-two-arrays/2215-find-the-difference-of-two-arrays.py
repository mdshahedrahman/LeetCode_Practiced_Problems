class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Count occurrences of each element in both lists
        count_nums1 = Counter(nums1)
        count_nums2 = Counter(nums2)

        # Find the common elements
        common_elements = count_nums1 & count_nums2

        # Extract the elements and their counts
        common_elements_list = list(common_elements.elements())

        # Remove common elements from nums1 and nums2
        nums1 = [num for num in nums1 if num not in common_elements_list]
        nums2 = [num for num in nums2 if num not in common_elements_list]

        # Remove duplicates
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        return [nums1, nums2]