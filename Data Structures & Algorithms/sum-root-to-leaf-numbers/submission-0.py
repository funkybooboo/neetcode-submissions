# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def helper(node: Optional[TreeNode], number: str) -> List[str]:
            if not node:
                return []

            number = number[:]
            number += str(node.val)

            if not node.left and not node.right:
                return [number]

            return helper(node.left, number) + helper(node.right, number)

        return sum([int(s) for s in helper(root, "")])
