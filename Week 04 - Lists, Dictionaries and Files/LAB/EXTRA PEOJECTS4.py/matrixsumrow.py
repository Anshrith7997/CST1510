def sum_row(matrix, rowIndex):
    return sum(matrix[rowIndex])

matrix = []

for i in range(4):
    row = []

    for j in range(4):
        num = int(input("Enter a number: "))
        row.append(num)

    matrix.append(row)

for i in range(4):
    print("Sum of row", i + 1, "=", sum_row(matrix, i))
