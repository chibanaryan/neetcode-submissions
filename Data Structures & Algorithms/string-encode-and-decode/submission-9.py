class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        res = []
        while i < len(s):
            hash_idx = s.index("#", i)
            char_count = int(s[i:hash_idx])
            next_str = s[hash_idx+1:hash_idx+1+char_count]
            res.append(next_str)
            i = hash_idx+1+char_count
        return res


