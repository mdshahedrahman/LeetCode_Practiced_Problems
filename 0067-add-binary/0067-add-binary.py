class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_number_a = int(a, 2)
        decimal_number_b = int(b, 2)
        dec_result = decimal_number_a + decimal_number_b
        binary_representation = bin(dec_result)[2:]

        return binary_representation