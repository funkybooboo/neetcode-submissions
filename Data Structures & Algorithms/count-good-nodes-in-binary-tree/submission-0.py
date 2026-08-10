class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        if not root:
            return count
        def helper(node: TreeNode, m: int) -> None:
            nonlocal count
            if not node:
                return
            if node.val >= m:
                count += 1
            m = max(m, node.val)
            helper(node.left, m)
            helper(node.right, m)
        helper(root, root.val)
        return count
