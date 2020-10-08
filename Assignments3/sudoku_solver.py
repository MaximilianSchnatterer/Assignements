

class SudokuSolver(object):

    def __init__(self, sudoku):

        self.sudoku = sudoku
        self.is_solved = False
        return


    def solve(self):
        index = 0
        while not self.is_solved and index<81:
            SudokuSolver.check_is_solved(self)
            SudokuSolver.print_solution(self)
            index += 1
        return
        

    def check_is_solved(self):
        
        for elements in range(0,9):
            if all(self.sudoku[elements]) == False:
                self.is_solved = False
                break
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



