from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_to_strs = defaultdict(list)
        for s in strs:
            anagram_to_strs["".join(sorted(s))].append(s)
        return list(anagram_to_strs.values())