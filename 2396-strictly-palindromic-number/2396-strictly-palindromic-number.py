class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def base_conversion(number, base):
            if base < 2 or base > 36:
                raise ValueError("Base must be between 2 and 36")

            result = ""
            while number > 0:
                remainder = number % base
                result = str(remainder) + result
                number //= base

            return result if result else "0"

        def is_palindrome(string):
            return string == string[::-1]

        for base in range(2, n):
            base_n_number = base_conversion(n, base)
            if not is_palindrome( base_n_number):
                return False
        return True 