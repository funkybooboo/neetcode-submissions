import random
from typing import List, Dict


class RandomizedSet:
    def __init__(self):
        self._vals: List[int] = []
        self._val_to_index: Dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self._val_to_index:
            return False

        self._vals.append(val)
        self._val_to_index[val] = len(self._vals) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self._vals:
            return False

        last_val: int = self._vals[-1]
        val_index: int = self._val_to_index[val]
        self._vals[val_index] = last_val
        self._val_to_index[last_val] = val_index

        self._vals.pop()
        del self._val_to_index[val]

        return True

    def getRandom(self) -> int:
        if not len(self._vals):
            return 0

        return random.choice(self._vals)
