class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_dict = defaultdict(set)
        row_dict = defaultdict(set)
        out_box_dict = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in col_dict[j]:
                    return False
                
                if board[i][j] in row_dict[i]:
                    return False
                
                if board[i][j] in out_box_dict[(i//3, j//3)]:
                    return False
                
                col_dict[j].add(board[i][j])
                row_dict[i].add(board[i][j])
                out_box_dict[(i//3, j//3)].add(board[i][j])
        
        return True