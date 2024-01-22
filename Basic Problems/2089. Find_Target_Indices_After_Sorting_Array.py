from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        temp = []

        nums_sorted = sorted(nums)
        print(nums_sorted)

        for i in range(len(nums_sorted)):
            if nums_sorted[i] == target:
                temp.append(i)

        return temp
