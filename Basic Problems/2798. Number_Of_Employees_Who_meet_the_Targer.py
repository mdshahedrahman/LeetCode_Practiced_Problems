from typing import List
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        counter = 0

        for i in hours:
            if i >= target:
                counter = counter + 1

        return counter