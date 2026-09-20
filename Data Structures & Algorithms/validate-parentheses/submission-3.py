class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        bracket_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for c in s:
            if c in bracket_map:
                stk.append(c)
            else:
                if not c or not stk or bracket_map[stk.pop()] != c:
                    return False
        return len(stk) == 0
