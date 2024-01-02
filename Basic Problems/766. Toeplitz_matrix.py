from typing import  List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        is_toeplitz = True

        for i in range(rows - 1):
            for j in range(cols - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    is_toeplitz = False
                    break

        if is_toeplitz:
            return True
        else:
            return False
