from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_dict_to_str = defaultdict(list)
        for s in strs:
            char_to_count = self._get_char_to_count(s)
            print(str(char_to_count))
            count_dict_to_str[tuple(sorted(char_to_count.items()))].append(s)
        ans = []
        for val in count_dict_to_str.values():
            ans.append(val)
        return ans
        
    def _get_char_to_count(self, s: str) -> Dict[str, int]:
        char_to_count = defaultdict(int)
        for c in s:
            char_to_count[c] += 1
        return char_to_count