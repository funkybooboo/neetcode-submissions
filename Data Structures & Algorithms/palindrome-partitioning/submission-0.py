from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Returns all possible palindrome partitionings of the input string s.
        """
        result = []  # Final list to hold all valid palindrome partitions
        part = []    # Current partition being built (list of substrings)

        def dfs(start_index: int):
            """
            Performs depth-first search to explore all partition possibilities
            starting from index `start_index`.
            """
            # If we've reached the end of the string, record the current partition
            if start_index >= len(s):
                result.append(part.copy())  # Use copy to avoid mutation
                return

            # Explore all substrings starting at start_index
            for end_index in range(start_index, len(s)):
                substring = s[start_index:end_index + 1]

                # Check if the current substring is a palindrome
                if self.is_palindrome(substring):
                    part.append(substring)    # Choose
                    dfs(end_index + 1)        # Explore
                    part.pop()                # Un-choose (backtrack)

        # Start DFS from the beginning of the string
        dfs(0)
        return result

    def is_palindrome(self, s: str) -> bool:
        """
        Returns True if the given string s is a palindrome.
        Uses two-pointer technique for efficient check.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
