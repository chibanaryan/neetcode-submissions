from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_to_instances = defaultdict(list)
        for s in strs:
            sorted_to_instances[''.join(sorted(s))].append(s)
        return list(sorted_to_instances.values())