class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.helper(root, 0, result)
        return result

    def helper(self, root: Optional[TreeNode], level: int, result: List[List[int]]) -> None:
        if not root:
            return
        if len(result) <= level:
            result.append([root.val])
        else:
            result[level].append(root.val)

        self.helper(root.left, level + 1, result)
        self.helper(root.right, level + 1, result)
