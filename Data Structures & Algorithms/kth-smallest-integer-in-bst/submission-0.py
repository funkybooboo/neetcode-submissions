class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        result = root.val

        def helper(node):
            nonlocal count, result
            if not node:
                return

            helper(node.left)
            count -= 1
            if count == 0:
                result = node.val
                return
            helper(node.right)

        helper(root)
        return result
