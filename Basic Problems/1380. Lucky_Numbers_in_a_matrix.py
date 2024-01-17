from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result = []

        # Iterate through each row
        for row_index, row in enumerate(matrix):
            min_in_row = min(row)

            # Find the column index of the minimum element in the row
            col_index = row.index(min_in_row)

            # Check if the minimum element is also the maximum in its column
            if min_in_row == max(matrix[i][col_index] for i in range(len(matrix))):
                result.append(min_in_row)

        return result