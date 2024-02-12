class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(map(str, digits)))
        number = number + 1 
        digits_array = list(map(int, str(number)))
        return digits_array