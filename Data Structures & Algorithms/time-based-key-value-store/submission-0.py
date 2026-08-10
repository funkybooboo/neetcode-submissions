from typing import Generic, TypeVar, Dict, List, Tuple, Optional

V = TypeVar('V')

class TimeMap(Generic[V]):
    def __init__(self):
        self.store: Dict[str, List[Tuple[int, V]]] = {}

    def set(self, key: str, value: V, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> Optional[V]:
        if key not in self.store:
            return ""

        items = self.store[key]
        left, right = 0, len(items) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            if items[mid][0] == timestamp:
                return items[mid][1]
            elif items[mid][0] < timestamp:
                result = items[mid][1]  # Keep track of latest value <= timestamp
                left = mid + 1
            else:
                right = mid - 1

        return result
