def read_csv(file_name):
    file = open(file_name)
    table = []
    for line in file:
        table.append(line.split(","))
    return table

def read_file(file_name, delimiter = " "):
    file = open(file_name)
    table = []
    for line in file:
        table.append(line.split(delimiter))
    return table
