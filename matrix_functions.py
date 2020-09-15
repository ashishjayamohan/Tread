def determinant(matrix):
    if (len(matrix) != len(matrix[0])):
        raise TypeError('Matrix must be a square')
    else:
        size = len(matrix)
        if (size == 1):
            return matrix[0][0]
        else:
            newmatrix = matrix[1:]
            ret = 0
            for i in range(size):
                element = matrix[0][i]
                minor = list(row[0:i]+row[i+1:size] for row in newmatrix)
                minor_determinant = determinant(minor)
                if (i % 2 == 0):
                    ret += element * minor_determinant
                else:
                    ret -= element * minor_determinant
            return ret
