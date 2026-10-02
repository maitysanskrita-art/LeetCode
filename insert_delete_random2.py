import random

class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        is_new = val not in self.pos

        if val not in self.pos:
            self.pos[val] = set()

        self.pos[val].add(len(self.arr))
        self.arr.append(val)

        return is_new

    def remove(self, val: int) -> bool:
        if val not in self.pos or not self.pos[val]:
            return False

        index = self.pos[val].pop()
        last = self.arr[-1]

        self.arr[index] = last

        if index != len(self.arr) - 1:
            self.pos[last].remove(len(self.arr) - 1)
            self.pos[last].add(index)

        self.arr.pop()

        if not self.pos[val]:
            del self.pos[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)