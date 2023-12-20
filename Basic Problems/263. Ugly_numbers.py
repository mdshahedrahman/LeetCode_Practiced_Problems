class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        # Divide the number by 2, 3, and 5 as long as it's divisible
        for prime_factor in [2, 3, 5]:
            while n % prime_factor == 0:
                n //= prime_factor

        # After dividing by 2, 3, and 5, if the remaining number is 1, it's an ugly number
        return n == 1


# Example usage:
solution = Solution()
result = solution.isUgly(6)
print(result)  # Output: True

result = solution.isUgly(14)
print(result)  # Output: False
