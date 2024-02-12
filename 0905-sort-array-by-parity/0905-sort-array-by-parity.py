from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        temp1 = []
        temp2 = []
        final_temp = []

        for i in nums:
            if i % 2 == 0:
                temp1.append(i)
            else:
                temp2.append(i)

        final_temp = temp1 + temp2

        return final_temp
