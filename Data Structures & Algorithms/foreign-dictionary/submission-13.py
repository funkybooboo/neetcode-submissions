from typing import List, Dict, Set

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjacency_list: Dict[str, Set[str]] = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
                return ""
            for j in range(min_length):
                if word1[j] != word2[j]:
                    adjacency_list[word1[j]].add(word2[j])
                    break

        visited: Dict[str, bool] = {}  # False=visited, True=current path
        result: List[str] = []

        def dfs(character: str) -> bool:
            if character in visited:
                return visited[character]
            visited[character] = True
            for neighbor in adjacency_list[character]:
                if dfs(neighbor):
                    return True
            visited[character] = False
            result.append(character)

        for character in adjacency_list:
            if dfs(character):
                return ""
        result.reverse()
        return "".join(result)