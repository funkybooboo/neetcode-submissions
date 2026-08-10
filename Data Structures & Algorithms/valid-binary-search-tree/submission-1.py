class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root: Optional[TreeNode], low: float, high: float) -> bool:
        if not root:
            return True

        if not (low < root.val < high):
            return False

        return self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)
