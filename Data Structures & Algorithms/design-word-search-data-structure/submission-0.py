class Node:
    def __init__(self, value: str | None = None):
        self.c: str | None = value
        self.children: list[Node] = []
        self.terminating = False

    def add_child(self, node: "Node"):
        self.children.append(node)


class WordDictionary:
    def __init__(self):
        self._root = Node()

    def addWord(self, word: str) -> None:
        node = self._root
        for c in word:
            # try to find an existing child
            next_child = None
            for child in node.children:
                if child.c == c:
                    next_child = child
                    break
            # if not found, create it
            if not next_child:
                next_child = Node(c)
                node.add_child(next_child)
            node = next_child
        node.terminating = True

    def search(self, word: str) -> bool:
        # recursive helper
        def helper(node: Node, i: int) -> bool:
            if i == len(word):
                return node.terminating

            c = word[i]
            if c == ".":
                # try any child
                for child in node.children:
                    if helper(child, i + 1):
                        return True
                return False
            else:
                # match a specific character
                for child in node.children:
                    if child.c == c:
                        return helper(child, i + 1)
                return False

        return helper(self._root, 0)
