from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_to_numset = defaultdict(set)
        col_to_numset = defaultdict(set)
        box_to_numset = defaultdict(set)
        for row_idx, row in enumerate(board):
            for col_idx, col in enumerate(row):
                val = board[row_idx][col_idx]
                box_tuple = self._coords_to_box_tuple(row_idx, col_idx)
                if val != "." and (
                    val in row_to_numset[row_idx] or
                    val in col_to_numset[col_idx] or
                    val in box_to_numset[box_tuple]
                ):
                    return False
                row_to_numset[row_idx].add(val)
                col_to_numset[col_idx].add(val)
                box_to_numset[box_tuple].add(val)
        return True

    def _coords_to_box_tuple(self, x, y) -> tuple(int, int):
        return (x // 3, y // 3)