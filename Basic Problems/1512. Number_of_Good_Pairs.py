from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter =0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums [i] == nums [j]:
                    counter = counter + 1

        return counter