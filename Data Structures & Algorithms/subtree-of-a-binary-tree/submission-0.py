class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root:
            return False
        if not subRoot:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, root: Optional[TreeNode], other: Optional[TreeNode]):
        if not root and not other:
            return True
        if not root:
            return False
        if not other:
            return False
        if root.val != other.val:
            return False
        return self.isSame(root.left, other.left) and self.isSame(root.right, other.right)
