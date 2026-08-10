class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node: Optional[TreeNode], currentSum: int) -> bool:
            if not node:
                return False

            currentSum += node.val

            if not node.left and not node.right:
                return currentSum == targetSum

            return dfs(node.left, currentSum) or dfs(node.right, currentSum)

        return dfs(root, 0)
