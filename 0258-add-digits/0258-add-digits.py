class Solution:
    def addDigits(self, num: int) -> int:
        remainder = num % 9 
        if num ==0: 
            return 0
        elif remainder == 0 and num > 0: 
            return 9
        else: 
            return remainder
        