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
            sum += float(str(j))
        return sum
    else:
        raise TypeError('Add failed - Incorrect data type')

def average(arr, mode = "mixed"):
    """
    average(arr, mode) takes the average of a given array
    Once again, the modes of add() can be used here to denote what the type of the array is
    The function below, determine_mode(arr) can be used to determine the correct mode for your array
    """
    if len(arr) == 0: return 0.0
    return add(arr, mode)/len(arr)

def types(arr):
    """
    types(arr) will return an array of length equivalent to that of the input array
    This is analogous to the type() function typically carried out on a singular variable
    """
    return [type(a) for a in arr]

def highest_frequency(arr):
    """
    highest_frequency(arr) returns a tuple of the form ((items with most frequency), their frequency)
    This function looks for the number of occurrences of each value in the given array and returns the top results
    """
    if len(arr) == 0: return None
    dictionary = frequency(arr)
    max_value = max(dictionary.values())
    return (tuple(key for key, value in dictionary.items() if value == max_value), max_value)

def frequency(arr, cast=False):
    """
    frequency() returns a dictionary with keys set as elements from the array
    and values as their respective frequencies
    Frequency is determined as the number of times occurred in given array
    """
    dictionary = {}
    for j in arr:
        if((float(j) if cast else j) in dictionary):
            dictionary[(float(j) if cast else j)] += 1
        else:
            dictionary[(float(j) if cast else j)] = 1
    return dictionary

def determine_mode(arr):
    """
    determine_mode helps determine which mode is necessary for function like add() and average()
    Note that mixed does not check explicitly for mixed cases and may return an error at runtime if array
    elements are of unparseable types
    """
    dictionary = frequency(types(arr))
    if len(dictionary) == 0:
        return None
    elif(len(dictionary) == 1):
        if("int" in str(dictionary.keys())):
            return "int"
        elif("float" in str(dictionary.keys())):
            return "float"
        else:
            return "str"
    else:
        return "mixed"

def median(arr, __nosort=False):
    """
    Returns the median of a given array or the middle element of an array
    """
    sample = sorted(arr) if not __nosort else arr
    if(len(sample) % 2 == 1):
        return sample[len(sample) // 2]
    else:
        return (sample[len(sample)//2 - 1] + sample[len(sample)//2]) / 2

def quartiles(arr):
    '''
    Returns the minimum and maximum, the median, and the first and third quartiles.
    If only one value is provided, that value is used for all of the outputs.
    If two values are provided, the result will be (first, None, average, None, second).
    If three values are provided, the result will be (first, first, second, third, third).
    Format: (minimum, first quartile, median, third quartile, maximum)
    '''
    if len(arr) == 0:
        return None
    elif (len(arr) == 1):
        return (arr[0], arr[0], arr[0], arr[0], arr[0])
    elif (len(arr) == 2):
        sample = sorted(arr)
        return (sample[0], None, (sample[0] + sample[1]) / 2, None, sample[1])
    elif (len(arr) == 3):
        sample = sorted(arr)
        return (sample[0], sample[0], sample[1], sample[2], sample[2])
    else:
        sample = sorted(arr)
        return (sample[0], median(sample[:len(sample)//2], __nosort=True), median(sample, __nosort=True), median(sample[(len(sample)+1)//2:], __nosort=True), sample[len(sample) - 1])

def mode(arr):
    """
    Returns the mode of a given array
    Note that this function is different from the above determine_mode() function
    This returns the most common element in a given set
    """
    freqs = highest_frequency(arr)
    return None if len(freqs[0]) > 1 else freqs[0][0]

def length(arr):
    """
    Returns the length of a given array
    """
    return len(arr)

def pare_unique(arr):
    """
    Returns an array with all unique values in a given array
    """
    return list(set(arr))
