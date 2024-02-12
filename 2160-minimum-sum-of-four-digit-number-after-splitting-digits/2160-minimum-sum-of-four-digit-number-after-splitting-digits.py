class Solution:
    def minimumSum(self, num: int) -> int:
        sorted_digits = [int(digit) for digit in sorted(str(num))]

        digit_pairs = [(sorted_digits[i], sorted_digits[-(i + 1)]) for i in range(len(sorted_digits) // 2)]

        integers = [int(str(pair[0]) + str(pair[1])) for pair in digit_pairs]
        result_sum = sum(integers)

        return result_sum
