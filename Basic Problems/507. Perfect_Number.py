class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = []

        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)

        divisors.remove(num)

        print(divisors)

        divisors_sum_1 = 0

        for divisor in divisors:
            if num % divisor == 0:
                divisors_sum_1 += divisor

        print(divisors_sum_1)

        return divisors_sum_1 == num

# Example usage
sol = Solution()
result = sol.checkPerfectNumber(24)
print(result)
