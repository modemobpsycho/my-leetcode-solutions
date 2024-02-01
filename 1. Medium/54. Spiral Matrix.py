from typing import Any, List, Literal


class Solution:
    def remove_boundary(
        self, matrix, final_list, terminate
    ) -> tuple[Any, Any, Literal[True]] | tuple:
        n: int = len(matrix)
        if n > 0:
            m: int = len(matrix[0])

        if n > 0:
            final_list.extend(matrix[0])
            del matrix[0]

            if len(matrix) > 0:
                for i in range(len(matrix)):
                    if matrix[i] != []:
                        final_list.append(matrix[i].pop())

                final_list.extend(matrix[i][::-1])
                del matrix[i]
            if len(matrix) > 0:
                for i in range(len(matrix))[::-1]:
                    if matrix[i] != []:
                        final_list.append(matrix[i].pop(0))
        else:
            terminate = True
            return final_list, matrix, terminate

        return final_list, matrix, terminate

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        terminate = False
        final_list: list = []
        while not terminate:
            final_list, matrix, terminate = self.remove_boundary(
                matrix, final_list, terminate
            )
        return final_list
