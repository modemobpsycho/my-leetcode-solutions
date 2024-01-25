from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visr = set()
        dic = {}
        stack = []

        for i in range(len(rooms)):
            dic[i] = rooms[i]

        for i in dic[0]:
            stack.append(i)

        visr.add(0)

        while len(stack) > 0:
            cur = stack.pop()
            visr.add(cur)
            for i in dic[cur]:
                if i not in visr:
                    stack.append(i)

        return len(dic) == len(visr)
