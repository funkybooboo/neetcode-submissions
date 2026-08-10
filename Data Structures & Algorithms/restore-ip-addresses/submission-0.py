from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_int(s: str) -> bool:
            try:
                int(s)
            except:
                return False
            return True

        # Length must be between 4 and 12 digits
        if len(s) < 4 or len(s) > 12 or not is_int(s):
            return []

        def is_ip_address(o1: str, o2: str, o3: str, o4: str) -> bool:
            def is_octet(o: str) -> bool:
                # Valid if no leading zero unless it's "0"
                if len(o) > 1 and o[0] == "0":
                    return False
                # Must be within range 0–255
                if not o.isdigit() or not (0 <= int(o) <= 255):
                    return False
                return True

            return all(is_octet(o) for o in [o1, o2, o3, o4])

        ip_address: List[str] = []

        def try_address(o1: str, o2: str, o3: str, o4: str) -> None:
            if is_ip_address(o1, o2, o3, o4):
                ip_address.append(f"{o1}.{o2}.{o3}.{o4}")

        # Try every possible split into 4 parts (1–3 digits each)
        for i in range(1, 4): # end of first octet
            for j in range(i + 1, i + 4): # end of second octet
                for k in range(j + 1, j + 4): # end of third octet
                    if k >= len(s): # avoid out-of-range slices
                        continue
                    o1, o2, o3, o4 = s[:i], s[i:j], s[j:k], s[k:]
                    # Skip if any part is too long
                    if max(len(o1), len(o2), len(o3), len(o4)) > 3:
                        continue
                    try_address(o1, o2, o3, o4)

        return ip_address
