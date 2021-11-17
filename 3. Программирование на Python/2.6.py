/step/7

numbers = [int(input())]
while sum(numbers) != 0:
    numbers.append(int(input()))
print(sum([x**2 for x in numbers]))

/step/8

def get_strange_sequence(length):
    sequence = []
    for i in range(1, length + 1):
        for j in range(i):
            sequence.append(i)
            if len(sequence) == length:
                break
        else:
            continue
        break
    return sequence
for param in get_strange_sequence(int(input())):
    print(param, end=' ')

/step/9

def get_indexes(lst, item):
    indexes = []
    for i in range(len(lst)):
        if lst[i] == item:
            indexes.append(i)
    return sorted(indexes)
numbers = [int(i) for i in input().split()]
number = int(input())
positions = get_indexes(numbers, number)
if len(positions) > 0:
    for pos in positions:
        print(pos, end=' ')
else:
    print('Отсутствует')
    
/step/10

def input_matrix(stop_word):
    matrix = []
    while True:
        row = input()
        if row == stop_word:
            break
        matrix.append([int(x) for x in row.split()])
    return matrix
def matrix_to_str(matrix):
    s = ''
    for row in matrix:
        for elem in row:
            s += (str(elem) + ' ')
        s += "\n"
    return s
def get_summed_matrix(matrix):
    final_matrix = []
    for i in range(len(matrix)):
        final_row = []
        for j in range(len(matrix[0])):
            item = matrix[i][j - 1]\
                + matrix[i - 1][j]\
                + matrix[i + 1 - len(matrix)][j]\
                + matrix[i][j + 1 - len(matrix[0])]
            final_row.append(item)
        final_matrix.append(final_row)
    return final_matrix
print(matrix_to_str(get_summed_matrix(input_matrix('end'))))

/step/11

def matrix_to_str(matrix):
    s = ''
    for row in matrix:
        for elem in row:
            s += (str(elem) + ' ')
        s += "\n"
    return s
def get_spiral_matrix(n):
    x, y, dx, dy, m = 0, 0, 0, 1, [[0] * n for _ in range(n)]
    for i in range(n * n):
        m[x][y] = str(i + 1)
        if x + dx >= n or x + dx < 0 or y + dy >= n or y + dy < 0 or m[x + dx][y + dy]:
            dx, dy = dy, -dx
        x, y = x + dx, y + dy
    return m
print(matrix_to_str(get_spiral_matrix(int(input()))))
