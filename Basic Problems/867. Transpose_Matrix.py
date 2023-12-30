from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Find the number of rows and columns in the original matrix
        num_rows = len(matrix)
        num_columns = len(matrix[0]) if num_rows > 0 else 0

        # Initialize the transposed matrix with zeros
        transposed_matrix = [[0] * num_rows for _ in range(num_columns)]

        # Fill in the values for the transposed matrix
        for i in range(num_rows):
            for j in range(num_columns):
                transposed_matrix[j][i] = matrix[i][j]

        return transposed_matrix

# Example usage:
solution_instance = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = solution_instance.transpose(matrix)

print(result)
