from collections import defaultdict, deque
from typing import Any, List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)

        for i in range(len(equations)):
            a, b = equations[i][0], equations[i][1]
            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]

        def bfs(start, end) -> Any | float:
            q = deque()
            q.append((start, 1))
            seen = set()

            while q:
                for _ in range(len(q)):
                    node, res = q.popleft()
                    if node == end:
                        return res
                    seen.add(node)

                    for n in graph[node]:
                        if n not in seen:
                            q.append((n, res * graph[node][n]))

            return -1.0

        res = []
        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
            else:
                res.append(bfs(a, b))

        return res
