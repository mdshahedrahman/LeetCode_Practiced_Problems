class Solution:
    def countBits(self, n: int) -> List[int]:
        temp = []

        for i in range(n+1):
            binary_representation = bin(i)[2:]
            temp.append(binary_representation)

        count_of_ones = [bin_str.count('1') for bin_str in temp]

        return count_of_ones