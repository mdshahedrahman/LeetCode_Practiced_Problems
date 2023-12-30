class Solution:
    def countDigits(self, num: int) -> int:
        str_number = str(num)

        # Split the string into a list of characters
        digits = [int(digit) for digit in str_number]

        counter = 0

        for i in digits:
            if num % i == 0:
                counter = counter + 1

        return counter