class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        def extract_digits(n):
            digits = []

            while n > 0:
                digit = n % 10
                digits.insert(0, digit)  # Insert at the beginning to maintain order
                n //= 10

            return digits

        result = extract_digits(n)

        sum_digits = sum(result)
        mul = 1

        for i in result:
            mul = mul * i
            
        return (mul - sum_digits)


