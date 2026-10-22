class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_char = set()
        max_len = 0
        i, j = 0, 0
        # Increment j until dup found
        # Increment i until dup removed
        while i < len(s):
            while j < len(s) and s[j] not in unique_char:
                unique_char.add(s[j])
                max_len = max(max_len, len(unique_char))
                j += 1
            unique_char.remove(s[i])
            i += 1
        return max_len