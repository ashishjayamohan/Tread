def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise TypeError('Table must be a square')
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


def element_wise_multiply(matrix1, matrix2):
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
    if len(new_matrix1) != len(new_matrix2) or len(new_matrix1[0]) != len(new_matrix2[0]):
        raise TypeError(
            f"Cannot point-wise multiply matrices of the size {len(new_matrix1)} x {len(new_matrix1[0])} and {len(new_matrix2)} x {len(new_matrix2[0])}"
        )
    else:
        result_matrix = []
        for x in range(len(new_matrix1)):
            result_matrix.append([])
            for y in range(len(new_matrix1[0])):
                result_matrix[x].append(new_matrix1[x][y] * new_matrix2[x][y])
    return result_matrix


def add_column_values(table, column_title, column_values):
    """
    Adds a column to a specific table
    Note that you must include a column title and the values of the column
    """
    table[0].append(column_title)
    for j in range(1, len(table)):
        table[j].append(column_values[j])
    return table


def remove_column(table, index):
    """
    Removes a column from a given table given the column index
    """
    for j in table:
        j.pop(index)
    return table


def extract_column(table, index):
    """
    Returns the values of a specific column in a table given the column index
    """
    return [j[index] for j in table]


def vector_function_column(table, function, index):
    """
    This function carries out a given function on a given table column
    It is necessary to refer to the column index and the function as a function pointer
    """
    for j in range(len(table)):
        table[j][index] = function(table[j][index])
    return table
