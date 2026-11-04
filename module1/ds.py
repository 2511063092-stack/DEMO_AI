import pandas as dp

str = "dnjnjdsksjdsjkds ks"
atpos = str.find(" ")

def square(data):
    result = [valua*valua for valua in data]
    return result

def relu(x):
    result = 0
    if x > 0:
        result = x

    return result

def reluForlist(data):
    result = [relu(x) for x in data]
    return result

def relu1(data):
    result = [x if x > 0 else 0 for x in data]
    return result

data = list(name)

#2D list
# create 2D Matrix

m = [[1,2,3], [4,5,6], [7,8,9]]
numrows = len(m) # 3 row in your example
numcols = len(m[0]) # 2 colums in your example

for row in m:
    for elem in row:
        print(elem, end=' ')
    print()

for r in range(numrows):
    for c in range(numcols):
        print(m[r][c], end=' ')
    print()

N = [[None]*cols for _ in range(rows)]

for r in range(row):
    for c in range(cols):
        N[r][c] = G[r][c] * H[r][c]

# create the matrix 
first_row = [1, 2, 3, 4]
first_col = [1, 5, 9, 13]
rows  = len(first_row)
cols = len(first_col)
matrix = [[0] * cols for _ in range(rows)]
for i in range(cols):
    matrix[0][i] = first_row[i]
for j in range(rows):
    matrix[r][0] = first_col[r]

for i in range(1, rows):
    for j in range(1, cols):
        matrix[i][j] = matrix[i][j-1] + matrix[i-1][j-1] + matrix[i - 1][j-1]


file_name = "data.txt"
def read_data(file_name):
    with open(file_name, "r") as file:
        data = file.read()
        file.close()
    return data.split(',') #tách 

def fill_missing_with_average(data):
    missing_values = [i for i, x in enumerate(data) if len(x) == 0]
    non_missing_values = [float(x) for x in data if len(x) > 0]
    average = sum(non_missing_values) / len(non_missing_values)
    for index in missing_values:
        data[index] = average
    return data

def write_data(file_name, data):
    with open(file_name, 'w') as file:
        file.write(','.join(str(x) for x in data))
        file.close()