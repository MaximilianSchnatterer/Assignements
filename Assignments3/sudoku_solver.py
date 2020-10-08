

class SudokuSolver(object):

    def __init__(self, sudoku):

        self.sudoku = sudoku
        self.is_solved = False
        return


    def solve(self):
        index = 0
        while not self.is_solved and index<81:
            for row_index in range(0,9):
                for column_index in range(0,9):
                    if self.sudoku[row_index][column_index] > 0:
                        continue

                    posnumbers = self.compute_possible_numbers(row_index, column_index)
                    if len(posnumbers) == 1:
                        self.insert_number(row_index, column_index, posnumbers[0])
            self.check_is_solved()
            print(f'Iteration {index}')
            self.print_solution()
            index += 1
        return


    def compute_possible_numbers(self, row_index, column_index):
        posnumbers = []
        for number in range(1, 10):
            if not(self.check_in_row(row_index, number)or self.check_in_column(column_index, number)or self.check_in_subgrid(row_index, column_index, number)):
                posnumbers.append(number)
        return posnumbers

    def insert_number(self, row_index, column_index, number):
        self.sudoku[row_index][column_index] = number
        return
    
    def check_in_row(self, row_index, number):
        if number in self.sudoku[row_index]:
            check = True
        else: 
            check = False
        return check
  
    def check_in_column(self, column_index, number):
        if number in SudokuSolver.compute_column(self, column_index):
            check = True
        else: 
            check = False
        return check
 
    def check_in_subgrid(self, row_index, column_index, number):
        for column_elements in range(SudokuSolver.compute_sub_grid_index(self, column_index)[0],SudokuSolver.compute_sub_grid_index(self, column_index)[1]):
            for row_elements in range(SudokuSolver.compute_sub_grid_index(self, row_index)[0],SudokuSolver.compute_sub_grid_index(self, row_index)[1]):
                if number == self.sudoku[row_elements][column_elements]:
                    check = True
                    break
                else:
                    check = False
            
            if check == True:
                break
        return  check

    def compute_column(self,column_index):
        self.column = []
        for elements in range(0,9):
            self.column.append(self.sudoku[elements][column_index])
        return self.column

    def compute_sub_grid_index(self,index):
        index_from = int(index/3)*3
        index_to = int(index/3)*3+3
        return (index_from, index_to)

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