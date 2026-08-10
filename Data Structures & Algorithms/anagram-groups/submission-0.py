class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use defaultdict to collect anagram groups
        ms: defaultdict[str, List[str]] = defaultdict(list)

        for s in strs:
            # Sort each string and use it as a key for anagram grouping
            key = ''.join(sorted(s))
            ms[key].append(s)

        # Return the grouped anagrams
        return list(ms.values())

