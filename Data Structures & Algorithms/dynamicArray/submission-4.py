class DynamicArray:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self._capacity: int = capacity
        self._size: int = 0
        self._array: list[int] = [0] * capacity

    def get(self, i: int) -> int:
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds")
        return self._array[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds")
        self._array[i] = n

    def pushback(self, n: int) -> None:
        self.resize()
        self._size += 1
        self._array[self._size - 1] = n

    def popback(self) -> int:
        if self._size == 0:
            raise IndexError("Pop from empty array")
        n: int = self._array[self._size - 1]
        self._size -= 1
        self.resize()
        return n

    def resize(self) -> None:
        if self._size >= self._capacity:
            self._capacity *= 2
            while len(self._array) < self._capacity:
                self._array.append(0)

    def getSize(self) -> int:
        return self._size

    def getCapacity(self) -> int:
        return self._capacity