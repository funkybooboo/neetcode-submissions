from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Return empty list if input is empty
        if not digits:
            return []

        # Mapping from digits to corresponding letters on a phone keypad
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = []

        # Recursive function to build combinations
        def backtrack(index: int, combination: str):
            # If the current combination is complete, add it to the result
            if index == len(digits):
                combinations.append(combination)
                return

            # Get the letters that the current digit maps to
            current_digit = digits[index]
            letters = digit_to_letters[current_digit]

            # Try each letter in the current position
            for letter in letters:
                backtrack(index + 1, combination + letter)

        # Start the backtracking process from index 0 and an empty string
        backtrack(0, "")
        return combinations
