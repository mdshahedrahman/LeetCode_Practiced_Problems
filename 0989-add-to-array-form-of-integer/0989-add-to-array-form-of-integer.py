from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        result = []
        i = len(num) - 1

        while i >= 0 or k > 0 or carry:
            x = num[i] if i >= 0 else 0
            y = k % 10
            current_sum = x + y + carry
            carry = current_sum // 10
            result.append(current_sum % 10)

            i -= 1
            k //= 10

        return result[::-1]