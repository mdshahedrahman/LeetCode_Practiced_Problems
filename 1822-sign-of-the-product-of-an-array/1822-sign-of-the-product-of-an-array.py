class Solution:
    def arraySign(self, nums: List[int]) -> int:
        mul = 1
        count_neg = 0
        count_pos = 0

        for i in nums:
            mul = mul * i

        if mul != 0:
            for i in nums:
            #    temp.append(i)
                if i < 0:
                    count_neg = count_neg + 1
                elif i > 0:
                    count_pos = count_pos + 1
            if count_neg % 2 == 0:
                return (1)
            else: return(-1)

        elif mul == 0:
            return (mul)
