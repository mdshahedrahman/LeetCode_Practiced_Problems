class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.square_sum_of_digits(n)

        return n == 1

    def square_sum_of_digits(self, number):
        # Convert the number to a string
        number_str = str(number)

        # Calculate the square of each digit and return their sum
        square_sum = sum(int(char) ** 2 for char in number_str)

        return square_sum