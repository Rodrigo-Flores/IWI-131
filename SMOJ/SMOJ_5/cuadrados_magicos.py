square = int(input())


matrix = []

for column in range(square):
    sub_matrix = []
    for file in range(square):
        sub_matrix.append(int(input()))

    matrix.append(sub_matrix)


magic_counter = 1
plus = sum(matrix[0])
i = 1
while i < square:
    if sum(matrix[i]) == plus:
        magic_counter+=1

    i+=1

if magic_counter == square:
    print(plus)

else:
    print('NO')