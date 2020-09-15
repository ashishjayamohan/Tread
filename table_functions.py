def add_column_values(table, column_title, column_values):
    table[0].append(column_title)
    for j in range(1, len(table)):
        table[j].append(column_values[j])
    return table

def remove_column(table, index):
    for j in table:
        j.pop(index)
    return table

def extract_column(table, index):
    return [j[index] for j in table]
    
def vector_function_column(table, function, index):
    for j in range(len(table)):
        table[j][index] = function(table[j][index])
    return table
