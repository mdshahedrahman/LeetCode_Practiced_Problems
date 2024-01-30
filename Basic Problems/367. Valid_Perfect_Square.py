import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        result = math.sqrt(num)
        if result.is_integer():
            return True
        else:
            return False