class TreeNode:
    def __init__(self, key: int, val: int) -> None:
        self.key: int = key
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class TreeMap:
    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if not self.root:
            self.root = new_node
            return
        node = self.root
        while True:
            if key < node.key:
                if not node.left:
                    node.left = new_node
                    return
                node = node.left
            elif key > node.key:
                if not node.right:
                    node.right = new_node
                    return
                node = node.right
            else:
                node.val = val
                return

    def get(self, key: int) -> int:
        node = self.root
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.val
        return -1

    def getMin(self) -> int:
        node = self.findMin(self.root)
        return node.val if node else -1

    def findMin(self, node: TreeNode | None) -> TreeNode | None:
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        node = self.findMax(self.root)
        return node.val if node else -1

    def findMax(self, node: TreeNode | None) -> TreeNode | None:
        while node and node.right:
            node = node.right
        return node

    def remove(self, key: int) -> None:
        def _remove(node: TreeNode | None, key: int) -> TreeNode | None:
            if not node:
                return None
            if key < node.key:
                node.left = _remove(node.left, key)
            elif key > node.key:
                node.right = _remove(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    min_node = self.findMin(node.right)
                    if min_node:
                        node.key = min_node.key
                        node.val = min_node.val
                        node.right = _remove(node.right, min_node.key)
            return node

        self.root = _remove(self.root, key)

    def getInorderKeys(self) -> list[int]:
        result: list[int] = []
        self.inorderTraveral(self.root, result)
        return result

    def inorderTraveral(self, node: TreeNode | None, result: list[int]) -> None:
        if node:
            self.inorderTraveral(node.left, result)
            result.append(node.key)
            self.inorderTraveral(node.right, result)
