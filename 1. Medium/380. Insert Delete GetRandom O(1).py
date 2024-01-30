from random import random


class RandomizedSet:
    def __init__(self) -> None:
        self.S = set()

    def insert(self, val: int) -> bool:
        if val not in self.S:
            self.S.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.S:
            self.S.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.S))
