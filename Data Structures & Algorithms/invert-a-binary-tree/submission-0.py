class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helper(root)
        return root

    def helper(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None
        node = root.left
        root.left = root.right
        root.right = node
        self.helper(root.left)
        self.helper(root.right)

