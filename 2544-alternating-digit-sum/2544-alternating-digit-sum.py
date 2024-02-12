class Solution:
    def alternateDigitSum(self, n: int) -> int:
        num_str = str(n)

    # Extract digits at odd and even indices
        odd_index_digits = [int(num_str[i]) for i in range(len(num_str)) if i % 2 == 0]
        even_index_digits = [int(num_str[i]) for i in range(len(num_str)) if i % 2 != 0]

    # Calculate the sum of digits at odd and even indices
        sum_odd_indices = sum(odd_index_digits)
        sum_even_indices = sum(even_index_digits)

        result = sum_odd_indices - sum_even_indices

        return result
        