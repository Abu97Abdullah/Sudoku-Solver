def cell_value_ok(puzzle, row_num, col_num, value):
    """
    This function checks if the current number (1-9) picked is 'ok' for
    this row, column, and box of this cell. NOTE: The function doesn't
    tell you if this value in the cell leads to a solution.
    :param puzzle: sudoku puzzle in the form of a 2D list
    :param row_num: integer value from 0-8
    :param col_num: integer value from 0-8
    :param value: integer from 1-9
    :return: Boolean True or False
    """
    # For this particular cell, get its row and column
    col_vec = [i[col_num] for i in puzzle]
    row_vec = puzzle[row_num]

    # Next get the 3x3 box the cell belongs to
    if row_num <= 2:
        if col_num <= 2:
            box = [i[0:3] for i in puzz[0:3]]
        elif col_num <= 5:
            box = [i[3:6] for i in puzz[0:3]]
        else:
            box = [i[6:] for i in puzz[0:3]]
    elif row_num <= 5:
        if col_num <= 2:
            box = [i[0:3] for i in puzz[3:6]]
        elif col_num <= 5:
            box = [i[3:6] for i in puzz[3:6]]
        else:
            box = [i[6:] for i in puzz[3:6]]
    else:
        if col_num <= 2:
            box = [i[0:3] for i in puzz[6:]]
        elif col_num <= 5:
            box = [i[3:6] for i in puzz[6:]]
        else:
            box = [i[6:] for i in puzz[6:]]

    # Flatten the box into a single list (make it easier to work with)
    box_flat = box[0] + box[1] + box[2]

    if (value in col_vec) or (value in row_vec) or (value in box_flat):
        return False
    return True


def solve_sudoku(puzzle, row_num, col_num):
    """
    Solves the sudoku puzzle using recursive means and the
    backtracking algorithm. NOTE: Only works with valid sudoku
    puzzle inputs.
    :param puzzle: sudoku puzzle in the form of a 2D list
    :param row_num: integer value from 0-8
    :param col_num: integer value from 0-8
    :return: True if this is a valid sudoku puzzle input
    """
    # Checking whether we're past the last cell of puzzle
    # or just need to drop down a row
    if col_num > 8:

        # Base case
        if row_num == 8:
            return True

        # Not the base case -> just drop down a row
        # and reset column to 0
        row_num += 1
        col_num = 0

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Going to use '0' to mean empty and
    # first check if cell is empty to begin with
    if puzzle[row_num][col_num] == 0:

        # Going to run through the 'numbers' in the cell of interest
        for i in numbers:
            if cell_value_ok(puzzle, row_num, col_num, i):
                puzzle[row_num][col_num] = i

                # Recursive check if leads to solution
                if solve_sudoku(puzzle, row_num, col_num + 1):
                    return True

                # Backtracking
                puzzle[row_num][col_num] = 0

    # So it's not empty...
    elif solve_sudoku(puzzle, row_num, col_num + 1):  # Recursive check if leads to solution
        return True


def print_solution(puzzle):
    """
    :param puzzle: 2D list of the sudoku puzzle
    :return: NoneType
    """
    for i in range(9):
        for j in puzzle[i]:
            print(str(j) + " ", end="")
        print()


# Now test it!
puzz = [[0, 0, 2, 7, 8, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 9, 8, 0, 1],
        [4, 0, 0, 0, 0, 3, 0, 7, 0],
        [9, 0, 5, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 4, 0, 8],
        [0, 6, 0, 4, 0, 0, 0, 0, 7],
        [3, 0, 9, 8, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 3, 1, 6, 0, 0]]

solve_sudoku(puzz, 0, 0)
print_solution(puzz)
