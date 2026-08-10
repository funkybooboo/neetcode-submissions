class PrefixTree:
    def __init__(self):
        self._whole_words = set()
        self._prefix_words = set()

    def insert(self, word: str) -> None:
        self._whole_words.add(word)
        prefix = ""
        for c in word:
            prefix += c
            self._prefix_words.add(prefix)

    def search(self, word: str) -> bool:
        return word in self._whole_words

    def startsWith(self, prefix: str) -> bool:
        return prefix in self._prefix_words
