class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        result_integer = int(''.join(map(str, b)))
        power = pow(a, result_integer, 1337)

        return power
        