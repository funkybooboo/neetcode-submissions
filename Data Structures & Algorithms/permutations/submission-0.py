from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # If the input list is empty, there is exactly one permutation: the empty list
        if len(nums) == 0:
            return [[]]  # Return a list containing an empty list

        # Recursively compute all permutations of the sublist that excludes the first element
        # nums[1:] is the list without its first element
        permutations = self.permute(nums[1:])

        # Initialize an empty list to collect the new permutations
        result = []

        # For each smaller permutation computed from the recursive call:
        for permutation in permutations:
            # We will insert the first element (nums[0]) into every possible position
            # in the current smaller permutation. There are (len(permutation) + 1) such positions.
            for i in range(len(permutation) + 1):
                # Make a copy of the current smaller permutation so as not to modify it in place
                permutation_copy = permutation.copy()
                # Insert the first element of nums at index i
                permutation_copy.insert(i, nums[0])
                # Add this new permutation to the result list
                result.append(permutation_copy)

        # After processing all smaller permutations and all insertion positions,
        # result will hold all permutations of the original list `nums`
        return result
