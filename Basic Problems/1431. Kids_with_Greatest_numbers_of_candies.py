from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        sum = 0
        temp = []

        for i in candies:
            sum = i + extraCandies
            if sum >= max_candies:
                temp.append(True)
            else: temp.append(False)


        return temp