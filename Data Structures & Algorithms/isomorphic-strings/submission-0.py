from typing import Dict, List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True
        if len(s) != len(t):
            return False

        def encode_pattern(string: str) -> List[int]:
            next_id: int = 0
            char_to_id: Dict[str, int] = {}
            pattern: List[int] = []

            for char in string:
                if char in char_to_id:
                    pattern.append(char_to_id[char])
                else:
                    char_to_id[char] = next_id
                    pattern.append(next_id)
                    next_id += 1

            return pattern

        s_pattern: List[int] = encode_pattern(s)
        t_pattern: List[int] = encode_pattern(t)

        return s_pattern == t_pattern
