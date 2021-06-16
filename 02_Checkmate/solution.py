n = 8
matrix = [[y for y in input().split(' ')] for x in range(n)]
final_list = []
queens = []
#find Queens positions
for index1, x in enumerate(matrix):
    for index2, y in enumerate(x):
        if y == 'Q':
            temp_list = []
            temp_list.append(index1)
            temp_list.append(index2)
            queens.append(temp_list)
for queen in queens:
    x_pos, y_pos = queen
    # up-left
    counter = 0
    for x in range(x_pos - 1, -1, -1):
        flag = 0
        counter += 1
        for y in range(y_pos - counter, -1, -1):
            if flag == 0:
                if matrix[x][y] == 'K':
                    final_list.append(queen)
                elif matrix[x][y] == 'Q':
                    break
                else:
                    flag += 1

    # up
    for x in range(x_pos - 1, -1, -1):
        if matrix[x][y_pos] == 'K':
            final_list.append(queen)
        elif matrix[x][y_pos] == 'Q':
            break

    # up-right
    counter = 0
    for x in range(x_pos - 1, -1, -1):
        flag = 0
        counter += 1
        for y in range(y_pos + counter, n):
            if flag == 0:
                if matrix[x][y] == 'K':
                    final_list.append(queen)
                elif matrix[x][y] == 'Q':
                    break
                else:
                    flag += 1

    # left
    for y in range(y_pos - 1, -1, -1):
        if matrix[x_pos][y] == 'K':
            final_list.append(queen)
        elif matrix[x_pos][y] == 'Q':
            break

    # right
    for y in range(y_pos + 1, n):
        if matrix[x_pos][y] == 'K':
            final_list.append(queen)
        elif matrix[x_pos][y] == 'Q':
            break

    # down-left
    counter = 0
    for x in range(x_pos + 1, n):
        flag = 0
        counter += 1
        for y in range(y_pos - counter, -1, -1):
            if flag == 0:
                if matrix[x][y] == 'K':
                    final_list.append(queen)
                elif matrix[x][y] == 'Q':
                    break
                else:
                    flag += 1

    # down
    for x in range(x_pos + 1, n):
        if matrix[x][y_pos] == 'K':
            final_list.append(queen)
        elif matrix[x][y_pos] == 'Q':
            break

    # down-right
    counter = 0
    for x in range(x_pos + 1, n):
        flag = 0
        counter += 1
        for y in range(y_pos + counter, n):
            if flag == 0:
                if matrix[x][y] == 'K':
                    final_list.append(queen)
                elif matrix[x][y] == 'Q':
                    break
                else:
                    flag += 1

if final_list:
    [print(x) for x in final_list]
else:
    print('The king is safe!')