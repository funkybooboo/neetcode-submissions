class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -100000, 1000000)

    def helper(self, root: Optional[TreeNode], low: int, high: int) -> bool:
        if not root:
            return True

        if not (low < root.val < high):
            return False

        return self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)
