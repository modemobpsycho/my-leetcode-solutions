from typing import Any, Literal


class Solution:
    def decodeString(self, s: str) -> str:
        stack: list = []
        curr_str: Literal[""] = ""
        curr_num = 0

        for c in s:
            if c.isdigit():
                curr_num: int = curr_num * 10 + int(c)
            elif c == "[":
                stack.append(curr_num)
                stack.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif c == "]":
                prev_str: Any = stack.pop()
                prev_num: Any = stack.pop()
                curr_str = prev_str + curr_str * prev_num
            else:
                curr_str += c

        while stack:
            curr_str = stack.pop() + curr_str

        return curr_str
