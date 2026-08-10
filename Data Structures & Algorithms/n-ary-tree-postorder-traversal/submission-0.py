class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        if not root.children:
            return [root.val]

        result = []
        for child in root.children:
            result.extend(self.postorder(child))
        result.append(root.val)
        return result
