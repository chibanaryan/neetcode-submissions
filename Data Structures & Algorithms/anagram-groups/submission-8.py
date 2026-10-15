from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_to_strs = defaultdict(list)
        for s in strs:
            anagram = [0] * 26
            for c in s:
                anagram[ord(c.lower()) - ord('a')] += 1
            anagram_to_strs[tuple(anagram)].append(s)
        return [v for v in anagram_to_strs.values()]