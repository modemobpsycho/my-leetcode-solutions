class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows: int = len(text2) + 1
        cols: int = len(text1) + 1
        rowlen, collen = 0, 0
        mat: list[list[int]] = [[0 for j in range(cols)] for i in range(rows)]
        for i in range(1, rows):
            for j in range(1, cols):
                if text2[i - 1] == text1[j - 1]:
                    mat[i][j] = mat[i - 1][j - 1] + 1
                else:
                    mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])
        return mat[-1][-1]
