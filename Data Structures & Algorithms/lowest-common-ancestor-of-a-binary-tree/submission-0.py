# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> Optional["TreeNode"]:
        if not root or not p or not q:
            return None

        def make_path(node: Optional["TreeNode"], t: "TreeNode") -> List["TreeNode"]:
            if not node:
                return []
            if node.val == t.val:
                return [node]
            
            left_path = make_path(node.left, t)
            if left_path:
                return [node] + left_path
            
            right_path = make_path(node.right, t)
            if right_path:
                return [node] + right_path
            
            return []

        p_path: List["TreeNode"] = make_path(root, p)
        q_path: List["TreeNode"] = make_path(root, q)

        last: Optional["TreeNode"] = None
        for p_n, q_n in zip(p_path, q_path):
            if p_n.val != q_n.val:
                return last
            last = p_n

        return last
