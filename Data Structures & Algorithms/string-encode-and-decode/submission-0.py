class Solution:
    SEPARATOR = '%%'

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans += s + self.SEPARATOR
        return ans

    def decode(self, s: str) -> List[str]:
        return s.split(self.SEPARATOR)[:-1]