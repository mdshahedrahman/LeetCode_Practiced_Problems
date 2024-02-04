from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sums = []

        for row in accounts:
            row_sum = sum(row)
            sums.append(row_sum)

        return  max(sums)