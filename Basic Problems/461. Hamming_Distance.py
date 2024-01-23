class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = x ^ y

        # Convert the result to binary
        result_binary = bin(result)[2:]

        # Count the number of set bits (1s)
        count_ones = result_binary.count('1')

        return count_ones