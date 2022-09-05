
def mult_matrix(x,y):
    num_line_x, num_col_x = len(x), len(x[0])
    num_line_y, num_col_y = len(y), len(y[0])
    assert num_col_x == num_line_y
    z = []
    for line in range(num_line_x):
        z.append([])
        for collun in range(num_col_y):
            z[line].append(0)
            for k in range(num_col_x):
                z[line][collun] += x[line][k] * y[k][collun]
    return z

if __name__ == "__main__":
    x = [[1,2,3],[4,5,6]]
    y = [[1,2],[3,4],[5,6]]
    print(mult_matrix(x,y))