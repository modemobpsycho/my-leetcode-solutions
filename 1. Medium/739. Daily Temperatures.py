from typing import Any, List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer: list[int] = [0] * len(temperatures)
        stack: list = []

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                prev_index: Any = stack.pop()
                answer[prev_index] = i - prev_index

            stack.append(i)

        return answer
