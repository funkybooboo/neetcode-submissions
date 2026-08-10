from typing import List, Dict, Set

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 0:
            return ""
        if len(words) == 1:
            return words[0]

        adj_list: Dict[str, Set[str]] = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            word1: str = words[i]
            word2: str = words[i + 1]
            min_length: int = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
                return ""
            for j in range(min_length):
                letter1 = word1[j]
                letter2 = word2[j]
                if letter1 != letter2:
                    adj_list[letter1].add(letter2)
                    break

        visited: Dict[str, bool] = {}
        stack: List[str] = []

        def dfs(node: str) -> bool:
            if node in visited:
                return visited[node]
            visited[node] = True
            for neighbor in adj_list[node]:
                if dfs(neighbor):
                    return True
            visited[node] = False
            stack.append(node)
            return False

        nodes = list(adj_list.keys())
        for node in nodes:
            if dfs(node):
                return ""

        stack.reverse()
        return "".join(stack)
