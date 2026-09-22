class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = s.index("#", i)
            char_count = int(s[i:j])
            current_str = s[j+1 : j+1+char_count] 
            res.append(current_str)
            i = j + 1 + char_count
        return res
