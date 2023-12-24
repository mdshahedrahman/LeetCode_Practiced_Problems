class Solution:
    def hammingWeight(self, n: int) -> int:
        # Convert integer to binary string
        binary_str = bin(n)[2:]  # [2:] to remove the '0b' prefix

        # Count the number of '1' characters in the binary string
        count_ones = binary_str.count('1')
        return count_ones