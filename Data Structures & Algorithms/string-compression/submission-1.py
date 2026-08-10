from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        read: int = 0
        write: int = 0
        ml: int = len(chars)
        while read < ml:
            c: str = chars[read]
            count: int = 0
            while read < ml and chars[read] == c:
                read += 1
                count += 1

            chars[write] = c
            write += 1
            if count != 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
