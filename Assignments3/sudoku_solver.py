

class SudokuSolver(object):

    def __init__(self, sudoku):

        self.sudoku = sudoku
        self.is_solved = False
        return


    def solve(self):
        index = 0
        while self.is_solved == False & index < 82:
            SudokuSolver.check_is_solved()
            SudokuSolver.print_solution()
            index += 1
        

    def check_is_solved(self):
        if all(self.sudoku) == 0:
            self.is_solved = False
        else:
            self.is_solved = True
        return

    def print_solution(self):
        print()
        index = 0
        while index < 9:
            print(self.sudoku[index])
            index += 1
        print()
        return



