class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)

        if target not in sorted_nums:
            return -1 
        else:
            indices = sorted_nums.index(target)
            return indices
