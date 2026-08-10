class Solution:
    def reverseBits(self, n: int) -> int:
        binary: str = ""
        for i in range(32):
            if n & (1 << i):
                binary += "1"
            else:
                binary += "0"

        next_n: int = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                next_n |= (1 << i)

        return next_n
