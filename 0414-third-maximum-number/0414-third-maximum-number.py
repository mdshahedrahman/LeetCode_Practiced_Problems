class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Sort the array in descending order
        sorted_arr = sorted(set(nums), reverse=True)

        # Pop the third-largest number
        if len(sorted_arr) >= 3:
            third_largest = sorted_arr.pop(2)
            print("Original array:", nums)
            print("Array after popping the third-largest number:", sorted_arr)
            return third_largest
        elif len(sorted_arr) <= 2:
            third_largest = sorted_arr.pop(0)
            return third_largest
        else:
            third_largest = sorted_arr.pop(0)
            return third_largest
        