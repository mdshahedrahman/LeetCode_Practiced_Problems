class Solution:
    def findComplement(self, num: int) -> int:
        binary_representation = bin(num)[2:]
        inverted_string = ''.join(['1' if bit == '0' else '0'
                                   for bit in binary_representation])
        decimal_number = int(inverted_string, 2)
        return decimal_number

    