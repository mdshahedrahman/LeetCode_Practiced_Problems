class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        list_nums1 = sorted(list(set_nums1))
        list_nums2 = sorted(list(set_nums2))

        common_elements = set_nums1.intersection(set_nums2)

        common_elements_1 = sorted(list(common_elements))

        return list(common_elements)