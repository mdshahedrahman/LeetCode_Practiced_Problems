class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        temp_div = []
        temp_nondiv = []

        for i in range(1,n+1):
            if i % m == 0:
                temp_div.append(i)
            else:
                temp_nondiv.append(i)

        sum_dif = sum(temp_nondiv) - sum(temp_div)

        return sum_dif