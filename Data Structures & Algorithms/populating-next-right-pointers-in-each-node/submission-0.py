class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        m: Dict[int, Node] = {}

        def dfs(depth: int, node: Node) -> None:
            if not node:
                return

            if depth not in m:
                m[depth] = node
            else:
                m[depth].next = node
                m[depth] = node

            dfs(depth + 1, node.left)
            dfs(depth + 1, node.right)

        dfs(0, root)
        return root
