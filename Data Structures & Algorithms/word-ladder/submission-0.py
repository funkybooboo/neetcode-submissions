from typing import List, Set


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0

        visited: Set[str] = set()
        wordSet = set(wordList)

        smallest = float('inf')

        def dfs(current_word: str, count: int) -> None:
            nonlocal smallest
            if current_word in visited:
                return
            visited.add(current_word)

            one_away_words = self.get_one_away_words(current_word, wordSet - visited)
            if endWord in one_away_words:
                smallest = min(smallest, count + 2)
                visited.remove(current_word)
                return
            for word in one_away_words:
                dfs(word, count + 1)
            visited.remove(current_word)

        dfs(beginWord, 0)
        return int(smallest) if smallest != float('inf') else 0

    def get_one_away_words(self, word: str, words: Set[str]) -> List[str]:
        result = []
        for other_word in words:
            if self.is_one_letter_different(word, other_word):
                result.append(other_word)
        return result

    def is_one_letter_different(self, w1: str, w2: str) -> bool:
        if len(w1) != len(w2):
            return False
        diff_count = 0
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                diff_count += 1
                if diff_count > 1:
                    return False
        return diff_count == 1
