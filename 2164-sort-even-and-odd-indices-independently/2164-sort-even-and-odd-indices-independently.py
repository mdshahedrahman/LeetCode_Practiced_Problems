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