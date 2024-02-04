class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        temp = []
        temp_1 = []

        for i in range(n):
            temp.append(start)
            start = start + 2

        result = temp[0]
        for i in range(len(temp) - 1):
            result = result ^ temp [i + 1]
            temp_1.append(result)


        return result