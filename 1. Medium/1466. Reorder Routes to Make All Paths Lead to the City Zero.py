from collections import defaultdict
from typing import Any, List, Literal


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        grid = defaultdict(list)
        for a, b in connections:
            grid[a].append((b, 1))
            grid[b].append((a, 0))

        def dfs(location, parent) -> Any | Literal[0]:
            ans = 0
            for connection, direction in grid[location]:
                if connection == parent:
                    continue
                ans += direction + dfs(connection, location)
            return ans

        return dfs(0, -1)
