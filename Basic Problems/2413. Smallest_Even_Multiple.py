class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        temp = []

        for i in range(10):
            mul = n * i
            temp.append(mul)

        final_array = sorted(temp)

        for i in final_array:
            if i % 2 == 0 and i != 0:
                return i
                break