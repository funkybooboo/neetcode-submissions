from collections import deque
from typing import List, Set


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0

        wordSet = set(wordList)
        queue = deque([(beginWord, 1)])
        visited: Set[str] = set()

        while queue:
            current_word, count = queue.popleft()
            if current_word == endWord:
                return count

            for next_word in self.get_one_away_words(current_word, wordSet - visited):
                visited.add(next_word)
                queue.append((next_word, count + 1))

        return 0

    def get_one_away_words(self, word: str, wordSet: Set[str]) -> List[str]:
        neighbors = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != word[i]:
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in wordSet:
                        neighbors.append(new_word)
        return neighbors
