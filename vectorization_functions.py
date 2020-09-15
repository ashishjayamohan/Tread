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
