# Between our diagonal, left, and upper tiles, which one contains the largest value?
# (Process used when calculating edit distance)
def getMin(diagonal, left, up):
    if diagonal <= left and diagonal <= up:
        return (diagonal, 'D')
    elif left <= diagonal and left <= up:
        return (left, 'L')
    elif up <= diagonal and up <= left:
        return (up, 'U')

# Calculate edit distance VALUES and possible movements to create our alignment (Which is useful for getAlignments() below)
def editDistance(word1: str, word2: str):
    row, col = len(word1) + 1, len(word2) + 1
    edit_distance_values = [[0] * col for i in range(row)] # Matrix for all edit distance NUMERICAL VALUES
    edit_distance_movements = [['D'] * col for i in range(row)] # Matrix for the DIRECTIONS TO GO 
    
    # Filling the outside of matrix with increasing numbers
    # (First row, and first columns only)
    for c in range(1, col):
        edit_distance_values[0][c] = c
        edit_distance_movements[0][c] = 'L'
    for r in range(1, row):
        edit_distance_values[r][0] = r
        edit_distance_movements[r][0] = 'U'
    
    # Looping through the matrix at the 1th positions of rows and columns
    # to analyze how many edit operations are needed for each entry of matrix
    for r in range(1, row):
        for c in range(1, col):
            if word1[r - 1] != word2[c - 1]:
                val, mvt = getMin(edit_distance_values[r - 1][c - 1], 
                                                edit_distance_values[r][c - 1], 
                                                edit_distance_values[r - 1][c])
                edit_distance_values[r][c] = val + 1
                edit_distance_movements[r][c] = mvt
            else: # If word1[r - 1] == word2[c - 1]
                edit_distance_values[r][c] = edit_distance_values[r - 1][c - 1]
                edit_distance_movements[r][c] = 'D'
    
    return edit_distance_values, edit_distance_movements

# Printing our Matrix
def displayMatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])

    for r in range(row):
        row_to_print = ''
        for c in range(col):
            num = str(matrix[r][c])
            token = '  ' + num + ' '*(2 - len(num)) + ' :' # Formatting each cell of the table
            row_to_print += token
        print(row_to_print)
        print('-' * len(row_to_print)) # Seperating each row using dashed lines

# This function returns the alignment strings by starting at the bottom left of the movements matrix (See editDistance())
# by starting at bottom right of movement matrix and working our way up to the top left according to directions in each cell:
# Whether to go: Up, Left, or Diagonal
def getAlignments(edit_movements, first_word, second_word):
    # First word's length represent the number of rows
    # Second word's length represent the number of columns
    
    row, col = len(edit_movements) - 1, len(edit_movements[0]) - 1
    first_alignment, second_alignment = '', ''

    while row >= 0 and col >= 0:
        if edit_movements[row][col] == 'D':
            first_alignment = first_word[row] + first_alignment[:]
            second_alignment = second_word[col] + second_alignment[:]
            row -= 1
            col -= 1
        elif edit_movements[row][col] == 'L':
            first_alignment = '_' + first_alignment[:]
            second_alignment = second_word[col] + second_alignment[:]
            col -=1
        elif edit_movements[row][col] == 'U':
            first_alignment = first_word[row] + first_alignment[:]
            second_alignment = '_' + second_alignment[:]
            row -= 1

    return first_alignment, second_alignment

# Main Program running/displaying everything
if __name__ == '__main__':
    first = str(input("The first word: "))
    second = str(input("The second word: "))


    edit_vals, edit_movts = editDistance(first, second)

    print('\nThe Matrix:\n')
    displayMatrix(edit_vals)
    print()
    # displayMatrix(edit_movts)

    # Last item of matrix is the final value calculated
    print(f'\n\nThe edit distance is: {edit_vals[len(edit_vals) - 1][len(edit_vals[0]) - 1]}')

    first_alignment, second_alignment = getAlignments(edit_movts, ' ' + first, ' ' + second)

    print('\nAlignments:')
    print(first_alignment)
    print(second_alignment)