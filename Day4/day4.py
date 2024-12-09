from Solution.solution import *

class SolutionD4(Solution):
    # Get a processable grid (2D array)
    def get_formatted_input(self):
        return list(map(lambda x: list(x), self.input))

class SolutionD4C1(SolutionD4):
    # Check if a character is the first letter of a word and, if so, how many words
    def is_first_letter_of_word(self, word, row, col):
        word = word[1:]
        grid = self.get_formatted_input()
        print(f"\nNew check: {col},{row}")

        def check_direction(row, col, dr, dc):
            print("New direction")
            for i in range(len(word)):
                new_row, new_col = row + dr, col + dc
                if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
                    return False
                print(f"Comparing to {grid[new_row][new_col]} ({new_col},{new_row})")
                if grid[new_row][new_col] != word[i]:
                    return False
                row, col = new_row, new_col
            print("Hit!")
            return True

        directions = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

        hits = 0
        for dr, dc in directions:
            if check_direction(row, col, dr, dc):
                hits += 1

        return hits
    
    # Find occurrences of XMAS in the input grid
    def solve(self):
        hits = 0
        for y in range(len(self.input)):
            for x in range(len(self.input[y])):
                if self.input[y][x] == 'X':
                    hits += self.is_first_letter_of_word('XMAS', y, x)
        return hits