class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.extend(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            hash_offset = s[i:].find('#')
            char_count = int(s[i:i+hash_offset])
            current_str = s[i+hash_offset+1:i+hash_offset+1+char_count] 
            res.append(current_str)
            i = i+hash_offset + 1 + char_count
        return res
