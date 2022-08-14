"""
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

p096_1.png     p096_2.png
A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
"""

from typing import Counter
from function_collection.main import timer_wrapper
import random
import copy


def load_sudoku(number: int, filename:str="problems/inputfiles/96_sudoku.txt") -> list[str]:
    """
    Uses pre-determined format
    """
    if number > 50:  # overflow
        print("This sudoku does not exist!")
        return None
    n = str(number).zfill(2)  # starts with '01'
    keyword = f"Grid {n}\n"
    with open(filename, "r") as sudokus:
        all_lines = sudokus.readlines()
        startline = all_lines.index(keyword)
        sudoku = all_lines[(startline + 1) : (startline + 10)]
        sudoku_formatted = [l.strip('\n') for l in sudoku]
        return sudoku_formatted


class Cell:
    """
    One Cell of the sudoku
    Can hold values 1..9
    We elliminate values when we can, based on the 3 checks
    - row
    - column
    - group (3x3)
    """
    def __init__(self, position: list[int], value: int):
        self.value = value
        self.possibilities = [1,2,3,4,5,6,7,8,9]
        self.unknown = False
        
        if value != 0:
            self.possibilities = [value]
        else:  # this is placed in unknown cells by default
            self.unknown = True
        self.position = position
        self.x, self.y = self.position
        self.group_id = self.x // 3 + self.y // 3 * 3  # group-magic

    def set_value(self, val):
        self.value = val
        self.possibilities = [val]
        self.unknown = False

    def elliminate_possibility(self, value: int):
        if value != 0:  # we can't eliminate this possibility
            if len(self.possibilities) > 1 and value in self.possibilities:
                self.possibilities.remove(value)
            if len(self.possibilities) == 1:  # 1 remaining possibility
                self.set_value(self.possibilities[0])  # tha last possibility

    def __str__(self) -> str:
        return (f'X: {self.x}, Y: {self.y}, value: {self.value}, unknown: {self.unknown}, possibilities: {self.possibilities}')


