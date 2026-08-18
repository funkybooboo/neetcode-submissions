from typing import List, Optional


class LinkedListNode:
    def __init__(self, value: int = 0, next: Optional["LinkedListNode"] = None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self._head: Optional[LinkedListNode] = None
        self._tail: Optional[LinkedListNode] = None
        self._length: int = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self._length:
            return -1
        if self._head is None:
            return -1

        current: LinkedListNode = self._head
        for _ in range(index):
            if current.next is None:
                return -1
            current = current.next
        return current.value

    def insertHead(self, val: int) -> None:
        node = LinkedListNode(val, self._head)
        self._head = node
        if self._length == 0:
            self._tail = node
        self._length += 1

    def insertTail(self, val: int) -> None:
        node = LinkedListNode(val)
        if self._length == 0:
            self._head = node
            self._tail = node
        else:
            assert self._tail is not None
            self._tail.next = node
            self._tail = node
        self._length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self._length:
            return False
        if self._head is None:
            return False

        if index == 0:
            self._head = self._head.next
            if self._length == 1:
                self._tail = None
            self._length -= 1
            return True

        current: LinkedListNode = self._head
        for _ in range(index - 1):
            assert current.next is not None
            current = current.next

        assert current.next is not None
        node_to_remove = current.next
        current.next = node_to_remove.next

        if index == self._length - 1:
            self._tail = current

        self._length -= 1
        return True

    def getValues(self) -> List[int]:
        values: List[int] = []
        current: Optional[LinkedListNode] = self._head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values