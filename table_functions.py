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
