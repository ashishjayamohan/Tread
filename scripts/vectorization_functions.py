import basic_functions as bf

def cumulative_sum(arr):
    """
    Returns an array of len(arr)-1
    Each element shows the sum of all numbers in the indices prior to the given element
    """
    current_val = 0
    answer = []
    for j in arr:
        current_val += j
        answer.append(current_val)
    return answer

def skew(arr, mode = "float"):
    """
    This function calculates the skew of a given array
    Note that the mode must be specified as the automatic mode is float in this case
    """
    average = bf.average(arr, mode)
    answer = (bf.add([(average - i) ** 2 for i in arr], mode) / len(arr)) ** (1/2)
    return answer

def vector_function(arr, function):
    """
    Applies a given function upon every element in a given array
    """
    return [function(j) for j in arr]

def cast_all(arr, final_type = "int"):
    """
    Casts all elements in a given array to specified data type
    Raises a type error if type is not found
    """
    if(final_type == "int"):
        return [int(i) for i in arr]
    elif(final_type == "float"):
        return [float(i) for i in arr]
    elif(final_type == "str"):
        return [str(i) for i in arr]
    else:
        raise TypeError('Cast Failed - Incorrect data type')
