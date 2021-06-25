# Maximum path sum I
import time


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

def find_best_path(tri):
    counter = 0
    for i in range(len(tri)-2,-1,-1):
    	for j in range(len(tri[i])):
    		tri[i][j] = tri[i][j] + max(tri[i+1][j], tri[i+1][j+1])
    		counter += 1
    	tri.pop()
    print('Found {} in {} iterations'.format(tri[0][0],counter))


start_time = time.time()

triangle = read_triangle_from_file("inputfiles/67.txt")
find_best_path(triangle)

print(time.time() - start_time)