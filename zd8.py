def solve_sudoku(matrix):
  
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
              
                for num in range(1, 5):
                    if is_valid(matrix, i, j, num):
                        matrix[i][j] = num         
                        if solve_sudoku(matrix):    
                            return True
                        matrix[i][j] = 0           
                return False 
    
    return True

def is_valid(matrix, row, col, num):
    # Проверка строки
    for j in range(4):
        if matrix[row][j] == num:
            return False
    
    # Проверка столбца
    for i in range(4):
        if matrix[i][col] == num:
            return False
    
    # Проверка квадрата 2×2
    start_row = (row // 2) * 2
    start_col = (col // 2) * 2
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if matrix[i][j] == num:
                return False
    
    return True

matrix = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 1, 0, 0],
    [3, 0, 0, 4]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

solve_sudoku(matrix)

print("\nРешённая матрица:")
for row in matrix:
    print(row)