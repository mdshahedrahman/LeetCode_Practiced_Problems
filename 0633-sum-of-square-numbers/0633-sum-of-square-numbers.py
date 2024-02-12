class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(c**0.5) + 1):
            j = c - i*i
            if (j >= 0) and (int(j**0.5)**2 == j):
                return True
        return False
