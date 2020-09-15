def add_column_values(table, column_values):
    for j in range(len(table)):
        table[j].append(column_values[j])
    return table

def remove_column(table, index):
    for j in table:
        j.pop(index)
    return table

def extract_column(table, index):
    arr = []
    for j in table:
        arr.append(j[index])
    return arr
