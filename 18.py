# Maximum path sum I
import time

test_triangle = [
          [3],
        [7, 4],
       [2, 4, 6],
      [8, 5, 9, 3],
]

triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]


def str_to_int(tri):
    rows = []
    for row in tri:
        row2 = []
        for val in row:
            row2.append(int(val))
        rows.append(row2)
    return rows

def read_triangle_from_file(f):
    return str_to_int([(line.replace('\n', '').split(' ')) for line in open(f, 'r')])

def naive_path_finder(tri):
    n = len(tri)
    i = 0
    pos_in_row = 0
    path = [pos_in_row]
    values = [tri[0][0]]
    while(i != n - 1):
        i += 1
        pos = pos_in_row
        val_in_row = max( tri[i][pos], tri[i][pos + 1] )
        if val_in_row == tri[i][pos]:
            pos_in_row = pos
        else:
            pos_in_row = pos + 1
        values.append(val_in_row)
        path.append(pos_in_row)
    return values, path, sum(values)

def find_best_path(tri):
    counter = 0
    for i in range(len(tri)-2,-1,-1):
    	for j in range(len(tri[i])):
    		tri[i][j] = tri[i][j] + max(tri[i+1][j], tri[i+1][j+1])
    		counter += 1
    	tri.pop()
    print('Found {} in {} iterations'.format(tri[0][0],counter))


start_time = time.time()

# print(triangle)
# print(read_triangle_from_file("18.txt"))
find_best_path(triangle)

print(time.time() - start_time)