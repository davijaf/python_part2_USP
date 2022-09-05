def create_matrix(num_lines, num_colluns):
    matrix = []
    for i in range(num_lines):
        line = []
        for j in range(num_colluns):
            value = int(input("Enter a number ["+ str(i)+"]["+ str(j)+"] : "))
            line.append(value)

        matrix.append(line)

    #print(matrix)
    for i in range(len(matrix)):
        print(matrix[i])


# create_matrix(4,5,1)

def read_matrix():
    lin = int(input("Enter a total lines in matrix : "))
    col = int(input("Enter a total colluns in matrix : "))
    create_matrix(lin,col)

read_matrix()
