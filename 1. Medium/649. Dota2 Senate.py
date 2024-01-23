class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue: list[bool] = [False] * len(senate)
        order = set()
        skipD, skipR = 0, 0
        while len(order) != 1:
            order = set()
            for i in range(len(senate)):
                if queue[i]:
                    continue
                if senate[i] == "R":
                    if skipR > 0:
                        skipR -= 1
                        queue[i] = True
                    else:
                        skipD += 1
                        order.add("R")
                else:
                    if skipD > 0:
                        skipD -= 1
                        queue[i] = True
                    else:
                        skipR += 1
                        order.add("D")
        return "Radiant" if order.pop() == "R" else "Dire"