class Sudoku:
    """
    Sudoku class
    Contains 9x9 cell objects
    """
    def __init__(self, lines_of_sudoku: list[str], debug=False):
        self.debug = debug
        self.backup = []
        self.sudoku_cells = []
        self.storage = []
        self.fill_cells(lines_of_sudoku)

    def fill_cells(self, lines_of_sudoku: list[str]):
        for linecounter, line in enumerate(lines_of_sudoku):
            for rowcounter, row in enumerate(line):
                cell = Cell([rowcounter, linecounter], int(row))
                self.sudoku_cells.append(cell)
                cell_copy = copy.copy(cell)
                self.storage.append(cell_copy)  # to be restored in case of trouble
        if self.debug:
            print(f"Original sudoku: \n{str(self)}")
    
    def get_cell_by_pos(self, pos: list[int]) -> Cell:
        return self.sudoku_cells[pos[0] + pos[1] * 9]

    def get_row_of_cells(self, row: int) -> list[Cell]:
        return [cell for cell in self.sudoku_cells if cell.x == row]
    
    def get_line_of_cells(self, line: int) -> list[Cell]:
        return [cell for cell in self.sudoku_cells if cell.y == line]

    def get_group_of_cells(self, group_id: int) -> list[Cell]:
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
    
    def count_unknowns(self) -> int:
        return len([cell for cell in self.sudoku_cells if cell.unknown])

    def check_cell_possibilities(self) -> bool:
        nothing_found = True
        for cell in self.sudoku_cells:
            if cell.unknown:
                for c1 in self.get_row_of_cells(cell.x):
                    if not c1.unknown and (cell.y != c1.y):
                        cell.elliminate_possibility(c1.value)
                for c2 in self.get_line_of_cells(cell.y):
                    if not c2.unknown and (cell.x != c2.x):
                        cell.elliminate_possibility(c2.value)
                for c3 in self.get_group_of_cells(cell.group_id):
                    if not c3.unknown and ((cell.x != c3.x) or (cell.y != c3.y)):
                        cell.elliminate_possibility(c3.value)
                if cell.value != 0:  # elliminated
                    nothing_found = False
                    if self.debug:
                        print(f"Found it! {self.count_unknowns()}")
                        print(cell)
        
        if nothing_found:
            return nothing_found
        else:
            return self.check_cell_possibilities()
        
    def __str__(self) -> str:
        rows = ""
        for i in range(9):
            cells = self.get_line_of_cells(i)
            w = '|'
            for v in cells:
                w += str(v.value) + '|'
            w += '\n'
            rows += w
        return rows

    def __repr__(self) -> str:
        return str(self)

    def solve_sudoku(self):
        """ The main algorithm """
        while self.count_unknowns() > 0 or not self.check_integrity():
            if self.debug:
                print(f'>> Remaining possibilities: {sum([len(cell.possibilities) for cell in self.sudoku_cells])}')
                print(self)
            # checking for possibilities, if none found, we have to make a guess
            notfound = self.check_cell_possibilities()
            # if checking returns problems -> reload, retry with new guess
            if not self.check_integrity():
                if self.debug:
                    print('<< Integrity broke! ')
                temp = self.restore_backup()
                temp.get_cell_by_pos(self.tip_cell.position).elliminate_possibility(self.tip_val)
                return temp.solve_sudoku()
            # if no unknowns left, and integrity is kept, we are doen
            if self.count_unknowns() == 0:
                break
            # if checking was useless, we make a guess
            if notfound:
                temp = copy.deepcopy(self)
                self.backup.append(temp)
                self.tip_val, self.tip_cell = self.guess_a_value()
                if self.debug:
                    print(f'<< Creating backup... len: {len(self.backup)}')
                
        if not self.check_integrity():
            print('PROBLEM!')
        
        print("DONE! ")
        print(self)
        result = ''
        for i in range(3): 
            result += str(self.sudoku_cells[i].value)
        return int(result)
    
    def guess_a_value(self) -> tuple[int, Cell]:
        """ Sometimes we don't have sure answers """
        min_ = min([len(cell.possibilities) for cell in self.sudoku_cells if cell.unknown])
        mins = [cell for cell in self.sudoku_cells if len(cell.possibilities) == min_]

        random_method = False
        if random_method:
            index = random.randint(0, len(mins) - 1)
            cell = mins[index]
        else:
            c = Counter([cell.value for cell in self.sudoku_cells if not cell.unknown])
            c = sorted(c.items(), key=lambda item: (-item[1], item[0]))
            for co in c:
                common_val = co[0]
                for m in mins:
                    if common_val in m.possibilities:
                        cell = m
                        break
            if not cell:
                cell = mins[0]
        
        guess = cell.possibilities[0]
        old_possibilities = cell.possibilities
        cell.set_value(guess)
        if self.debug:
            print(f'>> Guessing: {cell.position}: {cell.value}, because: {old_possibilities}')
        return guess, cell

    def check_integrity(self) -> bool:
        """ When guessing, the outcome may result in incorrect sudokus """
        for cell in self.sudoku_cells:
            if not cell.unknown:
                for c1 in self.get_row_of_cells(cell.x):
                    if c1.position != cell.position and c1.value == cell.value:
                        if self.debug:
                            print(self)
                            print(c1.position, cell.position)
                        return False
                for c2 in self.get_line_of_cells(cell.y):
                    if c2.position != cell.position and c2.value == cell.value:
                        if self.debug:
                            print(self)
                            print(c2.position, cell.position)
                        return False
                for c3 in self.get_group_of_cells(cell.group_id):
                    if c3.position != cell.position and c3.value == cell.value:
                        if self.debug:
                            print(self)
                            print(c3.position, cell.position)
                        return False
        return True

    def restore_backup(self):
        if self.debug:
            print(f">> Restoring backups... len: {len(self.backup)}")
        backups = self.backup
        temp = copy.deepcopy(backups[-1])  # restore latest backup
        backups.pop(len(backups) - 1)  # remove last backup
        temp.backup = backups
        return temp



def main():
    num_of_sudokus = 50  # 1 to 50
    results = []
    for s in range(1, num_of_sudokus + 1):
        print(s)
        x = Sudoku(load_sudoku(s), debug=False)
        val = x.solve_sudoku()
        results.append(val)
    return sum(results)


if __name__ == '__main__':
    testing = False 
    
    if testing:
        timer_wrapper(Sudoku(load_sudoku(6, "problems/inputfiles/96_sudoku.txt"), debug=True).solve_sudoku)
    else:
        print(timer_wrapper(main))  # runtime: ~71 sec