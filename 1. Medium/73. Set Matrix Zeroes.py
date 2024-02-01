from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n: int = len(matrix)
        m: int = len(matrix[0])

        rows: list = []
        col: list = []
        x = 0
        for i in range(n):
            if x in (matrix[i]):
                rows.append(i)
            for j in range(m):
                if matrix[i][j] == 0:
                    col.append(j)

        for i in rows:
            for j in range(m):
                matrix[i][j] = 0

        for j in col:
            for i in range(n):
                matrix[i][j] = 0
