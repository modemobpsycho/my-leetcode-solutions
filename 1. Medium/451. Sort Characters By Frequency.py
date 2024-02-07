from collections import Counter
import heapq
from typing import Literal


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        pq: list[tuple[int, str]] = [(-freq, char)
                                     for char, freq in counter.items()]
        heapq.heapify(pq)
        result: Literal[''] = ''
        while pq:
            freq, char = heapq.heappop(pq)
            result += char * -freq
        return result
