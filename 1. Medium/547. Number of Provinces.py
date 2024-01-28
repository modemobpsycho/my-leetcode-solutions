from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n: int = len(isConnected)
        visited: list[int] = [0] * n
        num_provinces = 0

        for i in range(n):
            if visited[i] == 0:
                queue = deque([i])
                visited[i] = 1
                while queue:
                    city: int = queue.popleft()
                    for j in range(n):
                        if isConnected[city][j] == 1 and visited[j] == 0:
                            queue.append(j)
                            visited[j] = 1
                num_provinces += 1
        return num_provinces
