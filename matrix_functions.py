def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise TypeError("Matrix must be a square")
    else:
        size = len(matrix)
        if size == 1:
            return matrix[0][0]
        else:
            newmatrix = matrix[1:]
            ret = 0
            for i in range(size):
                element = matrix[0][i]
                minor = list(row[0:i] + row[i + 1 : size] for row in newmatrix)
                minor_determinant = determinant(minor)
                if i % 2 == 0:
                    ret += element * minor_determinant
                else:
                    ret -= element * minor_determinant
            return ret


def multiply(matrix1, matrix2):
    new_matrix1 = []
    new_matrix2 = []
    if not (isinstance(matrix1[0], list)):
        new_matrix1 = [[float(item) for item in matrix1]]
    else:
        for x in range(len(matrix1)):
            new_matrix1.append([])
            for y in range(len(matrix1[x])):
                new_matrix1[x].append(float(matrix1[x][y]))

    if not (isinstance(matrix2[0], list)):
        new_matrix2 = [[float(item) for item in matrix2]]
    else:
        for x in range(len(matrix2)):
            new_matrix2.append([])
            for y in range(len(matrix2[x])):
                new_matrix2[x].append(float(matrix2[x][y]))
    if len(new_matrix1[0]) != len(new_matrix2):
        raise TypeError(
            f"Cannot multiply matrices of the size {len(new_matrix1)} x {len(new_matrix1[0])} and {len(new_matrix2)} x {len(new_matrix2[0])}"
        )
    else:
        result_matrix = [[0 for item in new_matrix2[0]] for item in new_matrix1]
        for x in range(len(new_matrix1)):
            for y in range(len(new_matrix2[0])):
                for z in range(len(new_matrix2)):
                    result_matrix[x][y] += new_matrix1[x][z] * new_matrix2[z][y]

    return result_matrix
