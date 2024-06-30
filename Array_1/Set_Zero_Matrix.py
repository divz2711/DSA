class Solution(object):
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        rowzero = False

        # Determine which rows and columns need to be zeroed
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowzero = True

        # Use the first row and column to set zeroes
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Zero out the first column if needed
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # Zero out the first row if needed
        if rowzero:
            for c in range(cols):
                matrix[0][c] = 0