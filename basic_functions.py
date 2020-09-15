def add(arr, mode = "mixed"):
    """
    Equivalent of Python's inbuilt sum() function, with compatibility for multiple data types
    This function takes in an array and a given mode, which can take on one of these data types:
    * int -- typical integer
    * float -- typical decimal value
    * str -- string
    * mixed -- consisting of all values above
    Note that in the mixed mode, the answer will be returned as a float value
    """
    if(mode == "int" or mode == "float"):
        sum = 0
        for j in arr:
            sum += j
        return sum
    elif(mode == "str"):
        sum = 0
        for j in arr:
            sum += float(j)
        return sum
    elif(mode == "mixed"):
        sum = 0
        for j in arr:
            summand = float(str(j))
            sum += summand
        return sum
    else:
        print('Function has failed. Incorrect data type.')

def average(arr, mode = "mixed"):
    """
    average(arr, mode) takes the average of a given array
    Once again, the modes of add() can be used here to denote what the type of the array is
    The function below, determine_mode(arr) can be used to determine the correct mode for your array
    """
    sum = add(arr, mode)
    answer = sum/len(arr)
    return answer

def types(arr):
    """
    types(arr) will return an array of length equivalent to that of the input array
    This is analogous to the type() function typically carried out on a singular variable
    """
    types = [type(a) for a in arr]
    return types

def highest_frequency(arr):
    """
    highest_frequency(arr) returns an array of length 2
    This function looks for the number of occurrences of each value in the given array and returns the top results
    Returned array has the structure: [value with highest frequency, number of occurrences of value]
    """
    dictionary = frequency(arr)
    max_value = dictionary[0]
    max_key = ""
    for a in dictionary:
        if(dictionary[a] > max_value):
            max_key = a
            max_value = dictionary[a]
    return [max_key, max_value]

def frequency(arr):
    """
    frequency() returns a dictionary with keys set as elements from the array and values as their respective frequencies
    Frequency is determined as the number of times occurred in given array
    """
    dictionary = {}
    for j in arr:
        if(j in dictionary):
            dictionary[j] += 1
        else:
            dictionary[j] = 1
    return dictionary

def determine_mode(arr):
    """
    determine_mode helps determine which mode is necessary for function like add() and average()
    Note that mixed does not check explicitly for mixed cases and may return an error at runtime if array
    elements are of unparseable types
    """
    type_arr = types(arr)
    dictionary = frequency(type_arr)
    if(len(dictionary) == 1):
        if("int" in str(dictionary.keys())):
            return "int"
        elif("float" in str(dictionary.keys())):
            return "float"
        else:
            return "str"
    else:
        return "mixed"
