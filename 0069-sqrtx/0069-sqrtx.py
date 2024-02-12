import math
class Solution:
    def mySqrt(self, x: int) -> int:
        k = math.sqrt(x)
        return math.floor(k)
        