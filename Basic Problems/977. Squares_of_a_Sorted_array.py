from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp = []

        for i in nums:
            mul = 0
            mul = i * i
            temp.append(mul)

        sorted_temp = sorted(temp)

        return sorted_temp