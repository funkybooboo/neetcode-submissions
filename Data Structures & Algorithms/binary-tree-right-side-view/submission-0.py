class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_most = []

        def helper(root: Optional[TreeNode], level: int):
            if not root:
                return

            # If we're visiting this level for the first time,
            # it means this node is the rightmost node at this level
            if level == len(right_most):
                right_most.append(root.val)

            # Traverse right subtree first to ensure rightmost nodes are visited before left ones
            helper(root.right, level + 1)

            # Then traverse left subtree
            helper(root.left, level + 1)

        helper(root, 0)

        return right_most
