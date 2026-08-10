from typing import List

class Solution:
    def characterReplacement(self, string: str, max_changes: int) -> int:
        # Initialize the result variable to store the maximum length of valid substring
        max_window_size = 0
        
        # Initialize a frequency map to track character counts within the window
        char_count = {}
        
        # Initialize left pointer of the window
        left_pointer = 0
        
        # Iterate through the string with the right pointer
        for right_pointer in range(len(string)):
            # Increment the count for the current character at the right pointer
            char_count[string[right_pointer]] = char_count.get(string[right_pointer], 0) + 1
            
            # Find the most frequent character in the current window
            max_freq = max(char_count.values())
            
            # Check if the window is valid, if not, shrink it from the left
            if (right_pointer - left_pointer + 1) - max_freq > max_changes:
                # Shrink the window by moving the left pointer
                char_count[string[left_pointer]] -= 1
                left_pointer += 1
            
            # Update the result with the maximum valid window length encountered
            max_window_size = max(max_window_size, right_pointer - left_pointer + 1)

        # Return the result after processing the entire string
        return max_window_size