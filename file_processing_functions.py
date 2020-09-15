def read_csv(file_name):
    """
    This function takes in a file path and will read the csv
    Remember that all your values must be seperated by a single comma
    """
    with open(file_name) as file:
        table = []
        for line in file:
            table.append(line.split(","))
    return table

def read_file(file_name, delimiter = " "):
    """
    This function is similar to read_csv but has a custom delimiter
    Note that this function returns all values in the table of type string
    """
    with open(file_name) as file:
        table = []
        for line in file:
            table.append(line.split(delimiter))
        return table

def write_csv(table, file_name):
    """
    write_csv() writes a comma-seperated-values file from a given table
    For custom delimiters, use write_file() below
    """
    with open(file_name, "w") as file:
        for j in table:
            file.write((",").join([str(i) for i in j]) + "\n")

def write_file(table, file_name, delimiter = " "):
    """
    This function is similar to write_csv() but utilizes a custom delimiter
    The default delimiter is a singular space
    """
    with open(file_name, "w") as file:
        for j in table:
            file.write((delimiter).join([str(i) for i in j]) + "\n")
