class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            index_of_element = nums.index(target)
            return index_of_element
        
        else:
            nums.append(target)
            new_nums = sorted(nums)
            index_of_element1 = new_nums.index(target)
            return index_of_element1