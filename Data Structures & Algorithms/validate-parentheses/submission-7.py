class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stk = []
        for c in s:
            if c in mapping:
                stk.append(c)
                continue
            
            if not stk or mapping[stk.pop()] != c:
                return False
        return not stk