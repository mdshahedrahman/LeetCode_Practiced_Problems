class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        count_odd = 0
        count_even = 0

        for i in sorted_nums:
            if i < 0:
                count_odd = count_odd + 1
            elif i > 0:
                count_even = count_even + 1

        max_odd_even = max(count_even, count_odd)

        return max_odd_even