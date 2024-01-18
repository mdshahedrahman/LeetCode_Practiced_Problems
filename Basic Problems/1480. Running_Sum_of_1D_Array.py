from typing import List
import string

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        temp = []

        for i in nums:
            sum = sum + i
            temp.append(sum)

        return temp