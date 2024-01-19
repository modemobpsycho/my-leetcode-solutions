from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        start_index = 0
        count = 1
        previous_element = chars[0]
        for i in range(1, len(chars)):
            if chars[i] == previous_element:
                count += 1
            else:
                chars[start_index] = previous_element
                previous_element = chars[i]
                if count != 1:
                    count = str(count)
                    for j in range(len(count)):
                        chars[start_index + 1 + j] = count[j]
                    start_index += len(count) + 1
                    count = 1
                else:
                    start_index += 1
                    count = 1

        chars[start_index] = chars[-1]
        if count != 1:
            count = str(count)
            for j in range(len(count)):
                chars[start_index + 1 + j] = count[j]
            return start_index + len(count) + 1
        else:
            return start_index + 1
