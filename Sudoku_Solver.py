# SUDOKU_SOLVER

def find_next_empty(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row,col

    return None, None

def valid_num(puzzle,guess,r,c):
    row_values = puzzle[r]
    if guess in row_values:
        return False

    col_values = []
    for i in range(9):
        col_values.append(puzzle[i][c])
        if guess in col_values:
            return False

    # 3*3 CUBE
    row_start = (r//3)*3
    col_start = (c//3)*3

    for row in range(row_start,row_start+3):
        for col in range(col_start,col_start+3):
            if puzzle[row][col] == guess:
                return False

    return True



def solve_sudoku(puzzle):
    r, c = find_next_empty(puzzle)

    if r is None:
        return True

    for guess in range(1,10):
        if valid_num(puzzle, guess, r, c):
            puzzle[r][c] = guess

            if solve_sudoku(puzzle):
                return True 

        puzzle[r][c] = -1
    
    
    return False 


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)

# Solved Board(Output)    
[[3, 9, 1, 8, 5, 6, 4, 2, 7], 
 [8, 6, 7, 2, 3, 4, 9, 1, 5],
 [4, 2, 5, 7, 1, 9, 6, 8, 3],
 [7, 5, 4, 9, 6, 8, 1, 3, 2], 
 [2, 1, 6, 4, 7, 3, 5, 9, 8], 
 [9, 3, 8, 5, 2, 1, 7, 6, 4], 
 [5, 4, 3, 6, 9, 2, 8, 7, 1], 
 [6, 7, 2, 1, 8, 5, 3, 4, 9], 
 [1, 8, 9, 3, 4, 7, 2, 5, 6]]
