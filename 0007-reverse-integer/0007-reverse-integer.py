class Solution:
    def reverse(self, x: int) -> int:
        # Determine the sign
        sign = -1 if x < 0 else 1

        # Convert the absolute value of the integer to a string and reverse it
        reversed_str = str(abs(x))[::-1]

        # Convert the reversed string back to an integer and apply the original sign
        reversed_int = int(reversed_str) * sign

        # Handle overflow cases
        max_int = 2**31 - 1
        min_int = -2**31
        if reversed_int > max_int or reversed_int < min_int:
            return 0

        return reversed_int
