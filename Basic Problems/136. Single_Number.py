from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_set = set()

        for num in nums:
            if num in seen_set:
                seen_set.remove(num)
            else:
                seen_set.add(num)

        return seen_set.pop()