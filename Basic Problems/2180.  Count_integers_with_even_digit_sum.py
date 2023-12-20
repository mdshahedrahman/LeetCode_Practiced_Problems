class Solution:
    def countEven(self, num: int) -> int:
        def digit_sum(num):
            return sum(int(digit) for digit in str(num))



# Calculate digit sums for each number in the range from 1 to num (inclusive)
        all_digit_sums = [digit_sum(i) for i in range(1, num + 1)]

# Filter the digit sums that are divisible by 2
        even_digit_sums = [digit_sum(i) for i in range(1, num + 1) if digit_sum(i) % 2 == 0]

# Count the number of digit sums that meet the specified condition
        count_even_digit_sums = len(even_digit_sums)

        return count_even_digit_sums