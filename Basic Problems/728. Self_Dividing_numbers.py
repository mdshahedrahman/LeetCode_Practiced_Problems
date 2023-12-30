from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        temp = []

        for i in range(left, right + 1):
            str_number = str(i)
            digits = [int(digit) for digit in str_number]
            if all(digit != 0 and i % digit == 0 for digit in digits):
                temp.append(i)

        return temp