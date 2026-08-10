from collections import deque
from typing import List, Set, Deque, Tuple


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if len(target) != 4:
            return -1

        lock: str = "0000"
        if lock in deadends:
            return -1

        def increment(lock: str, i: int) -> str:
            return lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i+1:]

        def decrement(lock: str, i: int) -> str:
            return lock[:i] + str((int(lock[i]) - 1 + 10) % 10) + lock[i+1:]

        def children(lock: str) -> List[str]:
            children: List[str] = []
            for i in range(len(lock)):
                children.append(increment(lock, i))
                children.append(decrement(lock, i))
            return children

        q: Deque[Tuple[str, int]] = deque()
        q.append((lock, 0)) # [lock, turns]
        visited: Set[str] = set(deadends)
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    q.append((child, turns + 1))
        return -1
