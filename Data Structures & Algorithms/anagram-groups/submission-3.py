from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_to_strs = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            anagram_to_strs[sorted_s].append(s)
        return [v for v in anagram_to_strs.values()]