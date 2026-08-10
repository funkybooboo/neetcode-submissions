class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', 
                             p: 'TreeNode|int', 
                             q: 'TreeNode|int') -> 'TreeNode':
        path_p = self._get_path_to(root, p)
        path_q = self._get_path_to(root, q)

        return self._get_lca(path_p, path_q)

    @staticmethod
    def _get_lca(a: list['TreeNode'], b: list['TreeNode']) -> 'TreeNode':
        seen = set(b)
        for x in a:
            if x in seen:
                return x
        # LeetCode guarantees p and q are in the tree, so we never really hit this.
        return None

    def _get_path_to(self, root: 'TreeNode', target: 'TreeNode|int') -> list['TreeNode']:
        if not root:
            return []

        # normalize to a value to compare against .val
        tgt_val = getattr(target, 'val', target)

        if root.val == tgt_val:
            return [root]

        # search left
        left_path = self._get_path_to(root.left, target)
        if left_path:
            left_path.append(root)
            return left_path

        # search right
        right_path = self._get_path_to(root.right, target)
        if right_path:
            right_path.append(root)
            return right_path

        return []
