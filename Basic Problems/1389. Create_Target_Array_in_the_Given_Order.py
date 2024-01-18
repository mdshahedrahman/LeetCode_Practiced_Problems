from typing import List
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []

        for i, idx in enumerate(index):
            result.insert(idx, nums[i])

        return result 