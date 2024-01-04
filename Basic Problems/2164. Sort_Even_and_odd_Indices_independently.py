from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        temp_odd = []
        temp_even = []
        temp_final = []
        result = []

        for index, value in enumerate(nums):
            if index % 2 == 0:
                temp_even.append(value)
            else:
                temp_odd.append(value)

        sorted_temp_odd = sorted(temp_odd, reverse=True)
        sorted_temp_even = sorted(temp_even)
        temp_final = [0] * len(nums)

        temp_final[::2] = sorted_temp_even
        temp_final[1::2] = sorted_temp_odd

        return temp_final

# Test
solution = Solution()
nums = [36, 45, 32, 31, 15, 41, 9, 46, 36, 6, 15, 16, 33, 26, 27, 31, 44, 34]
output = solution.sortEvenOdd(nums)
print(output)
