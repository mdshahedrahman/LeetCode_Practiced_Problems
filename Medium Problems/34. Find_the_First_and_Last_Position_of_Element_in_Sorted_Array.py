from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        temp = []

        nums_sorted = sorted(nums)

        for i in range(len(nums_sorted)):
            if nums_sorted[i] == target:
                temp.append(i)

        result = []
        if temp:
            result.extend([temp[0], temp[-1]])
            return result

        else:
            return [-1, -1]
