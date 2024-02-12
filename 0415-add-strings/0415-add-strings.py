class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        carry = 0

        # Make the lengths of num1 and num2 equal by adding leading zeros
        num1 = num1.zfill(max(len(num1), len(num2)))
        num2 = num2.zfill(max(len(num1), len(num2)))

        # Perform addition digit by digit
        for i in range(len(num1) - 1, -1, -1):
            digit_sum = int(num1[i]) + int(num2[i]) + carry
            result.append(str(digit_sum % 10))
            carry = digit_sum // 10

        # If there's a carry left, add it to the result
        if carry:
            result.append(str(carry))

        # Reverse the result list and join to get the final string
        return ''.join(result[::-1])