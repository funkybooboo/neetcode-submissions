#from __future__ import annotations
from typing import Iterator, Iterable, Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    __slots__ = ("data", "prev", "next")

    def __init__(self, data: T) -> None:
        self.data: T = data
        self.prev: Optional[Node[T]] = None
        self.next: Optional[Node[T]] = None

    def __repr__(self) -> str:
        return f"Node({self.data!r})"


class DoublyLinkedList(Generic[T]):
    def __init__(self, iterable: Optional[Iterable[T]] = None) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self._size: int = 0

        if iterable:
            for item in iterable:
                self.append(item)

    # ---------- Core Operations ----------

    def append(self, data: T) -> None:
        """Add element to the end (O(1))"""
        new_node: Node[T] = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, data: T) -> None:
        """Add element to the beginning (O(1))"""
        new_node: Node[T] = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def pop(self) -> T:
        """Remove and return last element (O(1))"""
        if not self.tail:
            raise IndexError("pop from empty list")
        data: T = self.tail.data
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            assert self.tail is not None
            self.tail.next = None
        self._size -= 1
        return data

    def popleft(self) -> T:
        """Remove and return first element (O(1))"""
        if not self.head:
            raise IndexError("popleft from empty list")
        data: T = self.head.data
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            assert self.head is not None
            self.head.prev = None
        self._size -= 1
        return data

    # ---------- Utility Operations ----------

    def find(self, data: T) -> Optional[Node[T]]:
        """Return first node containing data, or None"""
        current: Optional[Node[T]] = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def remove(self, data: T) -> None:
        """Remove first occurrence of data (O(n))"""
        node: Optional[Node[T]] = self.find(data)
        if not node:
            raise ValueError(f"{data!r} not in list")
        self._remove_node(node)

    def _remove_node(self, node: Node[T]) -> None:
        """Remove a given node (O(1))"""
        if node is self.head:
            self.popleft()
        elif node is self.tail:
            self.pop()
        else:
            assert node.prev is not None
            assert node.next is not None
            node.prev.next = node.next
            node.next.prev = node.prev
            self._size -= 1

    def insert_after(self, target_data: T, new_data: T) -> None:
        """Insert new_data after first occurrence of target_data"""
        node: Optional[Node[T]] = self.find(target_data)
        if not node:
            raise ValueError(f"{target_data!r} not in list")

        new_node: Node[T] = Node(new_data)
        new_node.prev = node
        new_node.next = node.next

        if node is self.tail:
            self.tail = new_node
        else:
            assert node.next is not None
            node.next.prev = new_node

        node.next = new_node
        self._size += 1

    def insert_before(self, target_data: T, new_data: T) -> None:
        """Insert new_data before first occurrence of target_data"""
        node: Optional[Node[T]] = self.find(target_data)
        if not node:
            raise ValueError(f"{target_data!r} not in list")

        if node is self.head:
            self.prepend(new_data)
        else:
            new_node: Node[T] = Node(new_data)
            assert node.prev is not None
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node
            self._size += 1

    # ---------- Advanced Operations ----------

    def reverse(self) -> None:
        """Reverse in-place (O(n))"""
        current: Optional[Node[T]] = self.head
        self.head, self.tail = self.tail, self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev  # prev is original next

    def to_list(self) -> list[T]:
        """Convert to Python list"""
        return [node.data for node in self]

    # ---------- Magic Methods ----------

    def __iter__(self) -> Iterator[Node[T]]:
        current: Optional[Node[T]] = self.head
        while current:
            yield current
            current = current.next

    def __reversed__(self) -> Iterator[Node[T]]:
        current: Optional[Node[T]] = self.tail
        while current:
            yield current
            current = current.prev

    def __len__(self) -> int:
        return self._size

    def __contains__(self, data: T) -> bool:
        return self.find(data) is not None

    def __repr__(self) -> str:
        items: list[str] = [str(node.data) for node in self]
        return f"DoublyLinkedList([{', '.join(items)}])"

    def __getitem__(self, index: int) -> T:
        """Support indexing (O(n))"""
        if index < 0:
            index += self._size
        if not 0 <= index < self._size:
            raise IndexError("index out of range")

        # Optimize: start from closer end
        current: Node[T]
        if index < self._size // 2:
            assert self.head is not None
            current = self.head
            for _ in range(index):
                assert current.next is not None
                current = current.next
        else:
            assert self.tail is not None
            current = self.tail
            for _ in range(self._size - 1 - index):
                assert current.prev is not None
                current = current.prev

        return current.data


class Deque:
    def __init__(self):
        self._queue: DoublyLinkedList[int] = DoublyLinkedList()

    def isEmpty(self) -> bool:
        return len(self._queue) == 0

    def append(self, value: int) -> None:
        self._queue.append(value)

    def appendleft(self, value: int) -> None:
        self._queue.prepend(value)

    def pop(self) -> int:
        try:
            return self._queue.pop()
        except:
            return -1

    def popleft(self) -> int:
        try:
            return self._queue.popleft()
        except:
            return -1
