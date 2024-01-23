from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        column_starts_with: List[int] = grid[0]

        columns = [[] for _ in column_starts_with]

        for row in grid:
            for j, element in enumerate(row):
                columns[j].append(element)

        equal_pairs = 0

        for row in grid:
            for j, element in enumerate(column_starts_with):
                if row[0] == element:
                    if row == columns[j]:
                        equal_pairs += 1

        return equal_pairs
