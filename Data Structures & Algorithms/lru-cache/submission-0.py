from typing import Dict, List


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity: int = capacity
        self._key_to_value: Dict[int, int] = {}
        self._usage_order: List[int] = [] # Tracks order of key usage (oldest at front)

    def _mark_recent(self, key: int) -> None:
        if key in self._usage_order:
            self._usage_order.remove(key)
        self._usage_order.append(key)

    def get(self, key: int) -> int:
        if key not in self._key_to_value:
            return -1
        self._mark_recent(key)
        return self._key_to_value[key]

    def put(self, key: int, value: int) -> None:
        if key in self._key_to_value:
            self._key_to_value[key] = value
            self._mark_recent(key)
            return

        if len(self._key_to_value) == self._capacity:
            lru_key = self._usage_order.pop(0) # Remove least recently used
            del self._key_to_value[lru_key]

        self._key_to_value[key] = value
        self._usage_order.append(key)
