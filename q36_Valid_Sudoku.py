class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        validSet = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        line = [[] for _ in range(9)]
        row = [[] for _ in range(9)]
        box = [[] for _ in range(9)]
        for x in range(9):
            for y in range(9):
                data = board[x][y]
                z = x // 3 + 3 * (y // 3)
                if data == '.':
                    pass
                elif data not in validSet:
                    return False
                elif data in line[x] or data in row[y] or data in box[z]:
                    return False
                else:
                    line[x].append(data)
                    row[y].append(data)
                    box[z].append(data)
        return True

    def isValidSudoku1(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += (j,c),(i,c),(i//3,j//3,c),
        return len(seen) == len(set(seen))


board1 = [[".", "8", "7", "6", "5", "4", "3", "2", "1"], ["2", ".", ".", ".", ".", ".", ".", ".", "."],
          ["3", ".", ".", ".", ".", ".", ".", ".", "."], ["4", ".", ".", ".", ".", ".", ".", ".", "."],
          ["5", ".", ".", ".", ".", ".", ".", ".", "."], ["6", ".", ".", ".", ".", ".", ".", ".", "."],
          ["7", ".", ".", ".", ".", ".", ".", ".", "."], ["8", ".", ".", ".", ".", ".", ".", ".", "."],
          ["9", ".", ".", ".", ".", ".", ".", ".", "."]]
board2 = [[".", ".", "4", ".", ".", ".", "6", "3", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
          ["5", ".", ".", ".", ".", ".", ".", "9", "."], [".", ".", ".", "5", "6", ".", ".", ".", "."],
          ["4", ".", "3", ".", ".", ".", ".", ".", "1"], [".", ".", ".", "7", ".", ".", ".", ".", "."],
          [".", ".", ".", "5", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", "."]]
print(Solution().isValidSudoku1(board2))
