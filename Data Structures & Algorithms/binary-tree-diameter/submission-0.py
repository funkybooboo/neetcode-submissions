class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            # update the max diameter if this path is longer
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            # return depth to parent
            return max(left_depth, right_depth) + 1

        dfs(root)
        return self.max_diameter
