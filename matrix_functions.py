def determinant(matrix):
    if (len(matrix) != len(matrix[0])):
        raise TypeError('Matrix must be square.')
    else:
        size = len(matrix)
        if (size == 1):
            return matrix[0][0] # the determinant of a 1x1 matrix is the value of the only element in the matrix.
        else:
            newmatrix = matrix[1:] # take off top row of matrix
            ret = 0 # keep track of return value
            for i in range(size): # for each top row element
                element = matrix[0][i] # get that element
                minor = list(row[0:i]+row[i+1:size] for row in newmatrix)
                minor_determinant = determinant(minor) # find the determinant of that element's minor
                if (i % 2 == 0): # alternate between adding and subtracting their product
                    ret += element * minor_determinant
                else:
                    ret -= element * minor_determinant
            return ret