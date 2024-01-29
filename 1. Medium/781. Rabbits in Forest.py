from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts: set = {}
        count: int = 0

        for answer in answers:
            if answer == 0:
                count += 1
            elif answer not in counts or counts[answer] == 0:
                counts[answer] = 1
                count += answer + 1
            else:
                counts[answer] += 1
                if counts[answer] > answer:
                    counts[answer] = 0

        return count
