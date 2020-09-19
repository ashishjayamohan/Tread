from itertools import tee


def determinant(matrix, __len=None, __nocheck=False):
    if (len(matrix) == 0):
        return 1
    elif (not __nocheck) and len(matrix) != len(matrix[0]):
        raise TypeError("Table must be a square")
    else:
        size = __len or len(matrix)
        if size == 1:
            return list(matrix)[0][0]
        elif size == 2:
            matrixlist = list(matrix)
            return (
                matrixlist[0][0] * matrixlist[1][1]
                - matrixlist[1][0] * matrixlist[0][1]
            )
        elif size == 3:
            matrixlist = list(matrix)
            ret = 0
            actual_size = len(matrixlist[0])
            for i in range(actual_size):
                ret += (
                    matrixlist[0][i]
                    * matrixlist[1][(i + 1) % actual_size]
                    * matrixlist[2][(i + 2) % actual_size]
                )
            for i in range(actual_size):
                ret -= (
                    matrixlist[2][i]
                    * matrixlist[1][(i + 1) % actual_size]
                    * matrixlist[0][(i + 2) % actual_size]
                )
            return ret
        else:
            ret = 0
            if isinstance(matrix, list):
                for i in range(size):
                    element = matrix[0][i]
                    recurse_generator = (row[0:i] + row[i + 1 : size] for row in matrix)
                    next(recurse_generator)
                    minor_determinant = determinant(
                        recurse_generator, __len=len(matrix) - 1, __nocheck=True
                    )
                    if i % 2 == 0:
                        ret += element * minor_determinant
                    else:
                        ret -= element * minor_determinant
                return ret
            else:
                start_row = next(matrix)
                new_iterators = tee(matrix, size)
                for i in range(size):
                    element = start_row[i]
                    minor_determinant = determinant(
                        (row[0:i] + row[i + 1 : size] for row in new_iterators[i]),
                        __len=__len - 1,
                        __nocheck=True,
                    )
                    if i % 2 == 0:
                        ret += element * minor_determinant
                    else:
                        ret -= element * minor_determinant
                return ret


def make_matrix(old_matrix):
    if len(old_matrix) == 0:
        raise TypeError('Empty matrix')
    new_matrix = []
    if not (isinstance(old_matrix[0], list)):
        new_matrix = [[float(item) for item in old_matrix]]
    else:
        for x in range(len(old_matrix)):
            new_matrix.append([])
            for y in range(len(old_matrix[x])):
                new_matrix[x].append(float(old_matrix[x][y]))
    return new_matrix


def multiply(matrix1, matrix2):
    new_matrix1 = make_matrix(matrix1)
    new_matrix2 = make_matrix(matrix2)
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
    new_matrix1 = make_matrix(matrix1)
    new_matrix2 = make_matrix(matrix2)
    if len(new_matrix1) != len(new_matrix2) or len(new_matrix1[0]) != len(
        new_matrix2[0]
    ):
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


def add(matrix1, matrix2):
    new_matrix1 = make_matrix(matrix1)
    new_matrix2 = make_matrix(matrix2)
    if len(new_matrix1) != len(new_matrix2) or len(new_matrix1[0]) != len(
        new_matrix2[0]
    ):
        raise TypeError(
            f"Cannot add matrices of the size {len(new_matrix1)} x {len(new_matrix1[0])} and {len(new_matrix2)} x {len(new_matrix2[0])}"
        )
    else:
        result_matrix = []
        for x in range(len(new_matrix1)):
            result_matrix.append([])
            for y in range(len(new_matrix1[0])):
                result_matrix[x].append(new_matrix1[x][y] + new_matrix2[x][y])
    return result_matrix


def subtract(matrix1, matrix2):
    new_matrix1 = make_matrix(matrix1)
    new_matrix2 = make_matrix(matrix2)
    if len(new_matrix1) != len(new_matrix2) or len(new_matrix1[0]) != len(
        new_matrix2[0]
    ):
        raise TypeError(
            f"Cannot subtract matrices of the size {len(new_matrix1)} x {len(new_matrix1[0])} and {len(new_matrix2)} x {len(new_matrix2[0])}"
        )
    else:
        result_matrix = []
        for x in range(len(new_matrix1)):
            result_matrix.append([])
            for y in range(len(new_matrix1[0])):
                result_matrix[x].append(new_matrix1[x][y] - new_matrix2[x][y])
    return result_matrix


def divide(matrix1, matrix2):
    new_matrix1 = make_matrix(matrix1)
    new_matrix2 = make_matrix(matrix2)
    if len(new_matrix1) != len(new_matrix2) or len(new_matrix1[0]) != len(
        new_matrix2[0]
    ):
        raise TypeError(
            f"Cannot divide matrices of the size {len(new_matrix1)} x {len(new_matrix1[0])} and {len(new_matrix2)} x {len(new_matrix2[0])}"
        )
    else:
        result_matrix = []
        for x in range(len(new_matrix1)):
            result_matrix.append([])
            for y in range(len(new_matrix1[0])):
                result_matrix[x].append(new_matrix1[x][y] / new_matrix2[x][y])
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
