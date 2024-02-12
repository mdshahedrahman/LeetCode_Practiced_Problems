class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        # Initialize an empty list to store the result
        result = []

        # Iterate through each element in the array
        for number in nums:
            # Convert the element to a string
            num_str = str(number)

            # Convert each digit back to an integer and extend the result list
            digits = [int(digit) for digit in num_str]
            result.extend(digits)

        return result