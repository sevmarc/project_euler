"""
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

p096_1.png     p096_2.png
A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
"""

from function_collection.main import timer_wrapper
import random
import copy


def load_sudoku(filename: str, number: int):
    if number > 50:  # overflow
        print("This sudoku does not exist!")
        return None
    keyword = f"Grid {number}\n"
    if number < 10:
        keyword = f"Grid 0{number}\n"        
    with open(filename, "r") as sudokus:
        all_lines = sudokus.readlines()
        startline = all_lines.index(keyword)
        sudoku = all_lines[(startline + 1) : (startline + 10)]
        sudoku_formatted = [l.strip('\n') for l in sudoku]
        return sudoku_formatted


class Cell:
    def __init__(self, position, value):
        self.value = value
        self.possibilities = [1,2,3,4,5,6,7,8,9]
        if value:
            self.possibilities = [value]
        self.unknown = False
        if value == 0:
            self.unknown = True
        self.position = position
        self.x, self.y = self.position
        self.group_id = self.x // 3 + self.y // 3 * 3

    def set_value(self, val):
        self.value = val
        self.possibilities = [val]
        self.unknown = False

    def elliminate_possibility(self, value):
        if len(self.possibilities) > 1:
            if value in self.possibilities:
                self.possibilities.remove(value)
        if len(self.possibilities) == 1:  # 1 remaining possibility
            self.value = self.possibilities[0]
            self.unknown = False
    
    def print_data(self):
        print(f'X: {self.x}, Y: {self.y}, value: {self.value}, unknown: {self.unknown}, group_id: {self.group_id}')


class Sudoku:
    def __init__(self, lines_of_sudoku, debug=False):
        self.debug = debug
        self.backup = []
        self.sudoku_cells = []
        self.storage = []
        self.fill_cells(lines_of_sudoku)

    def fill_cells(self, lines_of_sudoku):
        for linecounter, line in enumerate(lines_of_sudoku):
            for rowcounter, row in enumerate(line):
                cell = Cell([rowcounter, linecounter], int(row))
                # cell.print_data()
                self.sudoku_cells.append(cell)
                cell_copy = copy.copy(cell)
                self.storage.append(cell_copy)
        print("Original sudoku: ")
        self.print_sudoku()
    
    def get_cell_by_pos(self, pos):
        return self.sudoku_cells[pos[0] + pos[1] * 9]

    def get_row_of_cells(self, row):
        return [cell for cell in self.sudoku_cells if cell.x == row]
    
    def get_line_of_cells(self, line):
        return [cell for cell in self.sudoku_cells if cell.y == line]

    def get_group_of_cells(self, group_id):
        """
        000111222
        000111222
        000111222
        333444555
        333444555
        333444555
        666777888
        666777888
        666777888
        """
        # need to turn position into group_id
        return [cell for cell in self.sudoku_cells if cell.group_id == group_id]
    
    def check_cell_possibilities(self):
        nothing_found = True
        for cell in self.sudoku_cells:
            if cell.unknown:
                for c1 in self.get_row_of_cells(cell.x):
                    if c1.position != cell.position:
                        cell.elliminate_possibility(c1.value)
                for c2 in self.get_line_of_cells(cell.y):
                    if c2.position != cell.position:
                        cell.elliminate_possibility(c2.value)
                for c3 in self.get_group_of_cells(cell.group_id):
                    if c3.position != cell.position:
                        cell.elliminate_possibility(c3.value)
                if cell.value != 0:
                    nothing_found = False
                if self.debug:
                    if cell.value != 0:
                        print("Found it! ")
                        cell.print_data()
        return nothing_found
        
    def print_sudoku(self):
        for i in range(10):
            a = self.get_line_of_cells(i)
            w = ''
            for v in a:
                w += str(v.value)
            print(w)

    def solve_sudoku(self):
        while any([c for c in self.sudoku_cells if c.unknown]):
            if self.debug:
                print(f'remaining possibilities: {sum([len(cell.possibilities) for cell in self.sudoku_cells])}')
                self.print_sudoku()
            # checking for possibilities, if none found, we have to make a guess
            if not self.check_integrity():
                if self.debug:
                    print('Integrity broke')
                temp = self.restore_backup()
                temp.get_cell_by_pos(self.tip_cell.position).elliminate_possibility(self.tip_val)
                return temp.solve_sudoku()
            
            notfound = self.check_cell_possibilities()

            if notfound:
                temp = copy.deepcopy(self)
                self.backup.append(temp)
                self.tip_val, self.tip_cell = self.guess_a_value()
            
        if not self.check_integrity():
            retry = copy.deepcopy(self)
            retry.backup = []
            retry.sudoku_cells = []
            for c in retry.storage:
                retry.sudoku_cells.append(copy.copy(c))
            if self.debug:
                print('RETRY: ')
                retry.print_sudoku()
            return retry.solve_sudoku()
        print("DONE! ")
        self.print_sudoku()
        result = ''
        for i in range(3): 
            result += str(self.sudoku_cells[i].value)
        return int(result)
    
    def guess_a_value(self):
        min_ = min([len(cell.possibilities) for cell in self.sudoku_cells if cell.unknown])
        mins = [cell for cell in self.sudoku_cells if len(cell.possibilities) == min_]

        index = random.randint(0, len(mins) - 1)
        cell = mins[index]
        guess = cell.possibilities[0]
        cell.set_value(guess)
        if self.debug:
            print(f'guessing: {cell.position}: {cell.value}')
        return guess, cell

    def check_integrity(self):
        for cell in self.sudoku_cells:
            if not cell.unknown:
                for c1 in self.get_row_of_cells(cell.x):
                    if c1.position != cell.position and c1.value == cell.value:
                        if self.debug:
                            self.print_sudoku()
                            print(c1.position, cell.position)
                        return False
                for c2 in self.get_line_of_cells(cell.y):
                    if c2.position != cell.position and c2.value == cell.value:
                        if self.debug:
                            self.print_sudoku()
                            print(c2.position, cell.position)
                        return False
                for c3 in self.get_group_of_cells(cell.group_id):
                    if c3.position != cell.position and c3.value == cell.value:
                        if self.debug:
                            self.print_sudoku()
                            print(c3.position, cell.position)
                        return False
        return True

    def restore_backup(self):
        if self.debug:
            print("restoring backups...")
        backups = self.backup
        temp = copy.deepcopy(backups[-1])
        backups.pop(len(backups) - 1)
        temp.backup = backups
        return temp


def calc96():
    num_of_sudokus = 50  # 1 to 50
    sum = 0

    for s in range(1, num_of_sudokus + 1):
        print(s)
        x = Sudoku(load_sudoku("inputfiles/96_sudoku.txt", s), debug=False)
        val = x.solve_sudoku()
        print(val)
        sum += val
    return sum

# s1 = Sudoku(load_sudoku("96_sudoku.txt", 1))
# s1.solve_sudoku()
# timer_wrapper(Sudoku(load_sudoku("96_sudoku.txt", 44), debug=True).solve_sudoku)


print(timer_wrapper(calc96))  # runtime: ~71 sec
