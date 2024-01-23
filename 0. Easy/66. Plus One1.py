from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carr = 1

        for i in reversed(range(len(digits))):
            carr, digits[i] = divmod(digits[i] + carr, 10)

        return digits if not carr else [carr] + digits
