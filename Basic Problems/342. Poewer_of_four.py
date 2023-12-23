class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        # Check if n is a power of two
        if (n & (n - 1)) != 0:
            return False

        # Check if the only set bit in n is at an even position
        return bin(n).count('0') % 2 == 1
