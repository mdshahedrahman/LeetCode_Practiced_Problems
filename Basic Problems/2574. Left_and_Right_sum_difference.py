from typing import List
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        temp_1 = []
        temp_2 = []
        temp_3 = []

        sum_left = 0
        sum_right = 0

        for i in nums:
            temp_1.append(sum_left)
            sum_left = sum_left + i

        for i in range(len(nums)):
            temp_2.append(sum_right)
            sum_right = sum_right + nums[-(i+1)]
        temp_2.reverse()

        for i in range(len(nums)):
            k = abs(temp_1[i] - temp_2[i])
            temp_3.append(k)

        return temp_3