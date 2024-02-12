class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize the result to 0
        reversed_num = 0

        # Iterate through each bit of the input number
        for _ in range(32):
            # Shift the result to the left to make space for the next bit
            reversed_num <<= 1

            # Extract the rightmost bit of the input number and add it to the result
            reversed_num |= n & 1

            # Shift the input number to the right to get the next bit
            n >>= 1

        return reversed_num