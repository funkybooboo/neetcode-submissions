class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # go left, top, right

        l: List[int] = []

        def dfs(root: Optional[TreeNode]) -> None:
            if not root:
                return

            dfs(root.left)
            l.append(root.val)
            dfs(root.right)

        dfs(root)

        return l
