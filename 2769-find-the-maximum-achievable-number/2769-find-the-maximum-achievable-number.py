class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        
        for i in range(10000):
            output_1 = num + t
            x = output_1 + t
            if (x - t) == output_1:
                return x
                break
