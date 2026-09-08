class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        def horizontal(board):
            answer = True
            for row in board:
                arr = []
                for s in row:
                    if s != '.':
                        num = int(s)
                        if num not in arr:
                            arr.append(num)
                        else:
                            answer = False
                            break
            return answer

        def vertical(board):
            answer = True 
            for x in range(9):
                arr = []
                for i in range(9):
                    cell = board[i][x]
                    if cell != '.':
                        num = int(cell)
                        if num not in arr:
                            arr.append(num)
                        else:
                            answer = False
            return answer

        def grid(board):
            answer = True
            for box_row in range(3):
                for box_col in range(3):
                    arr = []
                    for i in range(3):
                        for j in range(3):
                            r = box_row * 3 + i
                            c = box_col * 3 + j
                            cell = board[r][c]
                            if cell != '.':
                                num = int(cell)
                                if num not in arr:
                                    arr.append(num)
                                else:
                                    answer = False
            return answer

        return horizontal(board) and vertical(board) and grid(board)








