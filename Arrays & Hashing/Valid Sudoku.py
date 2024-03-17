class Solution:
    # Optimal Solution
    def isValidSudoku(self,board:List[List]) -> bool:
        st = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                row = f"{board[i][j]}_ROW_{i}"
                col = f"{board[i][j]}_COL_{j}"
                box = f"{board[i][j]}_BOX_{i//3}_{j//3}"
                if row in st or col in st or box in st:
                    return False
                st.add(row)
                st.add(col)
                st.add(box)
        return True


# Loop Solution

'''
class Solution:
    def traverse(self, board: List[List[str]], sr: int, er: int, sc: int, ec: int) -> bool:
        check = set()
        for i in range(sr, er):
            for j in range(sc, ec):
                if board[i][j] != '.':
                    if board[i][j] in check:
                        return False
                    check.add(board[i][j])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in range(9):
            check = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in check:
                        return False
                    check.add(board[i][j])

        # Check columns
        for i in range(9):
            check = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in check:
                        return False
                    check.add(board[j][i])

        # Check subgrids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.traverse(board, i, i + 3, j, j + 3):
                    return False

        return True

'''
