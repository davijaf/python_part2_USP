
def sum_matrix(x,y):
    z = []
    for i in range(len(x)):
        w = []
        for j in range(len(x[i])):
            w.append(x[i][j]+y[i][j])
        z.append(w)

    return z

if __name__ == "__main__":
    x = [[1,2,3],[4,5,6],[7,8,9]]
    y = [[10,20,30],[40,50,60],[70,80,90]]
    print(sum_matrix(x,y))